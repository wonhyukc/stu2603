import os
import json
import argparse
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

def load_config():
    config_path = Path(__file__).parent / 'config.json'
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

class EcampusNoticeUploader:
    def __init__(self, page, config, dry_run=False):
        self.page = page
        self.config = config
        self.selectors = config['selectors']
        self.dry_run = dry_run

    def navigate_to_board(self, course_info):
        print(f"[{course_info['title']}] 페이지로 이동 중...")
        
        # config에 board_url이 명시되어 있다면 해당 게시판으로 다이렉트 이동
        if 'board_url' in course_info and course_info['board_url']:
            self.page.goto(course_info['board_url'])
            self.page.wait_for_load_state('networkidle')
        else:
            self.page.goto(course_info['url'])
            self.page.wait_for_load_state('networkidle')
            # (기존처럼) 과목 홈일 경우 공지사항 탐색 로직 (필요시)
            if 'course/view.php' in self.page.url:
                print("과목 홈 감지됨, 공지사항으로 진입을 시도합니다.")
                try:
                    notice_link = self.page.locator(self.selectors['notice_board_link']).first
                    notice_link.wait_for(state="visible", timeout=3000)
                    notice_link.click()
                    self.page.wait_for_load_state('networkidle')
                except Exception as e:
                    print(f"공지사항 링크를 찾지 못했습니다. 게시판에 직접 접속을 권장합니다. ({str(e).splitlines()[0]})")

    def write_notice(self, title, html_content):
        print("글쓰기 버튼 클릭 중...")
        self.page.locator(self.selectors['write_button']).first.click()
        self.page.wait_for_load_state('networkidle')

        print("제목 입력 중...")
        self.page.locator(self.selectors['title_input']).fill(title)

        print("내용 입력 중 (에디터 감지 및 주입)...")
        # 1. Moodle Atto 에디터 (contenteditable div)
        if self.page.locator(self.selectors.get('atto_editor', "div.editor_atto_content[contenteditable='true']")).count() > 0:
            print("Atto 에디터가 감지되었습니다. contenteditable 영역에 직접 주입합니다.")
            atto = self.page.locator(self.selectors.get('atto_editor', "div.editor_atto_content[contenteditable='true']")).first
            # Atto는 focus/input 이벤트가 발생해야 숨겨진 textarea와 동기화됨
            atto.fill("") # focus 및 clear
            atto.evaluate(f"(node) => node.innerHTML = `{html_content}`")
            # 강제로 input 이벤트 발생시켜 폼 동기화 유도
            atto.evaluate("(node) => node.dispatchEvent(new Event('input', { bubbles: true }))")
        else:
            # 2. HTML 토글 소스 버튼이 있는 경우 (TinyMCE/CKEditor source mode 지원시)
            try:
                self.page.wait_for_selector(self.selectors['html_mode_button'], timeout=2000)
                self.page.locator(self.selectors['html_mode_button']).click()
                self.page.locator(self.selectors['html_textarea']).fill(html_content)
                
                # 저장 버튼이 있으면 클릭
                if self.page.locator(self.selectors['html_save_button']).count() > 0:
                    self.page.locator(self.selectors['html_save_button']).click()
            except Exception:
                # 3. Source mode 버튼이 없거나 실패하면 에디터 iframe 내부 body에 직접 삽입 시도
                print("소스코드 입력 버튼 없음, 에디터 내부 Body에 주입을 시도합니다.")
                try:
                    frame = self.page.frame_locator(self.selectors['editor_iframe']).first
                    frame.locator("body").evaluate(f"(node) => node.innerHTML = `{html_content}`")
                except Exception as e:
                    print("위지윅 에디터 프레임을 찾을 수 없습니다. 기본 텍스트 영역에 순수 텍스트를 입력합니다.")
                    self.page.keyboard.insert_text(html_content)
        
        # 확인을 위한 대기
        time.sleep(1)
        
        if self.dry_run:
            print("🔥 안전 훈련 모드(Dry-Run): 저장하지 않고 스크린샷만 찍습니다.")
        else:
            print("글 등록 중...")
            self.page.locator(self.selectors['submit_button']).first.click()
            self.page.wait_for_load_state('networkidle')
            time.sleep(1) # 최종 저장 후 등록 대기

