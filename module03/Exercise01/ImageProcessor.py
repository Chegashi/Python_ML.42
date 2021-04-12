import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from PIL import Image
import numpy as np

class ImageProcessor:
    def __init(self):
        pass

    def load(self, path):
        img = Image.open(path)
        arr = np.array(img)
        print('Loading image of dimensions ', len(arr), ' x ', len(arr[0]))
        return arr

    def display(self, arr):
        img = Image.fromarray(arr, mode = 'P')
        img.save('new_img.png')


imp = ImageProcessor()
arr = imp.load("../resourses/1337_bg.jpeg")
