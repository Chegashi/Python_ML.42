import datetime


class Book:
    def __init__(self, name):
        self.name = name
        date = datetime.datetime.now()
        self.last_update = date
        self.creation_date = date
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def check(self):
        if (not isinstance(self.name, str)):
            raise TypeError("Only str are allowed in name()")
        if (not isinstance(self.last_update, datetime)):
            raise TabError("last_update(datetime)")
        if (not isinstance(self.creation_date, datetime)):
            raise TabError("creation_date(datetime)")
        if (not isinstance(self.recipes_list, dict)):
            raise TabError("recipes_list(dict) : a dictionnary")
        for recipe in self.recipes_list:
            if (recipe not in self.recipes_list.keys()):
                raise TabError("recipes_list(dict) : a dictionnary why 3 \
                    keys: “starter”, “lunch”, “dessert”.")

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for typr_rec in self.recipes_list:
            for recipe in self.recipes_list[typr_rec]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print("{} doesn't found".format(name))
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in self.recipes_list.keys():
            raise TabError("invalid recipe_type")
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, type(recipe)):
            raise TabError("invalid recipe")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()
