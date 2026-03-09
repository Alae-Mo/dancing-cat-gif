# This project is based on Sonny Li’s tutorial from Codedex.io: Create a GIF with Python
import imageio.v3 as iio
from PIL import Image


# List of images in order to create the dancing effect 
filenames = ["images/image_1.jpg", "images/image_2.jpg", "images/image_3.jpg", "images/image_4.jpg", "images/image_4.jpg",  "images/image_3.jpg", "images/image_2.jpg", "images/image_1.jpg"]
images = []

for filename in filenames:
    # Opening each image
    img = Image.open(filename)

    # Resizing image to (656, 656) so all images have the same shape
    img = img.resize((656, 656))
    images.append(img)

# Saving images as gif
# duration = 0.25s per frame (=fast), loop=0 makes it loop forever
iio.imwrite('dancing_cat.gif', images, duration= 0.25, loop = 0)
