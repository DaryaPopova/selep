import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    proxy = ['8.210.83.33:80']
    url = 'https://2ip.ru/'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxy)

    with webdriver.Chrome() as browser:
        browser.get(url)
        time.sleep(5)
        print(browser.find_element(By.CSS_SELECTOR, "div#d_clip_button span").text)
