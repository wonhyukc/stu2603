import json
from pathlib import Path
from playwright.sync_api import sync_playwright

config_path = Path(__file__).parent / 'config.json'
with open(config_path, 'r', encoding='utf-8') as f:
    config = json.load(f)

user_data_path = Path(__file__).parent / 'user_data'

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir=user_data_path,
        headless=True,
        viewport={"width": 1920, "height": 1080}
    )
    page = context.pages[0] if context.pages else context.new_page()
    url = config['courses']['web02']['url']
    print(f"가져올 주소: {url}")
    page.goto(url)
    page.wait_for_load_state('networkidle')
    html = page.content()
    out_file = Path(__file__).parent / 'real_board.html'
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"저장 완료. html 문자열 길이: {len(html)}")
    context.close()
