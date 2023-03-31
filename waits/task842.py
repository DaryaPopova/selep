from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/expectations/4/index.html')
        WebDriverWait(browser, 5, 1).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
        if WebDriverWait(browser, 20, 0.1).until(EC.title_contains("JK8HQ")):
            print(browser.title)
