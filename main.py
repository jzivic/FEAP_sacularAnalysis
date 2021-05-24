import pandas as pd
# from openpyxl.styles import Font, PatternFill
from Preprocessing.SimulationsData import *

allData = pd.read_pickle(PickleData_all)

print(allData)


# df.loc[df['column_name'] == some_value]




# c = allData.loc[allData["Flag"] == "C"]
ab = allData.loc[allData["Flag"] != "C" ]


print(ab)


