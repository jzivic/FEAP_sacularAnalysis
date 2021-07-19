import pandas as pd


from Preprocessing.SimulationsData import *

from DerivedParameters import DerivedParameters_f, MakeDir_pickles
MakeDir_pickles()
DerivedParameters_f(PickleData_basic)


from PlotContours import MakeDir_contours, PlotAllContours
# MakeDir_contours()
# PlotAllContours()


from PlotParameters import MakeDir_diagrams, PlotingAllDiagrams
MakeDir_diagrams()
PlotingAllDiagrams()



# from Statics import CalculateStatistic
# CalculateStatistic()






