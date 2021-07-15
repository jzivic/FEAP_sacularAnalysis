import pandas as pd
import shutil, os
from scipy.stats import linregress
from matplotlib import pyplot as plt
from Preprocessing.SimulationsData import *





ABData = pd.read_pickle(PickleData_AB)



P = ABData["P"]

L = ABData["L"]
D = ABData["D"]

d0 = ABData["d0"]

d1 = ABData["d1"]
d2 = ABData["d2"]
d3 = ABData["d3"]

d = [d1, d2, d3]

# D_d = D-d0


range_1 = [-3,-2,-1, 0, 1,2,3]
range_2 = [1,2]
range_3 = [1,2,4]


coeffList_all = []
rValuesList_all = []

coeffList_high = []
rValuesList_high = {"r_d0":[], "r_d1":[], "r_d2":[], "r_d3":[]}

# rValuesList_d1 = []
# rValuesList_d2 = []
# rValuesList_d3 = []


for iL in range_1:
    for iD in range_1:
        for id in range_1:

            coeffName_Dict = {"iL": iL, "iD":iD, "id": id}
            coeffName_String = "iL:"+str(iL)+",iD:"+str(iD)+",id:"+str(id)


            parameter = L**iL * D**iD * d0**id
            slope, intercept, rValue, pValue, se = linregress(parameter, P)

            rValuesList_all.append(rValue)
            coeffList_all.append(coeffName_String)

            df_all = pd.DataFrame({ "ime":coeffList_all, "rValue": rValuesList_all})



            if abs(rValue) > 0.85:
                coeffList_high.append(coeffName_String)

                rValuesList_high["r_d0"].append(rValue)

                par_d1 = L**iL * D**iD * d1**id
                slope, intercept, rValue, pValue, se = linregress(par_d1, P)
                rValuesList_high["r_d1"].append(rValue)

                par_d2 = L**iL * D**iD * d2**id
                slope, intercept, rValue, pValue, se = linregress(par_d2, P)
                rValuesList_high["r_d2"].append(rValue)

                par_d3 = L**iL * D**iD * d3**id
                slope, intercept, rValue, pValue, se = linregress(par_d3, P)
                rValuesList_high["r_d3"].append(rValue)







            # df_high = pd.DataFrame({ "ime":coeffList_high, "rValue": rValuesList_high})

            df_high = pd.DataFrame( rValuesList_high, index=coeffList_high)



print(df_high)











