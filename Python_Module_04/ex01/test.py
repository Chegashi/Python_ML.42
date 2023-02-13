from FileLoader import FileLoader
from YoungestFellah import youngestfellah
import os

loader = FileLoader()
data = loader.load(os.environ["CSV_PATH"])

print(youngestfellah(data, 1992))
#print("# output is: \"{'f': 12.0, 'm': 11.0}\"")

# print(youngestfellah(data, 2004))
# print("# output is: \"{'f': 13.0, 'm': 14.0}\"")

# print(youngestfellah(data, 2010))
# print("# output is: \"{'f': 15.0, 'm': 15.0}\"")

# print(youngestfellah(data, 2003))
# print("# output is: \"{'f': nan, 'm': nan}\"")

