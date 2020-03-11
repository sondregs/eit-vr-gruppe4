from os import walk
from time import sleep

import serial

from record import take_pic
from Gps.Neo6mGPS import getGPS


def list_files(directory, extension):
    file_list = []
    for (dirpath, dirnames, filenames) in walk(directory):
        file_list += [f for f in filenames if f.endswith('.' + extension)]
    return file_list

num = 3
path = '/media/pi/'
serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
old_files = list_files(path, 'jpg')
for i in range(num):
    take_pic() # Takes picture
    gps = getGPS()
    print(gps)
    sleep(4) # 4 is the lowest working sleep time
    new_files = list_files(path, 'jpg')
    new_file = list(set(new_files) - set(old_files))[0] # Selects first file if somehow multiple new files
    print(new_file)
    old_files = new_files
