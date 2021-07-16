import pandas as pd
from scipy.stats import linregress
from matplotlib import pyplot as plt
# from Preprocessing.SimulationsData import *



ABData = pd.read_pickle("SacularData_AB.pickle")



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
range_4 = [-3,-2,-1, 1,2,3]


allCoeffs = {"coeffName":[], "r_d0":[], "coeffDict":[]}
goodCoeffs = {"coeffName":[], "r_d0":[], "r_d1":[], "r_d2":[], "r_d3":[], "coeffDict":[]}


for iL in range_1:
    for iD in range_1:
        for id in range_1:

            for id2 in range_4:

                for M in range_3:

                    parameter = L**iL * D**iD * dSvi[0]**id * (M*D**id2 - dSvi[0]**id2)

                    coeffName = "iL="+str(iL)+" iD="+str(iD)+" id="+str(id)+" id2="+str(id2)+" M="+str(M)
                    coeffName_Dict = {"iL": iL, "iD":iD, "id": id, "id2":id2, "M":M}



                    slope, intercept, rValue, pValue, se = linregress(parameter, P)
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
                            parameterGood = L ** iL * D ** iD * dSvi[i] ** id * (M*D**id2 - dSvi[0]**id2)
                            slope, intercept, rValue, pValue, se = linregress(parameterGood, P)
                            rSvi.append(rValue)


                        goodCoeffs["r_d1"].append(rSvi[1-1])
                        goodCoeffs["r_d2"].append(rSvi[2-1])
                        goodCoeffs["r_d3"].append(rSvi[3-1])

                    df_good = pd.DataFrame(goodCoeffs)






df_good.to_pickle("DobreKombinacije.pickle")





# print(df_good)
#
# print( "Ukupno postoji kombinacija: ", len(df_all))


"""
import pandas as pd
from scipy.stats import linregress
from matplotlib import pyplot as plt
# from Preprocessing.SimulationsData import *
dobre = pd.read_pickle("DobreKombinacije.pickle")
ABData = pd.read_pickle("SacularData_AB.pickle")
# print(dobre)
# print(dobre.sort_values(by="r_d0"))
m = max(dobre["r_d0"])
a = list(dobre["r_d0"]).index(m)
dobre["rSuma"] =  (abs(dobre["r_d0"])+abs(dobre["r_d1"])+(dobre["r_d2"])+abs(dobre["r_d3"]) ) / 4
print(dobre.sort_values(by="rSuma"))
# print(dobre.sort_values(by="r_d0"))
# print(a)
# print(dobre)
# for rInd, row in dobre.iterrows():
#     print(row)
P = ABData["P"]
L = ABData["L"]
D = ABData["D"]
d0 = ABData["d0"]
d1 = ABData["d1"]
d2 = ABData["d2"]
d3 = ABData["d3"]
# a1 = [iL=0, iD=1 id=0 id2=-1 M=]
# parameter = L ** iL * D ** iD * dSvi[0] ** id * (M * D ** id2 - dSvi[0] ** id2)
d = d2
par = L**1 * D**(-1) * d**0 * (1*D**(2)-d**(2))
slope, intercept, rValue, pValue, se = linregress(par, P)
print(rValue)
plt.scatter(par, P)
plt.show()
"""