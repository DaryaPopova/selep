import time

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/infiniti_scroll_1/')
        summ = 0
        time.sleep(1)
        list_span = []
        while len(list_span) < 99:
            spans = [x for x in browser.find_elements(By.CSS_SELECTOR, 'div#scroll-container span')]
            for span in spans:
                if span.get_attribute('class') != 'last-of-list':
                    if span not in list_span:
                        summ += int(span.text)
                        span.find_element(By.TAG_NAME, 'input').send_keys(Keys.DOWN)
                        time.sleep(0.1)
                        list_span.append(span)
                else:
                    break
        summ += int(browser.find_element(By.CSS_SELECTOR, 'span.last-of-list').text)
        print(summ)
