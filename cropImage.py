#!/usr/bin/python

from PIL import Image
import sys

try:
    img = Image.open("to_crop.jpg")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
cropped = img.crop((100, 100, 350, 350))
cropped.save('cropped.jpg')
