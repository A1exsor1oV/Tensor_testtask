'''Кейс 1: ПОИСК В ЯНДЕКСЕ'''
#1) Зайти на yandex.ru
#2) Проверить наличие поля поиска
#3) Ввести в поиск Тензор
#4) Проверить, что появилась таблица с подсказками (suggest)
#5) При нажатии Enter появляется таблица результатов поиска
#6) Проверить 1 ссылка ведёт на сайт tensor.ru

import unittest
import tests.print_services as PServ
from tests.environment import TestEnvironment
from tests.exceptions import ObjectIsNotFoundOnWebPage
from tests.home_page import YandexHomePage
from tests.search_page import YandexSearchPage



class TextSearchTest(TestEnvironment):

    def test_text_search_case(self):
        """Тест-кейсы с заданым словом в Яндексе."""

        driver = self.driver
        homepage = YandexHomePage(driver)
        input_field = homepage.search_field

        self.assertIsNotNone(
            input_field,
            msg='None вместо объекта - поисковая строка не найдена.'
        )
        PServ.show_text_test_case_succeeded('input_search_field')

        input_field.clear()
        homepage.enter_word("Тензор")
        suggest_table = homepage.get_suggest_table()
        self.assertIsNotNone(
            suggest_table,
            msg='None вместо предложений - таблица вариантов не найдена.'
        )
        PServ.show_text_test_case_succeeded('suggest_table')

        homepage.press_enter()

        search_page = YandexSearchPage(driver)
        table_with_search_results = search_page.get_search_result_table()
        self.assertIsNotNone(
            table_with_search_results,
            msg='None вместо результатов поиска - таблица не обнаружена.'
        )
        PServ.show_text_test_case_succeeded('table_with_search_results')

        result_links = search_page.get_result_links()

        if result_links is None:
            raise ObjectIsNotFoundOnWebPage(
                'В таблице результатов поиска нет ссылок.'
            )

        self.assertGreater(
            len(result_links),
            0,
            msg='В результатах поиска нет предлагаемых вариантов.')
        PServ.show_text_test_case_succeeded('result_links')

        expected_link = "tensor.ru"
        expected_link_found = False

        for variant in result_links:
            item_link = variant.get_attribute('href')

            for i in range(5):
                if expected_link in item_link:
                    expected_link_found = True

        self.assertTrue(
            expected_link_found,
            msg=f'{expected_link} отсутствует в результатах поиска.'
        )
        PServ.show_text_test_case_succeeded('looking_for_link')


if __name__ == "__main__":
    unittest.main()
