class Matrix:
	def __init__(self, data):
		self.data = data
		self.shape = (len(data), len(data[0]))

		def __str__(self):
			return ("(Matrix {}".format(self.data))

	def __add__(self, A):
		S = [[0] * self.shape[1]] * self.shape[1]
		if (isinstance(A, int) or isinstance(A, float)):
			S = [[A] * self.shape[1]] * self.shape[0]
		for i in range(0, self.shape[0]) :
			for j in range(0, self.shape[1]) :
				S[i][j] += self.data[i][j]
		return Matrix(S)

	def __mul__(self, A):
		S = [[0] * self.shape[1]] * self.shape[1]
		if (isinstance(A, int) or isinstance(A, float)):
			S = [[A] * self.shape[1]] * self.shape[0]
		for i in range(0, self.shape[0]) :
			for j in range(0, self.shape[1]) :
				S[i][j] = 0
				for k in range(0, self.shape[1]):
					S[i][j] += self.data[i][k] + A[k][j]
		return Matrix(S)

	def __sub__(self, A):
		S = [[0] * self.shape[1]] * self.shape[1]
		if (isinstance(A, int) or isinstance(A, float)):
			S = [[A] * self.shape[1]] * self.shape[0]
		for i in range(0, self.shape[0]) :
			for j in range(0, self.shape[1]) :
				S[i][j] -= self.data[i][j]
		return Matrix(S)
			
			
# v1 = Vector([0.0, 1.0, 2.0, 3.0])