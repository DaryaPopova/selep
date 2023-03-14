# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.by import By


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    url = 'https://stepik.org/'
    browser = webdriver.Chrome('/home/degu/chromedriver_linux64/chromedriver')
    browser.get(url)
    button = browser.find_element(By.ID, "sale_button").click()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
