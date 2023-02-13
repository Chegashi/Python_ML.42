from FileLoader import FileLoader

loader = FileLoader()
data = loader.load("../athlete_events.csv")

print("# Output \n Loading dataset of dimensions 32561 x 15")
loader.display(data, -12)
print("____________________")
loader.display(data, 12)
print(loader.display(data, 0))
print(loader.display(data, "lol"))