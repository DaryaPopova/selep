from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/scroll/4/index.html')
        elements = browser.find_elements(By.CLASS_NAME, 'btn')
        summ = 0
        for element in elements:
            browser.execute_script("return arguments[0].scrollIntoView(true);", element)
            element.click()
            number_str = browser.find_element(By.ID, 'result').text
            summ += int(number_str)

        print(summ)
