import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/blank/modal/3/index.html')
        time.sleep(1)
        buttons = browser.find_elements(By.CSS_SELECTOR, 'input.buttons')
        for button in buttons:
            button.click()
            alert = browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            browser.find_element(By.ID, 'input').send_keys(alert_text)
            browser.find_element(By.ID, 'check').click()
            result_text = browser.find_element(By.ID, 'result').text
            if result_text != 'Неверный пин-код':
                print(result_text)
                break
