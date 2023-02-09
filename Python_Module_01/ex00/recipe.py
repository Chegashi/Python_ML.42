class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        self.check()

    def check(self):
        if (not isinstance(self.name, str) or not self.name):
            raise TypeError("Only str are allowed in name()")
        if (not isinstance(self.cooking_lvl, int)
                or self.cooking_lvl not in range(1, 5)):
            raise TabError("cooking_lvl(int) : range 1 to 5")
        if (not isinstance(self.cooking_time, int) or self.cooking_time < 0):
            raise TabError("cooking_time(int) : \
                  in minutes (no negative numbers)")
        if (not isinstance(self.ingredients, list)
                or len(self.ingredients) < 1):
            raise TabError("ingredients(list) : list of all ingredients ")
        for ing in self.ingredients:
            if (not isinstance(ing, str)):
                raise TabError("ingredients(list) : list of all ingredients\
                    each represented by a string")
            if (self.recipe_type not in ("starter", "lunch", "dessert")):
                raise TabError("recipe_type(str) : can be “starter”, \
                    “lunch” or “dessert”.")
            if (not isinstance(self.description, str)):
                raise TypeError("description(str) : description of the recipe")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "name : {}".format(self.name)
        txt += '\ncooking_lvl: {}'.format(self.cooking_lvl)
        txt += '\ncooking_time: {} minutes'.format(self.cooking_time)
        txt += '\ningredients(list): {}'\
            .format(' '.join(map(str, self.ingredients)))
        txt += '\ndescription: {}'.format(self.description)
        txt += '\nrecipe_type: {}'.format(self.recipe_type)
        txt += '\nRecipe {} at {}'.format(self.name, self.recipe_type)
        
        return(txt)
