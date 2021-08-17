"""
Class to analyze all parameters and sort them by key.
Write everything to excel table and plot several best parameters (stored in separate direcotries)
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
    if flagVersion == "v1":
        inputData = pd.read_pickle(PickleData_AB)                  # entry simulations data
    elif flagVersion == "v2":
        inputData = pd.read_pickle(PickleData_A)

    RPI = inputData["RPI"]
    L = inputData["L"]
    D = inputData["D"]
    d0 = inputData["d0"]
    d1 = inputData["d1"]
    d2 = inputData["d2"]
    d3 = inputData["d3"]
    dSvi = [d0, d1, d2, d3]
    allParameters = pd.read_pickle(PickleParamCombinations)     # get parameter exponents and coefficients

    def __init__(self, sortingKey, nBestParams=3):
        assert sortingKey in ["rAvg", "r_d0", "r_d1", "r_d2","r_d3"],\
            "sortingKey should be: rAvg, r_d0, r_d1, r_d2, r_d3"                # only possible
        self.sortingKey = sortingKey                                           # defined in SimulationsData
        self.indSorted = list(CombinationAnalysis.allParameters.sort_values(by=self.sortingKey, ascending=False).index) # sorted parameter indices list by r(d0,avg..)
        self.WriteExcel()
        self.ParameterIteration(nBestParams)


    def ParameterIteration(self, nBestParams):      # number of best parameters analyzed
        # iterates over nBestParams best parameters sorted by sortingKey
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

            #function just to write parameter shorteer
            def Parameter(diameter):
                parameter = CombinationAnalysis.L**iL * CombinationAnalysis.D**jD * diameter**kd * \
                            (N * CombinationAnalysis.D**mD_d - diameter**mD_d)**lDd
                return parameter
            self.MakeParDir(nParam)

            # iterating diameters d0,d1,d2,d3 and Plot diagram
            for i in range(len(CombinationAnalysis.dSvi)):
                diameter = CombinationAnalysis.dSvi[i]

                fig = plt.gcf()
                plt.ylabel("RPI [-]")
                plt.xlabel("Parameter "+ str(indParam))                                                 # parameter index
                plt.scatter(Parameter(diameter), CombinationAnalysis.RPI)
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
        self.Excel = CombinationAnalysis.allParameters.sort_values(by=[self.sortingKey], ascending=False)
        self.Excel.to_excel(paramXlsx)


MakeDir_combParam()
CombinationAnalysis(sortingKey, nBestParams)





















