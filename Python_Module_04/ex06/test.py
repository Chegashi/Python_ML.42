from MyPlotLib import MyPlotLib
import pandas as pd
from MyPlotLib import MyPlotLib
from FileLoader import FileLoader


loader = FileLoader()
data = loader.load("../athlete_events.csv")

m = MyPlotLib()
m.histogram(data)