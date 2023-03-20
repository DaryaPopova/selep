from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/methods/1/index.html')
        while 'refresh page' == browser.find_element(By.ID, 'result').text:
            browser.refresh()
        print(browser.find_element(By.ID, 'result').text)
        time.sleep(60)
