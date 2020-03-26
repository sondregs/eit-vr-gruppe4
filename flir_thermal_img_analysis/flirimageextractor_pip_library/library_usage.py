""" 
This is a demo for how to use the flirimageextractor library.

The library assumes that exiftool is installed and added to PATH as 'exiftool'. 
The library will not work unless this is done.
Alternatively, you can explicitly specify the exiftool path in the 'exiftool_path' attribute.

The thermal values that are returned by this library might not match the theramal values given by the camera. The reason for this is that the library is not designed for every flir camera. The library uses internal constants to calculate the temperature from the sensor data. If you want to fix this, you will have to enter the source code of this library, find the static method called 'raw2temp' and change the constants to approripate values for your use case.

"""

import flirimageextractor

img_path = "./../sample_data/flir_vue_pro_r_images/Images/sample_image.jpg"

# Initialize the FlirImageExtractor class
flir = flirimageextractor.FlirImageExtractor()

# Extract meta data from the image
meta_data = flir.get_metadata(img_path)
print(meta_data)

# Returns a boolean of whether the image contains thermal data
thermal_exists = flir.check_for_thermal_image(img_path)
print(thermal_exists)

# In general it is not neccessary to load the file. 
# However, the library has not accounted for all edge cases, and some methods might throw an error if the file is not loaded.
# The get_image_type method will sometimes(!) throw an error if the file is not loaded
flir.loadfile(img_path)
img_type = flir.get_image_type()
print(img_type)

# The process image method will process the image and asign appropriate values to all attributes in the class.
# We can specify if we want the class to generate rgb numpy array of the image. This will consume memory and take processing time, so it should be false. Also, right now there seems to be a bug that causes the library to crash when this is set to true
generate_rgb_array = False
flir.process_image(img_path, generate_rgb_array)
# After the image is processed the radiometric data can be accessed through the thermal_image_np attribute. The thermal data is returned as a numpy array. 
thermal_np_array = flir.thermal_image_np
print(thermal_np_array)

# If you want to save the image you will have to set the full path and name for the new image that will be saved
new_img_name = "saved image.jpg"
directory_path = "C:/Users/Utlån/code/eit/eit-vr-gruppe4/flir_thermal_img_analysis/flirimageextractor_pip_library/"
flir.flir_img_filename = directory_path + new_img_name

flir.save_images()

#  if bytesIO is set to true, the method will return a bytes object of the image that we can manually save to disk. It is important to note that when this is true, the method will NOT save the image to disk for us.
test = flir.save_images(bytesIO=True)

# Plots the image that has been processed. Palettes for the plot can be set in the class constructor or through the pallettes attribute of the class. 
flir.plot()
