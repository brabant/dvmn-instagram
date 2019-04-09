import os
import requests
from dotenv import load_dotenv
from utils import get_extension, download_file, get_images_path


def get_spacex_last_launch_images():
    url = 'https://api.spacexdata.com/v3/launches/latest'

    response = requests.get(url)
    if not response.ok:
        return False

    return response.json()['links']['flickr_images']


def fetch_spacex_last_launch():
    images = get_spacex_last_launch_images()
    for image_number, image_url in enumerate(images):
        download_file(image_url, 'spacex{}.{}'.format(image_number, get_extension(image_url)))


def main():
    load_dotenv()
    os.makedirs(get_images_path(), exist_ok=True)
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
