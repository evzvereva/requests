import requests
import os


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        headers = {'Authorization': ''}
        file_name = os.path.basename(self.file_path)
        response_get = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', headers=headers,
                                    params={'path': file_name, 'overwrite': 'true'})
        href = response_get.json()['href']
        with open(self.file_path, 'rb') as f:
            response_put = requests.put(href)
        return response_put.status_code


if __name__ == '__main__':
    uploader = YaUploader('/home/ekaterina/Downloads/VZvx.gif')
    result = uploader.upload()
    if result == 201:
        print('Файл был успешно загружен!')
