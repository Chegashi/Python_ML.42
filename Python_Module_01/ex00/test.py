from book import Book
from recipe import Recipe

# 01.00.01 
try:
    Recipe("cooki", 0, 10, ["dough", "sugar", "love"], "deliciousness incarnate", "dessert")
    print("\n# 01.00.01 ===> KO")
except:
    print("\n# 01.00.01 ===> OK")

# 01.00.02
try:
    Recipe("cooki", 1.5, 10, ["dough", "sugar", "love"], "deliciousness incarnate", "dessert")
    print("\n# 01.00.02 ===> KO")
except:
    print("\n# 01.00.02 ===> OK")

# 01.00.03
try:
    Recipe("cooki", 1, 10, [], "deliciousness incarnate", "dessert")
    print("\n# 01.00.03 ===> KO")
except:
    print("\n# 01.00.03 ===> OK")

# 01.00.04
try:
    Recipe("cooki", 1, 10, [], "deliciousness incarnate", "dessert")
    print("\n# 01.00.04 ===> KO")
except:
    print("\n# 01.00.04 ===> OK")

# 01.00.05
try:
    b = Book("My seductive recipes")
    print(b.creation_date)
    print("\n# should be the current date and time")
    print(b.last_update)
    print("\n# should be the same as the creation date or None")
    print("\n# 01.00.05 ===> OK")

except:
    print("\n# 01.00.05 ===> KO")

# 01.00.06
try:
    crumble = Recipe("Crumble" , 1, 25, ["apples", "flour", "sugar"], "delicious", "dessert")
    b.add_recipe(crumble)
    print(b.last_update)
    print("\n# 01.00.06 ===> OK")
except:
    print("\n# 01.00.06 ===> KO")

# 01.00.07
try:
    b.get_recipe_by_name("Crumble")
    print("# should print the recipe")
    print("# AND")
    print("# <Recipe object at x>")
    b.get_recipe_by_name("Liver Icecream")
    print("# The recipe does not exist")
    print("# The error must be handled in a justifiable manner")
    print("# such as returning None, [], or printing an error message")
    print("\n# 01.00.07 ===> OK")
except:
    print("\n# 01.00.07 ===> KO")

# 01.00.08
try:
    print(b.get_recipes_by_types("dessert")[0])
    print("# Should print the Crumble recipe")
    b.get_recipes_by_types("asdasd")
    print("# The recipe type does not exist, error must be handled in a justifiable manner")
    print("# such as returning None, [], or printing an error message")
    print("\n# 01.00.08 ===> KO")
except:
    print("\n# 01.00.08 ===> OK")
