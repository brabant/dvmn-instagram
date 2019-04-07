# Загрузка изображений космической тематики в Инстаграм

Скрипт для загрузки изображений из SpaceX и Hubble в профиль Инстаграм

### Как установить

После клонирования проекта создайте в корень файл .env с таким содержимым:

```
IMAGES_DIR=images
HUBBLE_COLLECTION=holiday_cards
INSTAGRAM_DIR=instagram
INSTAGRAM_LOGIN=_Instagram username_
INSTAGRAM_PASSWORD=_Instagram password_
```

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Пример запуска
Скачивание последних изображений из SpaceX
```
python fetch_spacex.py
```

Скачивание изображений Hubble из коллекции, которая указана в файле .env
```
python fetch_hubble.py
```

Заргузка скачанных файлов в Instagram
```
python publish_instagram.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
