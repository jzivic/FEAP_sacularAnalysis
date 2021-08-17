from A_Preprocessing.SimulationsData import *

from PlotContours import MakeDir_contours, PlotAllContours
# MakeDir_contours()
# PlotAllContours()


from PlotParameters_v1 import MakeDir_diagrams, PlotingAllDiagrams_v1
from PlotParameters_v2 import PlotingAllDiagrams_v2
MakeDir_diagrams()

if flagVersion == "v1":
    PlotingAllDiagrams_v1()
elif flagVersion == "v2":
    PlotingAllDiagrams_v2()

from Statics import CalculateStatistic
CalculateStatistic()






