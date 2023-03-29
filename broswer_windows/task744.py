import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/window_size/1/')
        time.sleep(1)
        browser.set_window_size(555 + 32, 555 + 171)
        time.sleep(1)
        text = browser.find_element(By.ID, 'result').text
        print(text)
