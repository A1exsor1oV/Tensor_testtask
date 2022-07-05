from datetime import datetime


def show_set_up_info(test_driver=None) -> None:
    """Выводит на консоль дополнительную информацию о запуске тестового драйвера."""

    print(f'Started at: {datetime.now()}')
    print(f'{test_driver} driver environment set up.')
    print('----------------------------------------------------------')


def show_set_down_info() -> None:
    """Выводит на консоль дополнительную информацию об отключении тестового драйвера."""

    print('----------------------------------------------------------')
    print(f'Test environment destroyed. Driver will be shut down.')
    print(f'Run completed at: {datetime.now()}')


def show_text_test_case_succeeded(test_condition) -> None:
    """Выводит в консоль статус для тест-кейса с текстом."""

    test_cases_success_outputs = {
        'input_search_field': 'Input search field found. OK.',
        'suggest_table': 'Table with suggestions for searching found. OK.',
        'table_with_search_results': 'Table with results found. OK.',
        'result_links': 'Search results have variants. OK.',
        'looking_for_link': 'Looking for link found in given range. OK.'
    }
    print(test_cases_success_outputs[test_condition])


def show_image_test_case_succeeded(test_condition) -> None:
    """Выводит в консоль статус для тест-кейса с изображениями"""

    image_test_cases_success_outputs = {
        'image_block': 'Yandex image block "Картинки" found. OK.',
        'new_tab_url': 'New tab url opened as expected. OK.',
        'new_page_url': 'Opened page has url as expected. OK.',
        'image_search_text': 'Input search text same with chosen category. OK.',
        'image_view': 'Chosen image opened. OK.',
        'click_next_image': 'Next image opened. OK.',
        'return_to_image': 'View returned to first image as expected. OK.'
    }
    print(image_test_cases_success_outputs[test_condition])
