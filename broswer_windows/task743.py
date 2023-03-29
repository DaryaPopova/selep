import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/blank/modal/4/index.html')
        time.sleep(1)
        pins = browser.find_elements(By.CSS_SELECTOR, 'span.pin')
        for pin in pins:
            pin_text = pin.text
            browser.find_element(By.ID, 'check').click()
            alert = browser.switch_to.alert
            alert.send_keys(pin_text)
            alert.accept()
            result_text = browser.find_element(By.ID, 'result').text
            if result_text != 'Неверный пин-код':
                print(result_text)
                break


