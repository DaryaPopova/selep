import time
from math import sqrt

from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        time.sleep(1)
        sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
                 'http://parsinger.ru/blank/1/3.html',
                 'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html',
                 'http://parsinger.ru/blank/1/6.html', ]
        for site in sites:
            browser.execute_script('window.open("{}");'.format(site))
        summ = 0
        for x in range(1, len(browser.window_handles)):
            browser.switch_to.window(browser.window_handles[x])
            browser.find_element(By.CSS_SELECTOR, "input.checkbox_class").click()
            number = int(browser.find_element(By.ID, 'result').text)
            summ += sqrt(number)
        print(summ)
