from playwright.sync_api import sync_playwright
timeout=90000

def extract_html_from(url, wait_for):
    with sync_playwright() as p:
            browser=p.chromium.launch(headless=False)
            page=browser.new_page()
            page.goto(url, timeout=timeout)
            page.wait_for_load_state("networkidle", timeout=timeout)
            page.evaluate("()=>window.scroll(0, document.body.scrollHeight)")
            # page.screenshot(path="steam2.png")
            page.wait_for_load_state("domcontentloaded", timeout=timeout)
            # "div[class*='gASJ2lL']"
            page.wait_for_selector(wait_for, timeout=timeout)
            html=page.inner_html("body")
            browser.close()
            return html