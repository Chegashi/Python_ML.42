from FileLoader import FileLoader
from ProportionBySport import proportionBySport
import os

loader = FileLoader()
data = loader.load("../athlete_events.csv")

print("")

print(proportionBySport(data, 2004, 'Tennis', 'F'), end = "\n\n")
# output is "0.02307"

print(proportionBySport(data, 2008, 'Hockey', 'F'), end = "\n\n")
# output is  "0.03284"

print(proportionBySport(data, 1964, 'Biathlon', 'M'), end = "\n\n")
# output is "0.00659"
