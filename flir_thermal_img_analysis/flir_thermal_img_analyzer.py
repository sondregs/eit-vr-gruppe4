import flirimageextractor
import numpy as np
from PIL import Image


def thresholder(img_path, temp_threshold_celsius=100, threshold_color=(255, 0, 0)):
    """
    :summary :
    Given a valid path to an image with radiometric data, find out if any pixel has a tempereature above a given thresold value.
    Then create a new image where every pixel above the thresold is given the specified threshold color.

    :dependency :
    This script relies heavily on the flirimageextractor library. In order to use that library exiftool must be installed
    and added to path as "exiftool".

    :param img_path: path to the image that shal be thresholded.
    :param temp_threshold_celsius: The temperature (in celsius) that will be the threshold for the image. It is set to 100 celsius by default.
    :param threshold_color: Specifies what RGB color the thresholded areas in the image should have.

    :return above_threshold: boolean if any pixels in the picture where above the threshold value
    :return org_image: a PIL object of the original and unprocessed image
    :return new_image: a PIL object of the new image that has been thresholded.
    """

    # Get the images that will be returned
    org_img = Image.open(img_path)
    new_img = Image.open(img_path)
    new_img_pixels = new_img.load()

    # Extract the thermal data
    flir = flirimageextractor.FlirImageExtractor()
    flir.process_image(img_path, False)
    temperature_array = np.array(flir.thermal_image_np.copy())

    # Check if any pixel is above threshold
    # Every pixel above the thermal threshold will be asgined the threshold color
    above_threshold = False
    for row, col in np.ndindex(temperature_array.shape):
        if temperature_array[row, col] > temp_threshold_celsius:
            new_img_pixels[col, row] = threshold_color
            above_threshold = True

    return above_threshold, org_img, new_img
