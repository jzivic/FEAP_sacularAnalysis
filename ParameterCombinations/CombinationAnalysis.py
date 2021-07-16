import shutil, os
import pandas as pd
from scipy.stats import linregress
from matplotlib import pyplot as plt
from Preprocessing.SimulationsData import *


def MakeDir_combParam():
    try:
        shutil.rmtree(paramCombDir)
        # shutil.rmtree(paramXlsx)
    except:
        FileNotFoundError
    os.mkdir(paramCombDir)



class CombAn:
    abData = pd.read_pickle(PickleData_AB)
    P = abData["P"]
    L = abData["L"]
    D = abData["D"]
    d0 = abData["d0"]
    d1 = abData["d1"]
    d2 = abData["d2"]
    d3 = abData["d3"]
    dSvi = [d0, d1, d2, d3]

    allParameters = pd.read_pickle(PickleParamCombinations)


    def __init__(self, sortingKey, nBestParams=3):
        assert sortingKey in ["rAvg", "r_d0", "r_d1", "r_d2","r_d3"],\
            "sortingKey should be: rAvg, r_d0, r_d1, r_d2, r_d3"

        self.sortingKey = sortingKey
        self.indSorted = list(CombAn.allParameters.sort_values(by=self.sortingKey, ascending=False).index)



        self.WriteExcel()
        self.ParameterIteration(nBestParams)





    def ParameterIteration(self, nBestParams):

        for nParam in range(nBestParams):

            indParam = self.indSorted[nParam]
            parameter = self.allParameters.iloc[indParam]
            paramDict = parameter["paramDict"]

            iL = paramDict["iL"]
            jD = paramDict["jD"]
            kd = paramDict["kd"]
            mD_d = paramDict["mD_d"]
            N = paramDict["N"]
            self.parName = self.allParameters.iloc[indParam]["paramName"]

            def Parameter(diameter):
                parameter = CombAn.L**iL * CombAn.D**jD * diameter**kd * \
                            (N * CombAn.D**mD_d - diameter**mD_d)
                return parameter



            self.MakeParDir(nParam)

            for i in range(len(CombAn.dSvi)):
                diameter = CombAn.dSvi[i]

                slope, intercept, rValue, pValue, se = linregress(Parameter(diameter), CombAn.P)

                fig = plt.gcf()
                plt.scatter(Parameter(diameter), CombAn.P)

                plt.grid(color='k', linestyle=':', linewidth=0.5)
                plt.pause(0.1)
                plt.draw()
                plt.close()

                plt.title(self.parName + ",   d=" + str(i))     #ZAŠTOime par OVO NE RADI U 0. FOLDERU??
                fig.savefig(self.parDir + "d= "+str(i) +"    " + self.parName)



    def MakeParDir(self, number):
        self.parDir = paramCombDir + (str(number) + "/")
        os.mkdir(self.parDir)



    def WriteExcel(self):
        self.toExcel = CombAn.allParameters.sort_values(by=[self.sortingKey], ascending=False)
        self.toExcel.to_excel(paramXlsx)







MakeDir_combParam()

# CombAn("r_d0")
CombAn("rAvg", 10)





















