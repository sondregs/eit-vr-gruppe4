import os
from os import walk
from time import sleep

import serial

from flir_thermal_img_analysis.flir_thermal_img_analyzer import thresholder
from gps import get_gps
from record import take_pic
from rpi.messaging import sending
from rpi.messaging.sending import send_alert
from util import logging
from util.logging import IMAGING_LOGGER


def list_images(directory, extension="jpg"):
    file_list = []
    for dirpath, dirnames, filenames in walk(directory):
        file_list += [os.path.join(dirpath, f) for f in filenames if f.endswith(f".{extension}")]
    return file_list


def get_newest_image(new_images: list, old_images: list):
    newest_images = list(set(new_images) - set(old_images))
    if newest_images:
        return newest_images[0]  # selects first file if somehow multiple new files
    else:
        return None


if __name__ == '__main__':
    logging.init()
    sending.init()

    finite_images = False
    num_of_images = 3
    path = '/media/pi/'
    serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
    old_images = list_images(path)

    while num_of_images or not finite_images:
        num_of_images -= 1
        take_pic()  # takes picture
        gps = get_gps()
        sleep(4)  # 4 is the lowest working sleep time

        new_images = list_images(path)
        newest_image = get_newest_image(new_images, old_images)
        if not newest_image:
            continue

        IMAGING_LOGGER.info(f'Captured image "{newest_image}", GPS: "{gps}"')
        above_threshold, org_img, new_img = thresholder(newest_image, 50)
        #org_img.show()
        new_img.show()
        if above_threshold:
            IMAGING_LOGGER.info(f'\tImage was above the threshold of 50 °C! ("{newest_image}", GPS: "{gps}")')
            # Send email
            subject = "WARNING: Fire Detected"
            body = f"Possible fire detected by Forest Fire Finder at {gps[2]}\n\n" \
                   f"Google Maps location:\n{gps[3]}\n\n" \
                   f"Geographical coordinates of drone:\n" \
                   f"Latitude: \t {gps[0]}\n" \
                   f"Longitude:\t {gps[1]}\n" \
                   f"Altitude: \t {gps[4]}{gps[5]}"
            send_alert(subject, body, (org_img, "Captured image"), (new_img, "Annotated image"))
