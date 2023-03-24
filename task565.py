import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def count_elements_sum() -> int:
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/infiniti_scroll_3/')
        time.sleep(1)
        scroll_containers = browser.find_elements(By.CSS_SELECTOR, "div[class *= scroll-container]")
        global_summ = 0
        for scroll_container in scroll_containers:
            global_summ += count_elements_window_sum(scroll_container, browser)
        return global_summ


def count_elements_window_sum(scroll_container: WebElement, browser: webdriver) -> int:
    set_element = set()
    scroll_element = scroll_container.find_element(By.TAG_NAME, 'div')
    numbers_sum = 0
    while True:
        ActionChains(browser).move_to_element(scroll_element).scroll_by_amount(0, 440).perform()
        elements = scroll_container.find_elements(By.TAG_NAME, 'span')
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
