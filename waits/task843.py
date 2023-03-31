import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/expectations/5/index.html')
        time.sleep(1)
        button = WebDriverWait(browser, 4, 1).until(EC.element_to_be_clickable(browser.find_element(By.ID, 'btn')))
        button.click()
        time.sleep(1)
        element = WebDriverWait(browser, 20, 0.1)\
            .until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY')))
        print(element.text)
