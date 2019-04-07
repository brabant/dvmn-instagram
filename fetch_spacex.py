import requests
from utils import get_extension, download_file


def get_spacex_last_launch_images():
    url = 'https://api.spacexdata.com/v3/launches/latest'

    response = requests.get(url)
    if response.status_code != 200:
        return False

    return (x for x in response.json()['links']['flickr_images'])


def fetch_spacex_last_launch():
    images = get_spacex_last_launch_images()
    for image_number, image_url in enumerate(images):
        download_file(image_url, 'spacex{}.{}'.format(image_number, get_extension(image_url)))
        print(image_number, image_url)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
