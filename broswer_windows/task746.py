import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def find_window_size() -> dict:
    window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
    delta_x = 32
    delta_y = 171
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/window_size/2/index.html')
        time.sleep(1)
        for x in window_size_x:
            for y in window_size_y:
                browser.set_window_size(x + delta_x, y + delta_y)
                text = browser.find_element(By.ID, 'result').text
                if text != '':
                    window_size = {'width': x, 'height': y}
                    print(window_size)
                    return window_size


if __name__ == '__main__':
    find_window_size()
