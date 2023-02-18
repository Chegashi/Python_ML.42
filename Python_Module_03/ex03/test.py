from ImageProcessor import ImageProcessor

imp = ImageProcessor()
load = "../mochegri.jpeg"

arr = imp.load(load)

# Output :
# Loading image of dimensions 200 x 200

from ColorFilter import ColorFilter
cf = ColorFilter()

# invert = cf.invert(arr)
# imp.display(invert)

# green = cf.to_green(arr)
# imp.display(green)

# red = cf.to_red(arr)
# imp.display(red)

# blue = cf.to_blue(arr)
# imp.display(blue)

celluloid = cf.to_celluloid(arr)
imp.display(celluloid)