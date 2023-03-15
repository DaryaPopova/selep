from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.html')
        elements = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
        length = len(elements)
        print(length)
        result: int = 0
        for element in elements:
            number = int(element.text)
            result += number
        print(result)