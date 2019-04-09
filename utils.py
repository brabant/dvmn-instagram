import requests
import os


def get_base_path():
    return os.getenv('BASE_PATH', os.path.dirname(__file__))


def get_images_path():
    return os.path.join(get_base_path(), os.getenv('IMAGE_DIR', 'images'))


def get_extension(filename):
    return filename.split('.')[-1]


def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    if not response.ok:
        return False

    filepath = os.path.join(get_images_path(), filename)

    with open(filepath, 'wb') as file:
        file.write(response.content)
        return True

