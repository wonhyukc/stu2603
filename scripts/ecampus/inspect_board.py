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
        headless=True
    )
    page = context.pages[0] if context.pages else context.new_page()
    url = config['courses']['python']['url']
    print(f"가져올 주소: {url}")
    page.goto(url)
    page.wait_for_load_state('networkidle')
    html = page.content()
    with open('board.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"저장 성공, HTML 길이: {len(html)}")
    context.close()
