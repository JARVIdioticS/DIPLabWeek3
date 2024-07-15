# from PIL import Image
# import numpy as np

# img = Image.open("images.mandril.bmp")

# data = np.array(img)

# width = data.shape(0)
# height = data.shape(1)

# mode_to_bpp = {"1":1,"L":8,"P":8,"RGB":24,"RGBA":32,"CMYK":32,"YCbCr":24,"LAB":24,"HSV":24,"I":32,"F":32}
# bitDepth = mode_to_bpp[img.mode]

# print("Image %s with %s x %s pixels (%s bits per pixels) has been read!" % (img.file-name, width, height, bitDepth))

# fo = "images/out.bmp"

# try:
#     img.save(fo)
# except: 
#     print("Write file error")
# else:
#     print("Image %s has been written!" % (fo))
    
from ImageManager import ImageManager

im = ImageManager()

im.read("images/mandril.bmp")

# Quest 001
# im.write("images/copy.bmp")

# Quest 002
# im.convertToGreen()
# im.write("images/green.bmp")
# im.restoreToOriginal()
# im.convertToBlue()
# im.write("images/blue.bmp")
# im.restoreToOriginal()

# Quest 003
# im.convertToGray()
# im.write("images/gray.bmp")

# Quest 004
# im.powerLaw(1, 2.2)
# im.write("images/power2dot2.bmp")
# im.restoreToOriginal()
# im.powerLaw(1, 0.4)
# im.write("images/power0dot4.bmp")
# im.restoreToOriginal()

# Quest 005
# im.adjustContrast(100)
# im.write("images/adjustContrast100.bmp")
# im.restoreToOriginal()
# im.adjustContrast(-100)
# im.write("images/adjustContrast-100.bmp")