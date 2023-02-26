import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from PIL import Image
import numpy as np

class ImageProcessor:
    def __init(self):
        pass

    def load(self, path):
        try:
            img = Image.open(path)
            arr = np.asarray(img)
            shape = arr.shape
            print('Loading image of dimensions {} x {}'.format(shape[0], shape[1]))
            return arr
        except:
            print("Exception: FileNotFoundError -- strerror: No such file or directory")
            return None

    def display(self, arr):
        img = Image.fromarray(arr)
        img.show('new_img.png')
