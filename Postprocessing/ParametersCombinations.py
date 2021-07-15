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


allCoeffNames = []
rVal_all = []

allCoeffs = {"coeffName":[], "r_d0":[], "coeffDict":[]}


goodCoeffs = {"coeffName":[], "r_d0":[], "r_d1":[], "r_d2":[], "r_d3":[], "coeffDict":[]}





# goodCoeffname = []
# goodCoeff_Dict = []
# rVal_good = { "r_d0":[], "r_d1":[], "r_d2":[], "r_d3":[], "coeffs":[]}





for iL in range_1:
    for iD in range_1:
        for id in range_1:

            # coeffName_Dict = {"iL": iL, "iD":iD, "id": id}
            # coeffName_String = "iL="+str(iL)+" iD="+str(iD)+" id="+str(id)
            # rVal_all.append(rValue)
            # allCoeffNames.append(coeffName_String)
            # df_all = pd.DataFrame({ "ime":allCoeffNames, "rValue": rVal_all})



            parameter = L**iL * D**iD * d0**id
            slope, intercept, rValue, pValue, se = linregress(parameter, P)

            coeffName = "iL="+str(iL)+" iD="+str(iD)+" id="+str(id)
            coeffName_Dict = {"iL": iL, "iD":iD, "id": id}

            allCoeffs["coeffName"].append(coeffName)
            allCoeffs["r_d0"].append(rValue)
            allCoeffs["coeffDict"].append(coeffName_Dict)


            df_all = pd.DataFrame(allCoeffs)



            if abs(rValue) > 0.85:







                # goodCoeffname.append(coeffName_String)
                #
                # rVal_good["coeffs"].append(coeffName_Dict)
                #
                # rVal_good["r_d0"].append(rValue)
                #
                # par_d1 = L**iL * D**iD * d1**id
                # slope, intercept, rValue, pValue, se = linregress(par_d1, P)
                # rVal_good["r_d1"].append(rValue)
                #
                # par_d2 = L**iL * D**iD * d2**id
                # slope, intercept, rValue, pValue, se = linregress(par_d2, P)
                # rVal_good["r_d2"].append(rValue)
                #
                # par_d3 = L**iL * D**iD * d3**id
                # slope, intercept, rValue, pValue, se = linregress(par_d3, P)
                # rVal_good["r_d3"].append(rValue)


            df_high = pd.DataFrame( rVal_good, index=goodCoeffname)



print(df_high)
# print(df_all)










