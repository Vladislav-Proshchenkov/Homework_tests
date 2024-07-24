import requests

yandex_token = input('https://yandex.ru/dev/disk/poligon/\nВведите токен Яндекс.Диска: ')
URL_Yandex = "https://cloud-api.yandex.net/v1/disk/resources"

def create_folder(folder_name):
    params = {
        'path': f'{folder_name}',
    }
    headers = {
        'Authorization': f'OAuth {yandex_token}'
    }
    response = requests.put(URL_Yandex, headers=headers, params=params)
    return response.status_code

def yandex_folder_exist(folder_name):
    params = {
        'path': f'{folder_name}',
    }
    headers = {
        'Authorization': f'OAuth {yandex_token}'
    }
    response = requests.get(URL_Yandex, headers=headers, params=params)
    print(response.status_code)
    return response.status_code

def delete_folder(folder_name):
    params = {
        'path': f'{folder_name}',
    }
    headers = {
        'Authorization': f'OAuth {yandex_token}'
    }
    response = requests.delete(URL_Yandex, headers=headers, params=params)
    return response.status_code
