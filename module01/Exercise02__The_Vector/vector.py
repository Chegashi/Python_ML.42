class Vector():
	def __init__(self, values):
		self.values = values
		self.size = len(self.values)
	def __str__(self):
		return ("(Vector {})".format(self.values))

	def __add__(self, a):
		i = 0
		if (isinstance(a, int) or isinstance(a, float)):
			li = self.values[:]
			while i < self.size:
				li[i] += a
				i += 1
			new_vect = Vector(li)
			return new_vect
		elif isinstance(a, list) and len(a) == self.size:
				i = -1
				while i < self.size:
					a[i] += self.values[i]
					i += 1
				new_vect = Vector(a)
				return new_vect
		else:
			raise TabError("ERROR only integrers and list with identic lenght")

	def	__mul__(self, a):
		i = 0
		if (isinstance(a, int) or isinstance(a, float)):
			li = self.values[:]
			while i < self.size:
				li[i] *= a
				i += 1
			new_vect = Vector(li)
			return new_vect
		elif isinstance(a, list) and len(a) == self.size:
				i = 0
				mul = 0
				while i < self.size:
					mul += a[i] * self.values[i]
					i += 1
				return mul
		else:
			raise TabError("ERROR only integrers and list with identic lenght")

v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = v1 * [0.0, 1.0, 2.0, 3.0]
print(v1)
print(v2)

