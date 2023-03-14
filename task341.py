import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://stepik-parsing.ru/selenium/1/1.html')
        #browser.find_element(By.CLASS_NAME, 'form').send_keys('Text')
        elements = browser.find_elements(By.CLASS_NAME, 'form')
        for element in elements:
            element.send_keys('Text')
        browser.find_elements(By.CLASS_NAME, 'btn')

        #time.sleep(5)
