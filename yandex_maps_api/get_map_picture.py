import requests


def get_map_picture(params):
    return requests.get('https://static-maps.yandex.ru/1.x/?', params=params)