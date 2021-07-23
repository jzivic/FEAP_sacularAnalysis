"""
class made for making all possible parameter combinations that contains L, D, d up to +- 3rd power.
for every parameter program calculates r value and sorts them by d0 od dAvg.

"""


import pandas as pd
from scipy.stats import linregress
from A_Preprocessing.SimulationsData import *




class MakeCombinations:
    def __init__(self, inputPickle):

        self.inputData = pd.read_pickle(inputPickle)
        self.SetParamCombos()
        self.Calculate_rValue()


    # Get values from pickles
    def SetParamCombos(self):
        self.coeffs_1 = [-3, -2, -1, 0, 1, 2, 3]         # exponents
        self.coeffs = [1, 2, 4]

        self.allParameters = {"paramName":[], "r_d0":[], "r_d1":[], "r_d2":[], "r_d3":[], "rAvg":[], "paramDict":[]}    # store r values, name and coeffs for every parameter

        self.RPI = self.inputData["RPI"]
        self.L = self.inputData["L"]
        self.D = self.inputData["D"]
        d0 = self.inputData["d0"]
        d1 = self.inputData["d1"]
        d2 = self.inputData["d2"]
        d3 = self.inputData["d3"]
        self.dSvi = [d0, d1, d2, d3]


    # Make parameter combinations, for every calculate rvalue. Store all to pickle
    def Calculate_rValue(self):
        for iL in self.coeffs_1:
            for jD in self.coeffs_1:
                for kd in self.coeffs_1:
                    for lDd in self.coeffs_1:
                        for mD_d in self.coeffs_1:
                            for N in self.coeffs:

                                paramName = "iL=" + str(iL) + " jD=" + str(jD) + " kd=" + str(kd)+ " lDd=" + str(lDd) + " mD_d=" + str(
                                            mD_d) + " N=" + str(N)
                                paramName_Dict = {"iL": iL, "jD": jD, "kd": kd, "lDd": lDd, "mD_d": mD_d, "N": N}

                                self.allParameters["paramName"].append(paramName)
                                self.allParameters["paramDict"].append(paramName_Dict)

                                rAll = []
                                for i in range(len(self.dSvi)):
                                    parameter = self.L ** iL * self.D ** jD * self.dSvi[i] ** kd *\
                                                    (N*self.D**mD_d - self.dSvi[i]**mD_d)**lDd
                                    slope, intercept, rValue, p, se = linregress(parameter, self.RPI)
                                    rValue = abs(rValue)
                                    rAll.append(rValue)

                                self.allParameters["r_d0"].append(rAll[0])
                                self.allParameters["r_d1"].append(rAll[1])
                                self.allParameters["r_d2"].append(rAll[2])
                                self.allParameters["r_d3"].append(rAll[3])

                                rAvg = (sum([i for i in rAll]))/4
                                self.allParameters["rAvg"].append(rAvg)


        df_all = pd.DataFrame(self.allParameters)
        df_all.to_pickle(PickleParamCombinations)

# MakeCombinations(PickleData_AB)




