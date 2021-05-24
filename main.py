import os, math#, xlsxwriter, openpyxl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
# from openpyxl.styles import Font, PatternFill
from SimulationsData import *

import xarray as xr




allData = pd.read_pickle(PickleData_all)

print(allData)


# df.loc[df['column_name'] == some_value]




# c = allData.loc[allData["Flag"] == "C"]
ab = allData.loc[allData["Flag"] != "C" ]


print(ab)


