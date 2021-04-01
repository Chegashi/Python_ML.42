cookbook = {
			'sandwich': (['ham', 'bread', 'cheese', 'tomatoes'], 'lunch' ,10), 
			'cake': (['flour', 'sugar', 'eggs'], 'dessert', 60),
			'salad': (['avocado', "arugula", 'tomatoes', 'spinach'], 'lunch', 15)}

def		print_recipe(recipe):
	print(cookbook[recipe])

def		del_recipe(recipe):
	cookbook.pop(recipe)

def		add_recipe(name_recipe, ingredients, meal, prep_time):
	cookbook[name_recipe] = (ingredients, meal, prep_time)

def		print_all():
	for recipe in cookbook:
		print(recipe,'ingredients are ', end="")
		for ingredient in cookbook[recipe][0]:
			print(ingredient, end=', ')
		print(' It is ', cookbook[recipe][1], 'and it takes ', cookbook[recipe][2], 'minutes of preparation')

print("Please select an option by typing the corresponding number:")
print("1: Add a recipe")
print("2: Delete a recipe")
print("3: Print a recipe")
print("4: Print the cookbook")
print("5: Quit")
n = input(">>")
n = int(n)
while (n != 5):
	if (n == 1):
		name_recip = input("recipe: ")
		name_ingre = input("a list of ingredients: ")
		name_meal = input("type of meal: ")
		prep_time = input("preparation time in minutes: ")
		grad = name_ingre.split(" ")
		add_recipe(name_recip, grad, name_meal, prep_time)
	if (n == 2):
		name_recip = input("recipe: ")
		if name_recip in cookbook:
			del_recipe(name_recip)
		else
			print(name_recip, ' not found')
	if (n == 3):
		name_recip = input("recipe: ")
		if name_recip in cookbook:
			print_recipe(name_recip)
		else
			print(name_recip, ' not found')
	if (n == 4):
		print_all()
	if (n == 5):
		break
	else
		print('This option does not exist, please type the corresponding number. To exit, enter 5.')
	n = input(">>")
	n = int(n)

print(n)