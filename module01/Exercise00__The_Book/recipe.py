class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ''):
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def check(self):
		if (not isinstance(self.name, str)):
			raise TypeError("Only str are allowed in name()")
		if (not isinstance(self.cooking_lvl, int) and self.cooking_lvl in range(1, 5)):
			raise TabError("cooking_lvl(int) : range 1 to 5")
		if (not isinstance(self.cooking_time, int) and  self.cooking_time < 0):
			raise TabError("cooking_time(int) : in minutes (no negative numbers)")
		if (not isinstance(self.ingredients, list)):
			raise TabError("ingredients(list) : list of all ingredients ")
		for ing in self.ingredients:
			if (not isinstance(ing, str)):
				raise TabError("ingredients(list) : list of all ingredients each represented by a string")
		if (self.recipe_type not in ("starter", "lunch", "dessert")):
			raise TabError("recipe_type(str) : can be “starter”, “lunch” or “dessert”.")
		if (not isinstance(self.description, str)):
			raise TypeError("description(str) : description of the recipe")
	
	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = ""
		txt += "name : " + self.name 
		txt += '\ncooking_lvl: ' + str(self.cooking_lvl )
		txt += '\ncooking_time: ' + str(self.cooking_time)
		txt += '\ningredients(list)' +  ' '.join(map(str, self.ingredients))
		txt += '\ndescription' + str(self.description)
		txt += '\nrecipe_type' + str(self.recipe_type)
		return(txt)