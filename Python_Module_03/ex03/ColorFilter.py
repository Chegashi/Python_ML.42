import numpy as np

class ColorFilter:
    def __init__(self):
        pass

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            new_arr = 255 - array
            # print(array)÷
            # for i in array:
            #     for j in i:
            #         print(i)
            return new_arr
        except:
            return None

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            new_arr = array.copy()
            new_arr[:,:, 0] = 0
            new_arr[:,:, 1] = 0
            return new_arr
        except:
            return None

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            new_arr = array.copy()
            new_arr[:,:, 0] = 0
            new_arr[:,:, 2] = 0
            return new_arr
        except:
            return None

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            new_arr = array.copy()
            new_arr[:,:, 1] = 0
            new_arr[:,:, 2] = 0
            return new_arr
        except:
            return None

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        gray = np.mean(array, axis=-1)
        # Define the number of levels or thresholds
        levels = 4

        # Compute the bin boundaries for each level
        bins = np.linspace(0, 1, levels + 1)

        # Apply the binning to the grayscale image
        indices = np.digitize(gray, bins)

        # Map the indices to colors or shades
        colors = (indices - 1) / (levels - 1)

        # Stack the color channels to get a 3D output image
        output = np.stack([colors] * 3, axis=-1)
        return output

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
            weights: [kwargs] list of 3 floats where the sum equals to 1,
            corresponding to the weights of each RBG channels.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        pass