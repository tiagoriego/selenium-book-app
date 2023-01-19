from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging
import time


class BookPy():

    _WAIT_SECS = 2

    _resource = {
        "login": "/#/login",
        "book": "/#/book",
        "new_book": "/#/new/book"
    }

    _form = {
        "login": {
            "field": {
                "username": "/html/body/app-root/app-login/form/section/div[2]/div/div/div[2]/div/div/input",
                "password": "/html/body/app-root/app-login/form/section/div[2]/div/div/div[3]/div/div/input"
            }
        },
        "new_book": {
            "field": {
                "title": "/html/body/app-root/app-new-book/section/form/div[2]/div[1]/div[1]/input",
                "author": "/html/body/app-root/app-new-book/section/form/div[2]/div[1]/div[2]/input",
                "dimensions": "/html/body/app-root/app-new-book/section/form/div[2]/div[1]/div[3]/input",
                "format": "/html/body/app-root/app-new-book/section/form/div[2]/div[1]/div[4]/input",
                "isbn": "/html/body/app-root/app-new-book/section/form/div[2]/div[2]/div[1]/input",
                "language": "/html/body/app-root/app-new-book/section/form/div[2]/div[2]/div[2]/input",
                "paperback": "/html/body/app-root/app-new-book/section/form/div[2]/div[2]/div[3]/input",
                "publication_date": "/html/body/app-root/app-new-book/section/form/div[2]/div[2]/div[4]/input",
                "publisher": "/html/body/app-root/app-new-book/section/form/div[2]/div[2]/div[5]/input"
            },
            "btn": {
                "save": "/html/body/app-root/app-new-book/section/form/div[1]/div/div[1]/button"
            }
        },
        "link": {
            "new_book": "/html/body/app-root/app-book/custom-header/header/nav/div/div/ul/li[2]/a",
            "logout": "/html/body/app-root/app-book/custom-header/header/nav/div/div/ul/ul/li/a"
        }
    }

    def __init__(self, url):
        self.url = url

    def initialize(self) -> bool:
        result = False
        self._driver = webdriver.Chrome()
        try:
            url = f'{self.url}{self._resource["login"]}'
            self._driver.get(url=url)

            assert "BooKPy" in self._driver.title
            assert url in self._driver.current_url

            result = True
        except Exception as e:
            logging.exception("Method 'initialize' failed")
        return result

    def close_browser(self):
        self._driver.close()

    def execute_login(self, user: dict) -> bool:
        # Form Login
        result = False
        try:
            logging.info(self._driver.current_url)

            elem_user = self._driver.find_element(
                By.XPATH, self._form["login"]["field"]["username"])
            elem_user.clear()
            elem_user.send_keys(user.get("username", {}))

            elem_pwd = self._driver.find_element(
                By.XPATH, self._form["login"]["field"]["password"])
            elem_pwd.clear()
            elem_pwd.send_keys(user.get("password", {}))

            elem_user.send_keys(Keys.ENTER)

            # Wait 2 seconds
            time.sleep(self._WAIT_SECS)

            assert f'{self.url}{self._resource["book"]}' in self._driver.current_url

            logging.info(self._driver.current_url)

            result = True
        except Exception as e:
            logging.exception("Method 'execute_login' failed")

        return result

    def execute_link_new_book(self) -> bool:
        # Form Book
        result = False
        try:
            elem_new_book = self._driver.find_element(
                By.XPATH, self._form["link"]["new_book"])
            elem_new_book.click()

            time.sleep(self._WAIT_SECS)

            assert f'{self.url}{self._resource["new_book"]}' in self._driver.current_url

            logging.info(self._driver.current_url)

            result = True

        except Exception as e:
            logging.exception("Method 'execute_link_book' failed")

        return result

    def execute_new_book(self, data: dict) -> bool:
        # Form New Book
        result = False
        try:
            form_el_01 = self._driver.find_element(
                By.XPATH, self._form["new_book"]["field"]["title"])
            form_el_02 = self._driver.find_element(
                By.XPATH, self._form["new_book"]["field"]["author"])
            form_el_03 = self._driver.find_element(
                By.XPATH, self._form["new_book"]["field"]["dimensions"])
            form_el_04 = self._driver.find_element(
                By.XPATH, self._form["new_book"]["field"]["format"])
            form_el_05 = self._driver.find_element(
                By.XPATH, self._form["new_book"]["field"]["isbn"])
            form_el_06 = self._driver.find_element(
                By.XPATH, self._form["new_book"]["field"]["language"])
            form_el_07 = self._driver.find_element(
                By.XPATH, self._form["new_book"]["field"]["paperback"])
            form_el_08 = self._driver.find_element(
                By.XPATH, self._form["new_book"]["field"]["publication_date"])
            form_el_09 = self._driver.find_element(
                By.XPATH, self._form["new_book"]["field"]["publisher"])

            form_el_01.clear()
            form_el_01.send_keys(data.get("title", {}))

            form_el_02.clear()
            form_el_02.send_keys(data.get("author", {}))

            form_el_03.clear()
            form_el_03.send_keys(data.get("dimensions", {}))

            form_el_04.clear()
            form_el_04.send_keys(data.get("format", {}))

            form_el_05.clear()
            form_el_05.send_keys(data.get("isbn", {}))

            form_el_06.clear()
            form_el_06.send_keys(data.get("language", {}))

            form_el_07.clear()
            form_el_07.send_keys(data.get("paperback", {}))

            form_el_08.clear()
            form_el_08.send_keys(data.get("publication_date", {}))

            form_el_09.clear()
            form_el_09.send_keys(data.get("publisher", {}))

            btn_form_el_save = self._driver.find_element(
                By.XPATH, self._form["new_book"]["btn"]["save"])
            btn_form_el_save.click()

            time.sleep(self._WAIT_SECS)

            assert f'{self.url}{self._resource["book"]}' in self._driver.current_url

            logging.info(self._driver.current_url)

            btn_logout = self._driver.find_element(
                By.XPATH, self._form["link"]["logout"])
            btn_logout.click()

            time.sleep(self._WAIT_SECS)

            assert f'{self.url}{self._resource["login"]}' in self._driver.current_url

            logging.info(self._driver.current_url)

            result = True

        except Exception as e:
            logging.exception("Method 'execute_new_book' failed")

        return result
