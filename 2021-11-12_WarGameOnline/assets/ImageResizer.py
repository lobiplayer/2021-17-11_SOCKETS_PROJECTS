
# https://www.geeksforgeeks.org/python-pil-image-resize-method/

# Importing Image class from PIL module
from PIL import Image


# Opens a image in RGB mode
im = Image.open(r"test.bmp")

# # Size of the image in pixels (size of original image)
# # (This is not mandatory)
width, height = im.size
print(width, height)

# # Setting the points for cropped image
# left = 4
# top = height / 5
# right = 154
# bottom = 3 * height / 5

# Cropped image of above dimension
# (It will not change original image)
# im1 = im.crop((left, top, right, bottom))
newsize = (int(round(width / 5)), (int(round(height / 5))))
im1 = im.resize(newsize)
# Shows the image in image viewer
im1.save('test1.bmp')
