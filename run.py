from os import walk
from time import sleep
from record import take_pic


def list_files(directory, extension):
    file_list = []
    for (dirpath, dirnames, filenames) in walk(directory):
        file_list += [f for f in filenames if f.endswith('.' + extension)]
    return file_list


num = 3
path = '/media/pi/'
old_files = list_files(path, 'jpg')
for i in range(num):
    take_pic()
    sleep(5)
    new_files = list_files(path, 'jpg')
    print(list(set(new_files) - set(old_files)))
    old_files = new_files
