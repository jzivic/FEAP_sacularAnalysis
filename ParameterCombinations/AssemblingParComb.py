import pandas as pd
from scipy.stats import linregress
from matplotlib import pyplot as plt
from Preprocessing.SimulationsData import *






from MakeCombinations import MakeCombinations
MakeCombinations(PickleData_AB)


from CombinationAnalysis import MakeDir_combParam, CombAn
MakeDir_combParam()
CombAn("rAvg", 10)


