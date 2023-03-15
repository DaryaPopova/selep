from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/4/4.html')
        elements = browser.find_elements(By.CLASS_NAME, 'check')
        for element in elements:
            element.click()
        browser.find_element(By.CLASS_NAME, 'btn').click()
        result_text = browser.find_element(By.ID, 'result').text
        print(result_text)



