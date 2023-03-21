from selenium import webdriver

if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/methods/3/index.html')
        cookies = browser.get_cookies()
        result: int = 0
        for cookie in cookies:
            name_number = int(str(cookie['name']).replace("secret_cookie_", ""))
            value_number = int(cookie['value'])
            if name_number % 10 == 0 or name_number % 2 == 0:
                result += value_number
        print(result)
