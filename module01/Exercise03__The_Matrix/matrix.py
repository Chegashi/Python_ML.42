import sys

sys.path.append('/Users/mochegri/Desktop/bootcamp_python.42-IA/module01/Exercise02__The_Vector/vector')
# import Vector

class Matrix:
	def __init__(self, data):
		self.data = data
		self.shape = (len(data), len(data[0]))
	
	def __str__(self):
		return ("(Matrix {}".format(self.data))
	
	# def __add__(self, A):
	# 	S = [[0] * self.shape[1]] * self.shape[1]
	# 	if (isinstance(A, int) or isinstance(A, float)):
	# 		for i in range(0, self.shape[0]):
	# 			for j in range(0, self.shape[1]):
	# 				S[i][j] = self.data[i][j] + 				
v1 = Vector([0.0, 1.0, 2.0, 3.0])