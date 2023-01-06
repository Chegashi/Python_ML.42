cookbook = {
    'sandwich': (['ham', 'bread', 'cheese', 'tomatoes'], 'lunch', 10),
    'cake': (['flour', 'sugar', 'eggs'], 'dessert', 60),
    'salad': (['avocado', "arugula", 'tomatoes', 'spinach'], 'lunch', 15)
}


def recipes_name():
    for recipe_itr in cookbook:
        if (recipe_itr is not None):
            print("--", recipe_itr)


def print_recipe(recipe):
    print("Recipe for" + " " + recipe + ":")
    print("\tIngredients list: " + str(cookbook[recipe][0]))
    print("\tTo be eaten for " + str(cookbook[recipe][1]) + ".")
    print("\tTakes " + str(cookbook[recipe][2]) + " minutes of cooking.")


def del_recipe(recipe):
    cookbook.pop(recipe)


def add_recipe():
    name_recip = input(">>> Enter a name:")
    __str = " "
    ingredient = []
    print(">>> Enter ingredients:")
    while (__str != ""):
        __str = input()
        ingredient.append(__str)
    name_meal = input("Enter a meal type:")
    prep_time = input(" Enter a preparation time:")
    cookbook[name_recip] = (ingredient, name_meal, prep_time)


def print_header():
    print("List of available option:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")


if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")
    print_header()
    while(1337):
        print("\nPlease select an option:")
        n = input(">>")
        if (not n.isdigit() or int(n) > 5 or int(n) < 1):
            print('Sorry, this option does not exist.')
            print_header()
            continue
        n = int(n)
        if (n == 1):
            add_recipe()
        elif (n == 2):
            name_recip = input("recipe: ")
            if name_recip in cookbook:
                del_recipe(name_recip)
            else:
                print(name_recip, ' not found')
        elif (n == 3):
            name_recip = input("recipe: ")
            if name_recip in cookbook:
                print_recipe(name_recip)
            else:
                print(name_recip, ' not found')
        elif (n == 4):
            recipes_name()
        elif (n == 5):
            print("\nCookbook closed. Goodbye !")
            exit()
        else:
            print('This option does not exist, \
                please type the corresponding number. To exit, enter 5.')
