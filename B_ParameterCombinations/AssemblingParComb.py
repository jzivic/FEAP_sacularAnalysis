import pandas as pd
from scipy.stats import linregress
from matplotlib import pyplot as plt
from A_Preprocessing.SimulationsData import *


# from DerivedParameters import DerivedParameters_f, MakeDir_pickles
# MakeDir_pickles()
# DerivedParameters_f(PickleData_basic)


# from MakeCombinations import MakeCombinations
# MakeCombinations(PickleData_AB)


from CombinationAnalysis import MakeDir_combParam, CombinationAnalysis
MakeDir_combParam()
CombinationAnalysis(sortingKey, nBestParams)




