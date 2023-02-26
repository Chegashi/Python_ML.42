import pandas as pd
from FileLoader import FileLoader
from MyPlotLib import MyPlotLib
import os

loader = FileLoader()
data = loader.load("../athlete_events.csv")

sp = MyPlotLib(data)

print(sp.where(2000))
# output is: ['Sydney']

print(sp.where(1980))
# output is: ['Lake Placid', 'Moskva'] If a single of these locations is returned it's ok.

print(sp.when('London'))
# output is: [2012, 1948, 1908]