def main():
    parser = argparse.ArgumentParser(description="eCampus Playwright Notice Uploader")
    parser.add_argument('--title', type=str, required=True, help="공지사항 제목")
    parser.add_argument('--file', type=str, required=True, help="업로드할 HTML/Markdown 파일 경로")
    parser.add_argument('--target', type=str, default='all', choices=['all', 'python', 'web01', 'web02'], help="대상 과목 식별자")
    parser.add_argument('--dry-run', action='store_true', help="실제 등록을 생략하고 캡처만 진행합니다.")
    args = parser.parse_args()

    # 콘텐츠 파일 읽기
    content_path = Path(args.file)
    with open(content_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Markdown을 입력받을 경우 단순 HTML 변환. (보통 워크플로우에 의해 HTML 변환된 것이 들어옴)
    if content_path.suffix.lower() == '.md':
        try:
            import markdown
            content = markdown.markdown(content)
        except ImportError:
            print("markdown 패키지가 없습니다. 텍스트 원문으로 업로드합니다.")

    config = load_config()
    targets = [args.target] if args.target != 'all' else ['python', 'web01', 'web02']

    # youtubePlaywright와 같은 user_data 관리 경로
    user_data_path = Path(__file__).parent / 'user_data'
    screenshots_path = Path(__file__).parent / 'screenshots'
    screenshots_path.mkdir(exist_ok=True)

    with sync_playwright() as p:
        # 최초 1회 로그인을 위해 user_data Persistent 컨텍스트 오픈
        print(f"브라우저 컨텍스트 실행: {user_data_path.absolute()}")
        context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_path,
            headless=False, # 눈으로 진행상황 및 eCampus SSO 확인 가능하도록
            viewport={"width": 1920, "height": 1080}, # 샌드박스에서도 모바일 메뉴로 축소되지 않도록 넓게 고정
            channel="chrome" # 사용자 개발용 크롬 브라우저 사용 시도
        )
        
        page = context.pages[0] if context.pages else context.new_page()
        uploader = EcampusNoticeUploader(page, config, args.dry_run)

        # 첫 번째 과목 주소로 먼저 이동하여 세션이 유효한지(로그인 페이지로 안 튕기는지) 확인
        test_url = config['courses'][targets[0]]['url']
        page.goto(test_url)
        page.wait_for_load_state('networkidle')
        
        # 주소창에 'login'이 포함되었다면 세션이 없거나 풀린 것임
        if 'login' in page.url:
            print("\n" + "="*60)
            print("🚨 [로그인 확인 대기]")
            print("세션이 없거나 로그아웃 되었습니다. 새로 뜬 창에서 수동 로그인을 진행해 주세요.")
            print("="*60)
            input("👉 로그인을 완전히 마친 후 [Enter] 키를 눌러 작업을 시작합니다... ")
            
            # [핵심] Moodle(eCampus)은 브라우저 종료 시 증발하는 '세션 쿠키'를 사용합니다.
            # 영구 로그인을 구현하기 위해 방금 받은 세션 쿠키를 30일 만료 쿠키로 강제 변조하여 user_data에 박제합니다.
            cookies = context.cookies()
            persistent_cookies = []
            for c in cookies:
                if c.get("expires", -1) == -1:
                    c["expires"] = time.time() + (30 * 24 * 60 * 60)  # 30일 뒤 만료로 변경
                persistent_cookies.append(c)
            context.clear_cookies()
            context.add_cookies(persistent_cookies)
            print("✅ eCampus 세션 쿠키의 수명을 영구(30일)로 연장하여 저장했습니다.")
        else:
            print("\n✅ 기존 user_data 세션을 통해 자동 로그인에 성공했습니다! (대기 없이 즉시 진행)")

        for target_key in targets:
            course_info = config['courses'][target_key]
            try:
                uploader.navigate_to_board(course_info)
                # (옵션) 과목마다 맞는 언어로 파일 내용(content) 및 title 분기 가능
                uploader.write_notice(args.title, content)
                
                # 결과 캡처
                stamp = time.strftime('%Y%m%d_%H%M%S')
                screen_file = screenshots_path / f"ecampus_{target_key}_{stamp}.png"
                page.screenshot(path=str(screen_file), full_page=True)
                print(f"✔️ {target_key} 완료. 캡처 저장됨: {screen_file}")
            
            except Exception as e:
                print(f"❌ {target_key} 처리 실패: {e}")

        print("모든 작업 종료. 3초 후 브라우저를 닫습니다.")
        time.sleep(3)
        context.close()

if __name__ == '__main__':
    main()
