import pandas as pd

from Preprocessing.SimulationsData import *

from DerivedParameters import DerivedParameters_f
from PlotContours import MakeDir_contours, PlotAllContours




DerivedParameters_f(PickleData_basic)       # calculates derived parameters

MakeDir_contours()
PlotAllContours()



print(4)
