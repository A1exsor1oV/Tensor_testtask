import unittest

import tests.print_services as PServ
from tests.environment import TestEnvironment
from tests.exceptions import ObjectIsNotFoundOnWebPage
from tests.home_page import YandexHomePage
from tests.image_page import YandexImagePage
from tests.utils import get_hashed_image, get_image_search_text


IMAGES_BLOCK_NAME = 'Картинки'
IMAGES_BLOCK_URL = 'https://yandex.ru/images/'
IMAGES_BLOCK_NUMBER = 0
IMAGE_ORDER_NUMBER = 0
IMAGES_FOLDER_NAME = 'temp_images/'


class TestImageSearch(TestEnvironment):

    def test_yandex_image_case(self):

        driver = self.driver
        homepage = YandexHomePage(driver)
        yandex_images = homepage.get_images_block()

        if yandex_images is None:
            raise ObjectIsNotFoundOnWebPage(
                'Yandex image block is not found.'
            )

        expected_text = IMAGES_BLOCK_NAME
        self.assertEqual(
            expected_text.lower(),
            yandex_images.text.lower(),
            msg=f'Название выбранного блока на сайте'
                f'отличается от ожидаемого: {expected_text}'
        )
        PServ.show_image_test_case_succeeded('image_block')

        yandex_images.click()
        homepage.change_to_second_tab()

        image_page = YandexImagePage(driver)  # new class for page with images
        page_url = image_page.get_page_url()
        expected_url = IMAGES_BLOCK_URL
        self.assertIn(
            expected_url,
            page_url,
            msg=f'Искомый адрес: {expected_url} не найден в адресе сайта.'
        )
        PServ.show_image_test_case_succeeded('new_tab_url')

        categories = image_page.images_categories

        if len(categories) < 1:  # if list with categories is empty
            raise ObjectIsNotFoundOnWebPage(
                'No image categories found on web page.'
            )

        category = categories[IMAGES_BLOCK_NUMBER]
        category_url = image_page.get_image_category_url()

        try:
            category.click()
        except AttributeError:
            raise ObjectIsNotFoundOnWebPage(
                'None instead of category object found.'
            )

        new_page_url = image_page.get_page_url()
        self.assertEqual(
            category_url,
            new_page_url,
            msg=f'Opened page url: {new_page_url}.'
                f'Expected url: {category_url}'
        )
        PServ.show_image_test_case_succeeded('new_page_url')

        expected_text = category.text
        current_url = image_page.get_page_url()
        image_search_text = get_image_search_text(current_url)
        self.assertEqual(
            expected_text,
            image_search_text,
            msg=f'Text in search input: {image_search_text} is not'
                f'as expected: {expected_text}'
        )
        PServ.show_image_test_case_succeeded('image_search_text')

        preview_image = image_page.get_preview_image(IMAGE_ORDER_NUMBER)

        try:
            preview_image.click()
        except AttributeError:
            raise ObjectIsNotFoundOnWebPage(
                'None instead of preview_image object found.'
            )

        image_view = image_page.get_image_view()
        self.assertIsNotNone(
            image_view,
            msg='Image view is not found.'
        )
        PServ.show_image_test_case_succeeded('image_view')

        first_image_url = image_page.get_image_view_src()
        first_image = get_hashed_image(
            url=first_image_url,
            image_name='first_image.jpg',
            download_folder=IMAGES_FOLDER_NAME
        )

        image_page.slide_image_forward()
        second_image_url = image_page.get_image_view_src()
        second_image = get_hashed_image(
            url=second_image_url,
            image_name=f'second_image.jpg',
            download_folder=IMAGES_FOLDER_NAME
        )

        self.assertNotEqual(
            first_image,
            second_image,
            msg='No image change after clicking button to next image.'
        )
        PServ.show_image_test_case_succeeded('click_next_image')

        image_page.slide_image_backward()
        control_image_url = image_page.get_image_view_src()
        control_image = get_hashed_image(
            url=control_image_url,
            image_name=f'control_image.jpg',
            download_folder=IMAGES_FOLDER_NAME
        )
        self.assertEqual(
            first_image,
            control_image,
            msg='View returned to not same image after'
                'clicking backward button.'
        )
        PServ.show_image_test_case_succeeded('return_to_image')


if __name__ == "__main__":
    unittest.main()
