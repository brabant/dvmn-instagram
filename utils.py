import requests
import os
from dotenv import load_dotenv


load_dotenv()

BASE_PATH = os.getenv('BASE_PATH', os.path.dirname(__file__))
IMAGES_PATH = os.path.join(BASE_PATH, os.getenv('IMAGE_DIR', 'images'))
os.makedirs(IMAGES_PATH, exist_ok=True)


def get_extension(filename):
    return filename.split('.')[-1]


def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code != 200:
        return False

    filepath = os.path.join(IMAGES_PATH, filename)

    with open(filepath, 'wb') as file:
        file.write(response.content)
        return True
