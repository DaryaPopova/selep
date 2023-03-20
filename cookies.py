import time
from pprint import pprint
from selenium import webdriver

if __name__ == '__main__':
    with webdriver.Chrome() as webdriver:
        webdriver.get('https://parsinger.ru/')
        cookie_dict = {
            'name': 'degu',  # Любое имя для cookie
            'value': 'begu',  # Любое значение для cookie
            'expiry': 1700000000,  # Время жизни cookie в секундах
            'path': '/',  # Директория на сервере дял которой будут доступны cookie
            'domain': 'parsinger.ru',  # Информация о домене и поддомене для которых доступны cookie
            'secure': True,  # or False   # Сигнал браузера о том что передать cookie только по защищённому HTTPS
            'httpOnly': True,  # or False # Ограничивает достук к cookie по средствам API
            'sameSite': 'Strict',  # or lax or none # Ограничение на передачу cookie между сайтами
        }
        webdriver.add_cookie(cookie_dict)
        cookies = webdriver.get_cookies()
        pprint(cookies)
        #for cookie in cookies:
            #print(cookie['name'])
        time.sleep(100)
