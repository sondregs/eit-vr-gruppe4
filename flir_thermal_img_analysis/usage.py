from flir_thermal_img_analyzer import thresholder
from PIL import Image

img_path = "./sample_data/flir_vue_pro_r_images/Images/sample_image.jpg" # Relative or absolute path
threshold_value = 25            # The temperature limit (in celsius) that is used for thresholding the thermal image 
threshold_color = (255, 0, 0)   # The new RGB value that will replace the pixels that are above the the temperature limit 

# If there are any pixels above the temperature limit, "above_threshold" will be true, if not it will be false
# "original_image" is the unprocessed image found at the image path.
# "thresholded_image" is the orignal image BUT all the pixels that has a temperature above the temperature 
#  limit is colored with the given color. If no pixels is above the limit, "original_image" will be equal to "thresholded_image"
above_threshold, original_image, thresholded_image = thresholder(img_path, threshold_value, threshold_color)

if above_threshold:
    # do something ?
    pass

else:
    # do nothing else ?
    pass

# The images are PIL objects
original_image.show()
thresholded_image.show()