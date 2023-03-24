import time

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By


def count_spans_sum() -> int:
    summ: int = 0
    list_span = set()
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/infiniti_scroll_1/')
        time.sleep(1)
        while True:
            spans = browser.find_elements(By.CSS_SELECTOR, 'div#scroll-container span')
            for span in spans:
                if span.get_attribute('class') != 'last-of-list':
                    if span not in list_span:
                        summ += int(span.text)
                        span.find_element(By.TAG_NAME, 'input').send_keys(Keys.DOWN)
                        time.sleep(0.1)
                        list_span.add(span)
                else:
                    summ += int(browser.find_element(By.CSS_SELECTOR, 'span.last-of-list').text)
                    return summ


if __name__ == '__main__':
    summ = count_spans_sum()
    print(summ)
