import os
from pprint import pprint

BASE_PATH = os.getcwd()
print(BASE_PATH)
listdir = "files"

filelist = {}
for filename in os.listdir("files"):
    with open(os.path.join("files", filename), 'r', encoding='UTF-8') as file:
        file_lines = [i for i in file.readlines()]
        line_count = len(file_lines)
        filelist[filename] = (line_count, file_lines)
sorted_tuple = sorted(filelist.items(), key=lambda item: item[1])
data = dict(sorted_tuple)

with open('test.txt', 'w', encoding='utf-8') as file:
    for key, value in data.items():
        file.write(f'\nфайл - {key} \nколичество строк в файле {value[0]}\n')
        # print(f'\nфайл - {key} \nколичество строк в файле {value[0]}\n')
        for text in value[1]:
            file.write(f'\n{text.strip()}')
           # print(f'\n{text.strip()}')