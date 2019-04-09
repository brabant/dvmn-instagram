import os
import requests
from dotenv import load_dotenv
from utils import get_extension, download_file, get_images_path


def download_hubble_image(image_id):
    url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    response = requests.get(url)
    if not response.ok:
        return False

    image_url = response.json()['image_files'][-1]['file_url']
    return download_file(image_url, 'hubble{}.{}'.format(image_id, get_extension(image_url)))


def download_hubble_collection(collection_name):
    url = 'http://hubblesite.org/api/v3/images/{}'.format(collection_name)
    response = requests.get(url)
    if not response.ok:
        return False

    images = response.json()
    for image_obj in images:
        download_hubble_image(image_obj['id'])


def main():
    load_dotenv()
    os.makedirs(get_images_path(), exist_ok=True)
    download_hubble_collection(os.getenv('HUBBLE_COLLECTION'))


if __name__ == '__main__':
    main()
