import os
from dotenv import load_dotenv
from instabot import Bot
from utils import get_base_path, get_images_path


def main():
    load_dotenv()

    instagram_path = os.path.join(get_base_path(), os.getenv('INSTAGRAM_DIR', 'instagram'))
    images_path = get_images_path()
    os.makedirs(instagram_path, exist_ok=True)

    bot = Bot(base_path=instagram_path)
    bot.login(username=os.getenv('INSTAGRAM_LOGIN'), password=os.getenv('INSTAGRAM_PASSWORD'))

    for filename in os.listdir(images_path):
        image_path = os.path.join(images_path, filename)
        if os.path.isfile(image_path):
            bot.upload_photo(image_path, caption='')

    # remove tmp files
    for filename in filter(lambda x: x.endswith('.REMOVE_ME'), os.listdir(images_path)):
        os.unlink(os.path.join(images_path, filename))


if __name__ == '__main__':
    main()
