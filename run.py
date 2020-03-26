import os
from os import walk
from time import sleep

import serial

from flir_thermal_img_analyzer import thresholder
from gps import get_gps
from record import take_pic
from rpi.messaging.sending import send_alert


def list_files(directory, extension):
    file_list = []
    for (dirpath, dirnames, filenames) in walk(directory):
        file_list += [os.path.join(dirpath, f) for f in filenames if f.endswith(f".{extension}")]
    return file_list


if __name__ == '__main__':
    finite_images = False
    num_of_images = 3
    path = '/media/pi/'
    serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
    old_files = list_files(path, 'jpg')
    while num_of_images or not finite_images:
        num_of_images -= 1
        take_pic()  # Takes picture
        gps = get_gps()
        print(gps)
        sleep(4)  # 4 is the lowest working sleep time
        new_files = list_files(path, 'jpg')
        new_file = list(set(new_files) - set(old_files))[0]  # Selects first file if somehow multiple new files
        old_files = new_files
        print(new_file)
        above_threshold, org_img, new_img = thresholder(new_file, 50)
        #org_img.show()
        new_img.show()
        with open('log.txt', 'a') as file:
            file.write(f'{"file": "{new_file}", "gps": "{gps}", "above_threshold": "{above_threshold}"}\n')
        if above_threshold:
            # Send email
            subject = 'WARNING: Fire Detected'
            body = f"Possible fire detected by Forest Fire Finder at {gps[2]}\n\n" \
                   f"Google Maps Location:\n{gps[3]}\n\n" \
                   f"Geographical coordinates of drone:\n" \
                   f"Latitude:\t  {gps[0]}\n" \
                   f"Longitude:\t{gps[1]}\n" \
                   f"Altitude:\t   {gps[4]}{gps[5]}"
            send_alert(subject, body, (org_img, "Captured image"), (new_img, "Annotated image"))
