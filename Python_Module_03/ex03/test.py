from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

imp = ImageProcessor()
load = "../mochegri.jpeg"

arr = imp.load(load)

# Output :
# Loading image of dimensions 200 x 200

cf = ColorFilter()

# invert = cf.invert(arr)
# imp.display(invert)

# green = cf.to_green(arr)
# imp.display(green)

# red = cf.to_red(arr)
# imp.display(red)

# blue = cf.to_blue(arr)
# imp.display(blue)

# celluloid = cf.to_celluloid(arr)
# imp.display(celluloid)

# grayscale = cf.to_grayscale(arr)
# imp.display(grayscale)





for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
	array = plt.imread(load)
	# plt.imshow(f(array))
	# plt.show()

# im = cf.to_grayscale(array, "m")
# plt.imshow(im, cmap="gray")
# plt.show()

im = cf.to_grayscale(array, "w", weights = [0.2126, 0.7152, 0.0722])
plt.imshow(im, cmap="gray")
plt.show()