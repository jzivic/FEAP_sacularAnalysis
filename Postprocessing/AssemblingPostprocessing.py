import pandas as pd

from Preprocessing.SimulationsData import *

from DerivedParameters import DerivedParameters_f
from PlotContours import MakeDir_contours, PlotAllContours
from PlotParameters import MakeDir_diagrams, PlotingAllDiagrams



DerivedParameters_f(PickleData_basic)       # calculates derived parameters

MakeDir_contours()
PlotAllContours()

MakeDir_diagrams()


print(4)
