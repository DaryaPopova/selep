from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/expectations/1/index.html')
        element = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.ID, "btn"))).click()
        print(browser.find_element(By.ID, 'result').text)
