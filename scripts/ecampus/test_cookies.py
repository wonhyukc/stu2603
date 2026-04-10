from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context("user_data", headless=True)
    cookies = context.cookies()
    updated = False
    new_cookies = []
    for c in cookies:
        if c.get("expires", -1) == -1:
            c["expires"] = 9999999999
            updated = True
            print(f"Session Cookie modified: {c['name']}")
        new_cookies.append(c)
    if updated:
        context.add_cookies(new_cookies)
        print("Updated cookies set.")
    print("Total cookies:", len(cookies))
    context.close()
