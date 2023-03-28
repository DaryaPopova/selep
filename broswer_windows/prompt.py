import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/blank/modal/1/index.html')
        browser.find_element(By.ID, 'prompt').click()
        time.sleep(2)
        prompt = browser.switch_to.alert
        prompt.send_keys('Введёный текст')
        prompt.accept()
        time.sleep(.5)
        print(browser.find_element(By.ID, 'result').text)
