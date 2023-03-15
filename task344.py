import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/2/2.html')
        browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624').click()
        result = browser.find_element(By.ID, 'result').text
        print(result)
        time.sleep(60)
