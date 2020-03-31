import flirimageextractor
import numpy as np
from PIL import Image

# User defined variables
threshold = 25                  # Celsius
threshold_color = (255, 0, 0)   # RGB value
img_path = "./sample_data/flir_vue_pro_r_images/Images/sample_image.jpg"  # Relative or absolute path to the image

# Get the images that will be sent to the end user
org_img = Image.open(img_path)
new_img = Image.open(img_path)
new_img_pixels = new_img.load()

# Extract the thermal data
flir = flirimageextractor.FlirImageExtractor()
flir.process_image(img_path, False)
temperatures = np.array(flir.thermal_image_np.copy())

# Check if any pixel is above threshold
# Every pixel above the thermal threshold will be asgined the threshold color
above_threshold = False
for row, col in np.ndindex(temperatures.shape):
    if temperatures[row, col] > threshold:
        new_img_pixels[col, row] = threshold_color
        above_threshold = True

if above_threshold:
    # Do something here 
    # Return the pil objects
    org_img.show()
    new_img.show()
