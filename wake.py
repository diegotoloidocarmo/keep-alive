from playwright.sync_api import sync_playwright
  import time

  with sync_playwright() as p:
      browser = p.chromium.launch()
      page = browser.new_page()
      page.goto('https://simples-nacional.streamlit.app', timeout=60000, wait_until='domcontentloaded')
      time.sleep(8)
      text = page.inner_text('body')
      if 'gone to sleep' in text or 'get this app back up' in text:
          print('App dormindo - acordando...')
          page.click('button', timeout=5000)
          time.sleep(30)
          print('Acordado!')
      else:
          print('App ja estava no ar.')
      browser.close()
