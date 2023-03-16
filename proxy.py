import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    url = 'https://2ip.ru/'
    with webdriver.Chrome() as browser:
        browser.get(url)
        time.sleep(5)
        print(browser.find_element(By.CSS_SELECTOR, "div#d_clip_button span").text)
