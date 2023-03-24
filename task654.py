import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


def count_spans_sum() -> int:
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/infiniti_scroll_2/')
        time.sleep(1)
        scroll_element = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
        for x in range(100):
            ActionChains(browser).move_to_element(scroll_element).scroll_by_amount(0, 440).perform()
        elements = browser.find_elements(By.CSS_SELECTOR, 'div#scroll-container p')
        numbers_sum = 0
        for element in elements:
            numbers_sum += int(element.text)
        return numbers_sum


if __name__ == '__main__':
    summ = count_spans_sum()
    print(summ)
