import pandas as pd
from scipy.stats import linregress
from matplotlib import pyplot as plt
from Preprocessing.SimulationsData import *




class MakeCombinations:
    def __init__(self, inputPickle):

        self.inputData = pd.read_pickle(inputPickle)

        self.SetCase()
        self.Calculate_rValue()



    def SetCase(self):
        self.range_1 = [-3, -2, -1, 0, 1, 2, 3]
        self.range_12 = [-3, -2, -1, 1, 2, 3]
        self.range_2 = [1, 2, 4]

        self.allParameters = {"paramName":[], "r_d0":[], "r_d1":[], "r_d2":[], "r_d3":[], "rAvg":[], "paramDict":[]}


        self.P = self.inputData["P"]
        self.L = self.inputData["L"]
        self.D = self.inputData["D"]

        d0 = self.inputData["d0"]
        d1 = self.inputData["d1"]
        d2 = self.inputData["d2"]
        d3 = self.inputData["d3"]

        self.dSvi = [d0, d1, d2, d3]



    def Calculate_rValue(self):

        for iL in self.range_1:
            for jD in self.range_1:
                for kd in self.range_1:
                    # for lDd in range_12:
                    for mD_d in self.range_1:
                        for N in self.range_2:

                            parameter = self.L ** iL * self.D ** jD * self.dSvi[0] ** kd * (N * self.D ** mD_d - self.dSvi[0] ** mD_d)
                            slope, intercept, rValue, pValue, se = linregress(parameter, self.P)

                            paramName = "iL=" + str(iL) + " jD=" + str(jD) + " kd=" + str(kd) + " mD_d=" + str(
                                        mD_d) + " N=" + str(N)
                            paramName_Dict = {"iL": iL, "jD": jD, "kd": kd, "mD_d": mD_d, "N": N}

                            self.allParameters["paramName"].append(paramName)
                            self.allParameters["r_d0"].append(rValue)
                            self.allParameters["paramDict"].append(paramName_Dict)

                            rAll = []
                            for i in range(1, len(self.dSvi)):
                                parameterGood = self.L ** iL * self.D ** jD * self.dSvi[i] ** kd *\
                                                ( N * self.D ** mD_d - self.dSvi[i] ** mD_d)

                                slope, intercept, rValueRest, p, se = linregress(parameterGood, self.P)
                                rAll.append(rValueRest)

                            self.allParameters["r_d1"].append(rAll[1 - 1])
                            self.allParameters["r_d2"].append(rAll[2 - 1])
                            self.allParameters["r_d3"].append(rAll[3 - 1])

                            rA = (sum([abs(i) for i in rAll]) + abs(rValue))/4
                            # rA = (sum([i for i in rAll]) + rValue)/4

                            self.allParameters["rAvg"].append(rA)


        df_all = pd.DataFrame(self.allParameters)
        df_all.to_pickle(PickleParamCombinations)


MakeCombinations(PickleData_AB)




