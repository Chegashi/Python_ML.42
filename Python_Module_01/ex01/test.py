from game import Stark, GotCharacter

luigi = GotCharacter("Name", True)
print(luigi.__dict__)
arya = Stark("Arya")
print(arya.__doc__)
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)