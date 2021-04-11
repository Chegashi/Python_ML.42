class ScrapBooker:
	def __init():
		pass

	def crop(self, array, dimensions , position = [0,0]):
		new_arr = [[0] * dimensions[0]] * dimensions[1]
		for i in range(position[0], dimensions[0]):
			new_arr[i] = array[position[0]:dimensions[1]]
		return new_arr [[0] * dimensions[0]] * dimensions[1]

	def thin(self, array, n, axis):
		new_arr = np.array(array)
		new_arr = new_arr.delete(array[n])
		for i
	def juxtapose(self, array, n, axis):
		pass
	
	def mosaic(self, array, dimensions):
		pass