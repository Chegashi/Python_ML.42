class Vector():
	def __init__(self, values):
		self.values = values
		self.size = len(self.values)

	def __str__(self):
		return ("(Vector {})".format(self.values))

	def __add__(self, a):
		i = 0
		if (isinstance(a, int) or isinstance(a, float)):
			li = [a] * self.size
		elif isinstance(a, list):
			li = a[:]
		elif len(a) != self.size:
			return self.__radd__(a)
		else :
			raise TabError("ERROR only integrers and list with identic lenght")
		while i < self.size:
			li[i] += self.values[i]
			i += 1
		new_vect = Vector(li)
		return new_vect

	def __radd__(self, a):
		if len(a) > len(self.values):
			li = self.values
			i = len(self.values)
			max = len(a)
		elif len(a)	< len(self).values:
			li = a[:]
			i = len(a)
			max = len(self.values)
		while i < max:
			li.append(0)
			i += 1
		return self + li

	def __mul__(self, a):
		i = 0
		if (isinstance(a, int) or isinstance(a, float)):
			li = [a] * len(self.values)
		elif isinstance(a, list):
			li = a[:]
		elif len(a) != self.size:
			return self.__rmul__(a)
		else :
			raise TabError("ERROR only integrers and list with identic lenght")
		while i < self.size:
			li[i] *= self.values[i]
			i += 1
		new_vect = Vector(li)
		return new_vect

	def __rmul__(self, a): 
		if len(a) > len(self.values):
			li = self.values
			i = len(self.values)
			max = len(a)
		elif len(a)	< len(self).values:
			li = a
			i = len(a)
			max = len(self.values)
		while i < max:
			li.append(0)
			i += 1
		return self * li

	def __sub__(self, a):
		i = 0
		if (isinstance(a, int) or isinstance(a, float)):
			li = [-1 * a] * len(self.values)
		elif isinstance(a, list):
			li = [1] * len(a)
			for i in range(0, len(a)):
				li[i] = -1 * a[i]
			return self + li
		elif len(a) != self.size:
			return self.__rsub__(a)
		else :
			raise TabError("ERROR only integrers and list with identic lenght")
		
	def __rsub__(self, a):
		if len(a) > len(self.values):
			li = self.values
			i = len(self.values)
			max = len(a)
		elif len(a)	< len(self).values:
			li = a
			i = len(a)
			max = len(self.values)
		while i < max:
			li.append(0)
			i += 1
		return self + li

	def __truediv__(self, a):
		i = 0
		if (isinstance(a, int) or isinstance(a, float)) and a:
			li = [1/a] * len(self.values)
			return self * li
		elif isinstance(a, list):
			li = [1] * len(a)
			for i in range(0, len(a)):
				if a[i] != 0:
					li[i] = 1 / a[i]
				else:
					raise TabError("dvide by sero")
				i += 1
			return self * li
		elif len(a) != self.size:
			return self.__rtruediv__(a)
		else :
			raise TabError("ERROR only integrers and list with identic lenght")

	def __rtruediv__(self, a):
		if len(a) > len(self.values):
			li = self.values
			i = len(self.values)
			max = len(a)
		elif len(a)	< len(self).values:
			li = a
			i = len(a)
			max = len(self.values)
		while i < max:
			li.append(1)
			i += 1
		return self * li

	def __repr__(self):
		return str(self.values)
