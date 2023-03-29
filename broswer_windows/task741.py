import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/blank/modal/2/index.html')
        time.sleep(1)
        buttons = browser.find_elements(By.TAG_NAME, 'input')
        for button in buttons:
            button.click()
            alert = browser.switch_to.alert
            alert.accept()
            result_text = browser.find_element(By.CSS_SELECTOR, 'p#result').text
            if result_text != '':
                print(result_text)
                break
