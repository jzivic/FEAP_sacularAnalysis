import pandas as pd
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

dSvi = [d0, d1, d2, d3]



range_1 = [-3,-2,-1, 0, 1,2,3]
range_2 = [1,2]
range_3 = [1,2,4]


allCoeffs = {"coeffName":[], "r_d0":[], "coeffDict":[]}
goodCoeffs = {"coeffName":[], "r_d0":[], "r_d1":[], "r_d2":[], "r_d3":[], "coeffDict":[]}


for iL in range_1:
    for iD in range_1:
        for id in range_1:

            parameter = L**iL * D**iD * dSvi[0]**id
            slope, intercept, rValue, pValue, se = linregress(parameter, P)

            coeffName = "iL="+str(iL)+" iD="+str(iD)+" id="+str(id)
            coeffName_Dict = {"iL": iL, "iD":iD, "id": id}

            allCoeffs["coeffName"].append(coeffName)
            allCoeffs["r_d0"].append(rValue)
            allCoeffs["coeffDict"].append(coeffName_Dict)

            df_all = pd.DataFrame(allCoeffs)



            if abs(rValue) > 0.85:

                goodCoeffs["coeffName"].append(coeffName)
                goodCoeffs["r_d0"].append(rValue)
                goodCoeffs["coeffDict"].append(coeffName_Dict)



                rSvi = []
                for i in range(1,len(dSvi)):
                    parameterGood = L ** iL * D ** iD * dSvi[i] ** id
                    slope, intercept, rValue, pValue, se = linregress(parameterGood, P)
                    rSvi.append(rValue)


                goodCoeffs["r_d1"].append(rSvi[1-1])
                goodCoeffs["r_d2"].append(rSvi[2-1])
                goodCoeffs["r_d3"].append(rSvi[3-1])

            df_good = pd.DataFrame(goodCoeffs)













print(df_good)
# print(df_all)










