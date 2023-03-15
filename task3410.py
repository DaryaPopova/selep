from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/6/6.html')
        dropdown_value = ((12434107696 * 3) * 2) + 1
        css_dropdown_value = "//option[text()='{}']".format(dropdown_value)
        browser.find_element(By.ID, 'selectId').click()
        browser.find_element(By.XPATH, css_dropdown_value).click()
        browser.find_element(By.ID, 'sendbutton').click()
        result_text = browser.find_element(By.ID, 'result').text
        print(result_text)
