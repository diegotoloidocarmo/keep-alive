from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://simples-nacional.streamlit.app', timeout=60000, wait_until='domcontentloaded')
    page.wait_for_timeout(8000)
    text = page.inner_text('body')
    if 'gone to sleep' in text or 'get this app back up' in text:
        print('App dormindo - acordando...')
        page.click('button', timeout=5000)
        page.wait_for_timeout(30000)
        print('Acordado!')
    else:
        print('App ja estava no ar.')
    browser.close()
