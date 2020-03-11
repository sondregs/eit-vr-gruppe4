from os import walk
import os
from time import sleep
import serial
from record import take_pic
from gps import get_gps


def list_files(directory, extension):
    file_list = []
    for (dirpath, dirnames, filenames) in walk(directory):
        file_list += [os.path.join(dirpath,f) for f in filenames if f.endswith('.' + extension)]
    return file_list

if __name__ == '__main__':
    num = 3
    path = '/media/pi/'
    serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
    old_files = list_files(path, 'jpg')
    for i in range(num):
        take_pic() # Takes picture
        gps = get_gps()
        print(gps)
        sleep(4) # 4 is the lowest working sleep time
        new_files = list_files(path, 'jpg')
        new_file = list(set(new_files) - set(old_files))[0] # Selects first file if somehow multiple new files
        old_files = new_files
        print(new_file)
        with open('log.txt', 'a') as file:
            file.write('{"file": "%s", "gps": "%s""}\n' % (new_file, gps))