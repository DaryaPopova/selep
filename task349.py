import time

from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/7/7.html')
        browser.find_element(By.ID, 'opt').click()
        elements = browser.find_elements(By.TAG_NAME, 'option')
        result: int = 0
        for element in elements:
            element_value = int(element.text)
            result += element_value
        print(result)
        browser.find_element(By.ID, 'input_result').send_keys(result)
        browser.find_element(By.ID, 'sendbutton').click()
        time.sleep(60)
