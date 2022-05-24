from pprint import pprint
import requests
import os
from progress.bar import Bar
from datetime import datetime



full_path = r'C:\Users\Владимир\PycharmProjects\pythonProject_2\Netology\Lesson\token.txt'

def get_token():
    with open(full_path) as file:
        token = file.readline()
    return token


class YaUploader:
    url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, token: str):
        self.token = token


    @property
    def header(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }



    def get_files(self):
        response = requests.get(f'{self.url}/files', headers=self.header)
        return response.json()


    def create_folder(self, path):
        requests.put(f'{self.url}?path={path}', headers=self.header)



    def upload_file(self, loadfile, savefile, replace=False):
        response = requests.get(f'{self.url}/upload?path={savefile}&overwrite={replace}', headers=self.header).json()
        with open(loadfile, 'rb') as f:
            try:
                requests.put(response['href'], files={'file': f})
                print('Файл загружен')
            except KeyError:
                print(response)



    def upload_folder(self, savepath, loadpath):
        date_folder = '{0}_{1}'.format(loadpath.split('\\')[-1], datetime.now().strftime("%Y.%m.%d-%H.%M.%S"))
        self.create_folder(savepath)
        for address, _, files in os.walk(loadpath):
            self.create_folder(
                '{0}/{1}/{2}'.format(savepath, date_folder, address.replace(loadpath, "")[1:].replace("\\", "/"))
            )
            bar = Bar('Loading', fill='x', max=len(files))
            for file in files:
                bar.next()
                self.upload_file(
                    '{0}\{1}'.format(address, file),
                    '{0}/{1}{2}/{3}'.format(savepath, date_folder, address.replace(loadpath, "").replace("\\", "/"),
                                            file)
                )

            bar.finish()
        print('Все файлы загружены')



if __name__ == '__main__':

    uploader = YaUploader(get_token())
    # uploader.upload_folder('IMAGE', r'E:\Personal\Private\image')
    uploader.upload_folder('melody', r'E:\Personal\MUSIC\melody')
    result = uploader.get_files()
    pprint(result)





















