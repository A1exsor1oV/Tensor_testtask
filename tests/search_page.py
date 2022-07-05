from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from tests.base_page import BasePage


class SearchLocator(object):

    search_result_table = (By.XPATH, '//ul[@id="search-result"]')
    result_links = (By.CSS_SELECTOR, '#search-result > li:nth-child(3) > div > div.Organic.organic.Typo.Typo_text_m.Typo_line_s.i-bem > div.VanillaReact.OrganicTitle.OrganicTitle_multiline.Typo.Typo_text_l.Typo_line_m.organic__title-wrapper > a')


class YandexSearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_search_result_table(self):
        return self.find_elem(SearchLocator.search_result_table, time=15)

    def get_result_links(self) -> list:
        return self.find_elems(SearchLocator.result_links)
