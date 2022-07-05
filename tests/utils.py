import hashlib
import os
import re
import urllib.request
from urllib.parse import unquote


def get_image_search_text(search_url: str) -> str:
    """Получение параметра из строки URL."""

    try:
        full_url = unquote(search_url)
    except TypeError:
        return

    query_param = 'text='
    match = re.search(query_param, full_url)

    if match is not None:
        start_idx, end_idx = match.span()
        url_params_part = full_url[end_idx:]
        end_symbol = '&'
        end_symbol_idx = url_params_part.index(end_symbol)
        search_text = url_params_part[:end_symbol_idx]

        return search_text


def hash_object(path):
    with open(path, 'rb') as file:
        hasher = hashlib.md5()
        hasher.update(file.read())
        return hasher.hexdigest()


def get_hashed_image(url: str, image_name: str, download_folder: str) -> str:
    """Возвращает изображение в виде строки."""

    directory_name = get_directory_path_or_none(download_folder)
    new_image_name = f'{directory_name}/{image_name}'

    if download_image_and_return_result(url, new_image_name):
        hash_name = hash_object(new_image_name)
        return hash_name


def get_directory_path_or_none(directory_name):
    """
    Возвращает полный путь к папке.
    """

    if create_directory_and_return_result(directory_name):
        try:
            current_path = os.getcwd()
        except OSError:
            return

        folder_path = f'{current_path}/{directory_name}'
        return folder_path


def create_directory_and_return_result(folder_name: str) -> bool:
    """
    Создаёт новую папку в текущей, если её ещё нет и возвращает статус True, если папка существует или уже создана.
    Иначе False.
    """

    if not os.path.exists(folder_name):
        try:
            os.mkdir(folder_name)
            return True
        except OSError as e:
            pass

    return True


def download_image_and_return_result(image_url: str, image_name: str) -> bool:
    """
    Загружает файл с указанного адреса и даёт ему имя.
    """
    try:
        urllib.request.urlretrieve(image_url, image_name)
        return True
    except Exception:
        pass
