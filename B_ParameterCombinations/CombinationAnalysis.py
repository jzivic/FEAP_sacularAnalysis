"""
Class to analyze all parameters and sort them by key.
Write everything to excel table and plot n best parameters (stored in separate direcotries)
"""

import shutil, os
import pandas as pd
from matplotlib import pyplot as plt
from A_Preprocessing.SimulationsData import *



# make Directory to store parameter combinaitons
def MakeDir_combParam():
    try:
        shutil.rmtree(paramCombDir)
    except:
        FileNotFoundError
    os.mkdir(paramCombDir)


class CombinationAnalysis:

    def __init__(self, inputData_raw, sortingKey, nBestParams=3):
        assert sortingKey in ["rAvg", "r_d0", "r_d1", "r_d2","r_d3"],\
            "sortingKey should be: rAvg, r_d0, r_d1, r_d2, r_d3"                # only possible
        self.sortingKey = sortingKey                                           # defined in SimulationsData
        self.SetInputData_f(inputData_raw)
        self.indSorted = list(self.allParameters.sort_values(by=self.sortingKey, ascending=False).index) # sorted parameter indices list by r(d0,avg..)
        self.WriteExcel()
        self.ParameterIteration(nBestParams)


    def SetInputData_f(self, inputData_arg):
        inputData = pd.read_pickle(inputData_arg)
        self.RPI = inputData["RPI"]
        self.L = inputData["L"]
        self.D = inputData["D"]
        d0 = inputData["d0"]
        d1 = inputData["d1"]
        d2 = inputData["d2"]
        d3 = inputData["d3"]
        self.dAll = [d0, d1, d2, d3]
        self.allParameters = pd.read_pickle(PickleParamCombinations)     # get parameter exponents and coefficients


    # Iterates over nBestParams best parameters sorted by sortingKey
    def ParameterIteration(self, nBestParams):      # number of best parameters analyzed
        for nParam in range(nBestParams):
            indParam = self.indSorted[nParam]                                   # parameter index
            parameter = self.allParameters.iloc[indParam]
            paramDict = parameter["paramDict"]                                  # exponents written
            self.parName = parameter["paramName"]

            iL = paramDict["iL"]        # exponents
            jD = paramDict["jD"]
            kd = paramDict["kd"]
            lDd = paramDict["lDd"]
            mD_d = paramDict["mD_d"]
            N = paramDict["N"]

            self.MakeParDir(nParam)

            # iterating diameters d0,d1,d2,d3 and Plot diagram
            for i in range(len(self.dAll)):
                diameter = self.dAll[i]
                parameter = self.L ** iL * self.D ** jD * diameter ** kd * (N * self.D ** mD_d - diameter ** mD_d) ** lDd

                fig = plt.gcf()
                plt.ylabel("RPI [-]")
                plt.xlabel("Parameter "+ str(indParam))                                                 # parameter index
                plt.scatter(parameter, self.RPI)
                paramExp = self.parName + ",   d=" + str(i)
                plt.title(paramExp)
                plt.grid(color='k', linestyle=':', linewidth=0.5)
                plt.pause(0.1)
                plt.draw()
                plt.close()
                fig.savefig(self.parDir + "d= "+str(i) +",    " + self.parName)

    # Make directory for every parameter to store diagrams
    def MakeParDir(self, number):
        self.parDir = paramCombDir + (str(number) + "/")
        os.mkdir(self.parDir)

    # Write xlsx with all parameter combinations
    def WriteExcel(self):
        self.Excel = self.allParameters.sort_values(by=[self.sortingKey], ascending=False)
        self.Excel.to_excel(paramXlsx)


# MakeDir_combParam()
# CombinationAnalysis(PickleData_A, sortingKey, nBestParams)





















