import requests
import os
from utils import get_extension, download_file


def download_hubble_image(image_id):
    url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    response = requests.get(url)
    if response.status_code != 200:
        return False

    image_url = response.json()['image_files'][-1]['file_url']
    print(image_url)
    return download_file(image_url, 'hubble{}.{}'.format(image_id, get_extension(image_url)))


def download_hubble_collection(collection_name):
    url = 'http://hubblesite.org/api/v3/images/{}'.format(collection_name)
    response = requests.get(url)
    if response.status_code != 200:
        return False

    images = response.json()
    for image_number, image_obj in enumerate(images):
        download_hubble_image(image_obj['id'])


def main():
    download_hubble_collection(os.getenv('HUBBLE_COLLECTION'))


if __name__ == '__main__':
    main()
