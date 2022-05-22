import requests
from dotenv import load_dotenv
import os
import time
from tqdm import tqdm


class YandexAPI:
    load_dotenv('.env_example')
    host = 'https://cloud-api.yandex.net'

    def __init__(self, ya_token=os.getenv('YA_TOKEN')):
        self.ya_token = ya_token

    def create_folder(self, name):
        response = requests.put(self.host + "/v1/disk/resources",
                                params={"path": f'/{name}'},
                                headers={"Authorization": self.ya_token})
        print(f'Создан файл с именем {name}\n')
        return response.ok

    def upload(self, list):
        name_folder = input('Введите имя для создания папки на яндекс диске: ')
        self.create_folder(name_folder)
        print('Начинается загрузка файлов')
        for i in list:
            try:
                for _ in tqdm(list):
                    time.sleep(0.3)
                load = requests.post(self.host + '/v1/disk/resources/upload',
                                     params={'path': f'/{name_folder}/{i["file_name"]}',
                                             'url': i["url"]},
                                     headers={'Authorization': self.ya_token})
                if load.status_code == 202 or load.status_code == 201:
                    time.sleep(0.1)
                    print('Успешно!\n')
                    time.sleep(0.1)
            except:
                print('Произошла неизвестная ошибка, повторите попытку!')
        print("Загрузка завершена!")