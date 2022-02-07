import requests

API_KEY = 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3'


def search_maps(address):
    maps_request = f"https://search-maps.yandex.ru/v1/"
    maps_params = {
        "apikey": API_KEY,
        "ll": address,
        "text": f"организация",
        "spn": "0.001,0.001",
        "type": "biz",
        "lang": "ru_RU",
    }

    # Выполняем запрос.
    response = requests.get(maps_request, params=maps_params)

    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()
    else:
        raise RuntimeError(
            f"""Ошибка выполнения запроса:
            {maps_request}
            Http статус: {response.status_code} ({response.reason})""")

    features = json_response["features"]
    return features[0]["properties"] if features else None


# Получаем координаты объекта по его адресу.
def get_organization(address):
    toponym = search_maps(address)
    if not toponym:
        return None, None
    org_name = toponym["name"]
    org_address = toponym["description"]
    return org_name, org_address
