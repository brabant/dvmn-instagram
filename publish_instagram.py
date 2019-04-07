import os
from instabot import Bot
from utils import BASE_PATH, IMAGES_PATH

INSTAGRAM_PATH = os.path.join(BASE_PATH, os.getenv('INSTAGRAM_DIR', 'instagram'))


def main():
    os.makedirs(INSTAGRAM_PATH, exist_ok=True)

    bot = Bot(base_path=INSTAGRAM_PATH)
    bot.login(username=os.getenv('INSTAGRAM_LOGIN'), password=os.getenv('INSTAGRAM_PASSWORD'))

    for filename in os.listdir(IMAGES_PATH):
        image_path = os.path.join(IMAGES_PATH, filename)
        if os.path.isfile(image_path):
            bot.upload_photo(image_path, caption='')

    # remove tmp files
    for filename in filter(lambda x: x.endswith('.REMOVE_ME'), os.listdir(IMAGES_PATH)):
        os.unlink(os.path.join(IMAGES_PATH, filename))


if __name__ == '__main__':
    main()
