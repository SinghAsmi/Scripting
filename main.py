# SCRIPTING IN PYTHON

from PIL import Image, ImageFilter
import sys
import os

# OPENING IMAGE
# img = Image.open('./pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.convert('L')

# ROTATING
# crooked = filtered_img.rotate(90)
# crooked.save('grey.png', 'png')

# RESIZING
# resize = filtered_img.resize((300, 300))
# resize.save('grey.png', 'png')

# CROPPING IMAGE
# box = (100, 100, 200, 200)
# region = filtered_img.crop(box)
# region.save('grey.png', 'png')
# filtered_img.show()

# How to make a big picture smaller with astro.jpg
# img = Image.open('./astro.jpg')
# img.thumbnail((400, 400))
# img.save('Thumbnail.jpg')

# JPEG TO PNG CONVERTER

image_folder = sys.argv[1]
output_folder = sys.argv[2]

