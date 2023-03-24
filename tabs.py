import time
from selenium import webdriver

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        result = []
        browser.get('http://parsinger.ru/blank/2/1.html')
        time.sleep(1)
        browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
        browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
        browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')
        time.sleep(2)
        print(browser.window_handles)
