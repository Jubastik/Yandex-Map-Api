import requests
from io import BytesIO
from PIL import Image, ImageQt
import sys


def get_map_picture(params):
    response = requests.get("https://static-maps.yandex.ru/1.x/?", params=params)
    if not response:
        print("Ошибка выполнения запроса:")
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    return ImageQt.ImageQt(Image.open(BytesIO(response.content)))
