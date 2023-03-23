from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/scroll/2/')
        summ = 0
        checkboxes = browser.find_elements(By.CSS_SELECTOR, 'input')
        for checkbox in checkboxes:
            checkbox.send_keys(Keys.DOWN)
            checkbox.click()
            id_attr = checkbox.get_attribute('id')
            number_text = browser.find_element(By.ID, "result{}".format(id_attr)).text
            if number_text != '':
                summ += int(number_text)

        print(summ)
