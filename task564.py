from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/methods/5/index.html')
        links = browser.find_elements(By.CSS_SELECTOR, "div.urls a")
        max_date = 0
        number = 0
        for link in links:
            link.click()
            expiration_date = browser.get_cookies()[0]['expiry']
            if expiration_date > max_date:
                max_date = expiration_date
                number = browser.find_element(By.ID, 'result').text
            browser.back()
        print(number)
