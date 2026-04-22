import json
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

user_data_path = Path(__file__).parent / 'user_data'

with sync_playwright() as p:
    print("브라우저를 실행합니다. 화면에 브라우저가 나타나면 e캠퍼스에 로그인해 주세요.")
    context = p.chromium.launch_persistent_context(
        user_data_dir=user_data_path,
        headless=False,
        viewport={"width": 1280, "height": 720}
    )
    page = context.pages[0] if context.pages else context.new_page()
    page.goto("https://ecampus.stu.ac.kr/")
    
    print("로그인이 완료될 때까지 대기합니다. (최대 120초)")
    try:
        # 로그인 후 나타나는 특정 요소(예: 로그아웃 버튼이나 사용자 이름)를 기다릴 수도 있지만,
        # 사용자가 직접 조작할 수 있도록 시간을 줍니다.
        # page.wait_for_selector(".usertext", timeout=120000)
        # 그냥 60초 정도 여유있게 대기하거나, URL 변경을 감지합니다.
        page.wait_for_url("**/login.php**", timeout=5000)
        print("로그인 페이지입니다. 로그인을 진행해주세요.")
        page.wait_for_url("**/index.php**", timeout=120000)
        print("로그인이 감지되었습니다. 세션을 저장합니다.")
    except Exception as e:
        print("대기 시간이 초과되었거나 이미 로그인되어 있을 수 있습니다.")
    
    # 추가로 5초 더 대기하여 쿠키가 완전히 저장되도록 함
    time.sleep(5)
    print("세션 쿠키가 업데이트 되었습니다.")
    context.close()
