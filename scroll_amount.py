from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/infiniti_scroll_2/')
        div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
        for x in range(10):
            ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
