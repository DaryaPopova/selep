from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/methods/5/index.html')
        links = browser.find_elements(By.CSS_SELECTOR, "div.urls a")
        max_date = 0
        array = []
        for link in links:
            link.click()
            expiration_date = browser.get_cookies()[0]['expiry']
            array.append(expiration_date)
            if expiration_date > max_date:
                max_date = expiration_date
            browser.back()
        print(max_date)
