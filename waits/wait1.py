from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/expectations/2/index.html')
        element = WebDriverWait(browser, 10).until(EC.title_is('title changed'))
        print(element)
