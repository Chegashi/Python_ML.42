import pandas as pd
from HowManyMedals import howManyMedals
from FileLoader import FileLoader
import os

loader = FileLoader()
data = loader.load("../athlete_events.csv")

print(howManyMedals(data, 'Gary Abraham'))
#  the output is: "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}"

print(howManyMedals(data, 'Yekaterina Konstantinovna Abramova'))
#  the output is "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}"

print(howManyMedals(data, 'Kristin Otto'))
#  the output is: "{1988: {'G': 6, 'S': 0, 'B': 0}}"
