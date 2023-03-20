from selenium import webdriver
import time

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/methods/3/index.html')
        cookies = browser.get_cookies()
        result: int = 0
        for cookie in cookies:
            result += int(cookie['value'])
        print(result)
