from book import Book
from recipe import Recipe

msaman = Recipe('msaman', 3, 60, ['dgig', 'zit', 'khmira'], 'dessert')
to_print = str(msaman)
newBook = Book('chhiwat')
newBook.add_recipe(msaman)
newBook.get_recipe_by_name('msaman')
newBook.get_recipes_by_types('dessert')
