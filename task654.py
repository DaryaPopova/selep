import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


def count_elements_sum() -> int:
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/infiniti_scroll_2/')
        time.sleep(1)
        numbers_sum = 0
        set_element = set()
        scroll_element = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
        while True:
            ActionChains(browser).move_to_element(scroll_element).scroll_by_amount(0, 440).perform()
            elements = browser.find_elements(By.CSS_SELECTOR, 'div#scroll-container p')
            if not all(element in set_element for element in elements):
                for element in elements:
                    if element not in set_element:
                        numbers_sum += int(element.text)
                        set_element.add(element)
            else:
                return numbers_sum


if __name__ == '__main__':
    summ = count_elements_sum()
    print(summ)
