import unittest
from selenium import webdriver
import tests.print_services as PServ


class TestEnvironment(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://yandex.ru/")
        self.driver.set_page_load_timeout(10)
        PServ.show_set_up_info('Chrome')
        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()

    def tearDown(self) -> None:
        driver = self.driver
        if driver is not None:
            PServ.show_set_down_info()
            driver.close()
            driver.quit()

