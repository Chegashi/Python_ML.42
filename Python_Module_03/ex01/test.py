import numpy as np
from ImageProcessor import ImageProcessor
imp = ImageProcessor()

arr = imp.load("../42AI.png")
# Loading image of dimensions 200 x 200
print(arr)
imp.display(arr)
