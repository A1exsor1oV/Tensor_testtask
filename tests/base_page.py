from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait as webdw
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_elem(self, locator, time=10):
        try:
            element = webdw(self.driver, time).until(
                ec.presence_of_element_located(locator),
                message=f"Не удается найти элемент по локатору {locator}"
            )
            return element
        except TimeoutException as e:
            print(e.msg)
            pass

    def find_elems(self, locator, time=10):
        try:
            elements = webdw(self.driver, time).until(
                ec.presence_of_all_elements_located(locator),
                message=f"Не удается найти элементы по локатору {locator}"
            )
            return elements
        except TimeoutException as e:
            print(e.msg)
            pass

    def get_page_url(self) -> str:
        return self.driver.current_url

    def change_to_second_tab(self):
        new_page = self.driver.window_handles[1]
        return self.driver.switch_to.window(new_page)
