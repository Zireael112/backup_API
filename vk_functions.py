import json
from dotenv import load_dotenv
import os
import requests
import time

list_info = []


class VkAPI:
    load_dotenv('.env_example')
    url_vk = os.getenv('URL_VK')
    vk_id = int(os.getenv('VK_ID'))
    vk_token = os.getenv('VK_TOKEN')

    def get_photo(self, offset=0, count=50):
        params = {
            'owner_id': self.vk_id,
            'album_id': 'profile',
            'access_token': self.vk_token,
            'offset': offset,
            'v': '5.131',
            'count': count,
            'extended': 1,
        }

        res = requests.get(self.url_vk + 'photos.get', params=params).json()
        return res

    def get_largest_photo(self):
        data = self.get_photo()
        count_photo = data['response']['count']
        i = 0
        count = 50

        while i <= count_photo:
            if count_photo == 0:
                print('Фотографии(ия) не найдены(а)!')
                break
            if i != 0:
                data = self.get_photo(offset=i, count=count)

            for files in data['response']['items']:
                dir_info = {}
                file_size = files['sizes'][-1]['type']
                file_url = files['sizes'][-1]['url']
                filename = files['likes']['count']
                time.sleep(0.1)

                # Запись информации о фотографии в файл
                dir_info['file_name'] = str(filename) + '.' + str(file_url.split('/')[-1].split('?')[0].split('.')[-1])
                dir_info['size'] = str(file_size)
                dir_info['url'] = (file_url)
                list_info.append(dir_info)

            i += count
            return list_info

    def recording(self, list):
        with open('info.json', 'w') as file:
            json.dump(list, file)
