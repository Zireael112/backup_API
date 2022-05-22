from pprint import pprint

from vk_functions import VkAPI
from yandex_functions import YandexAPI


def make_photo():
    exampl_vk = VkAPI()
    list_info = exampl_vk.get_largest_photo()
    exampl_vk.recording(list_info)
    exampl_ya = YandexAPI()
    exampl_ya.upload(list_info)
    with open('info.json', 'r') as f:
        pprint(f.read())


if __name__ == '__main__':
    make_photo()
