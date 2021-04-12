import  numpy as np

class ScrapBooker:
	def __init__(self):
		pass

	def crop(self, array, dimensions , position = [0,0]):
		new_arr = [[0] * dimensions[0]] * dimensions[1]
		for i in range(position[0], dimensions[0]):
			new_arr[i] = array[position[0]:dimensions[1]]
		return new_arr [[0] * dimensions[0]] * dimensions[1]

	def thin(self, array, n, axis):
		new_arr = np.array(array)
		new_arr = new_arr.delete(array[n])
		new_arr = np.delete(array, 1, axis = 1)
		return new_arr

	def juxtapose(self, array, n, axis):
		if axis:
			return array[n]
		return array[:,n]

	def mosaic(self, array, dimensions):
		pass
