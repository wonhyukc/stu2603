import os
import getpass
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

user_data_path = Path(__file__).parent / 'user_data'

def login():
    username = input("e캠퍼스 아이디를 입력하세요: ")
    password = getpass.getpass("e캠퍼스 비밀번호를 입력하세요: ")

    print("헤드리스 브라우저를 시작하여 로그인을 시도합니다...")
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_path,
            headless=True,
            viewport={"width": 1280, "height": 720}
        )
        page = context.pages[0] if context.pages else context.new_page()
        
        try:
            page.goto("https://ecampus.stu.ac.kr/")
            # Check if we need to click a login button first to reveal the form
            login_button = page.query_selector('.logininfo a')
            if login_button and "login" in login_button.get_attribute("href"):
                login_button.click()
            else:
                page.goto("https://ecampus.stu.ac.kr/login.php")
            
            page.wait_for_selector('input[name="username"]')
            page.fill('input[name="username"]', username)
            page.fill('input[name="password"]', password)
            page.click('.loginbtn') # or whatever the submit button class is, let's just press Enter
            
            # Press enter to submit
            page.press('input[name="password"]', 'Enter')
            
            # Wait for dashboard or error
            page.wait_for_url("**/index.php**", timeout=10000)
            print("로그인 성공! 세션이 저장되었습니다.")
        except Exception as e:
            print(f"로그인 실패: {e}")
        finally:
            context.close()

if __name__ == "__main__":
    login()
