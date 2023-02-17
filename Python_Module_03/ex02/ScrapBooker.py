import  numpy as np

class ScrapBooker:
	def __init__(self):
		pass

	def crop(self, array, dimensions , position = [0,0]):
		"""
		Crops the image as a rectangle via dim arguments (being the new height
		and width of the image) from the coordinates given by position arguments.
		Args:
		-----
		array: numpy.ndarray
		dim: tuple of 2 integers.
		position: tuple of 2 integers.
		Return:
		-------
		new_arr: the cropped numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		try:
			arr = array[position[0]:position[0]+ dimensions[0],
               position[1]:position[1]+ dimensions[1]]
			return arr
		except:
			return None

	def thin(self, array, n, axis):
		"""
		Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
		Args:
		-----
		array: numpy.ndarray.
		n: non null positive integer lower than the number of row/column of the array
		(depending of axis value).
		axis: positive non null integer.
		Return:
		-------
		new_arr: thined numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		try:
			arr = np.delete(array, np.s_[n-1::3], axis)
			return arr
		except:
			return None

	def juxtapose(self, array, n, axis):
		"""
		Juxtaposes n copies of the image along the specified axis.
		Args:
		-----
		array: numpy.ndarray.
		n: positive non null integer.
		axis: integer of value 0 or 1.
		Return:
		-------
		new_arr: juxtaposed numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""
		try:
			if axis:
				arr = np.tile(array, (1,n))
			else:
				arr = np.tile(array, (n,1))
			return arr
		except:
			return None

	def mosaic(self, array, dimensions):
		"""
		Makes a grid with multiple copies of the array. The dim argument specifies
		the number of repetition along each dimensions.
		Args:
		-----
		array: numpy.ndarray.
		dim: tuple of 2 integers.
		Return:
		-------
		new_arr: mosaic numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""
		try:
			shap = array.shap 
			arr = np.array([array] * dimensions[0] * dimensions[1])
			arr2 = arr.reshape(dimensions[0], dimensions[1], shap[0], shap[1])
			return arr2
		except:
			return None
