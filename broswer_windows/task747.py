import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/blank/3/index.html')
        time.sleep(1)
        buttons = browser.find_elements(By.CSS_SELECTOR, 'input.buttons')
        summ = 0
        for button in buttons:
            button.click()
        for x in range(1, len(browser.window_handles)):
            browser.switch_to.window(browser.window_handles[x])
            summ += int(browser.title)
        print(summ)
