import shutil, os
import pandas as pd
from scipy.stats import linregress
from matplotlib import pyplot as plt
from Preprocessing.SimulationsData import *


def MakeDir_diagrams():
    try:
        shutil.rmtree(paramCombDir)
        shutil.rmtree(paramXlsx)
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

        for indParam in range(nBestParams):

            ind = self.indSorted[indParam]
            parameter = self.allParameters.iloc[ind]
            paramDict = parameter["paramDict"]

            iL = paramDict["iL"]
            jD = paramDict["jD"]
            kd = paramDict["kd"]
            mD_d = paramDict["mD_d"]
            N = paramDict["N"]
            parName = self.allParameters.iloc[ind]["paramName"]
            def Parameter(diameter):
                parameter = CombAn.L**iL * CombAn.D**jD * diameter**kd * \
                            (N * CombAn.D**mD_d - diameter**mD_d)
                return parameter



            self.MakeParDir(indParam)

            for i in range(len(CombAn.dSvi)):
                diameter = CombAn.dSvi[i]
                parameter = Parameter(diameter)

                slope, intercept, rValue, pValue, se = linregress(parameter, CombAn.P)

                fig = plt.gcf()
                plt.scatter(parameter, CombAn.P)

                plt.grid(color='k', linestyle=':', linewidth=0.5)
                plt.pause(0.1)
                plt.draw()
                plt.close()

                plt.title(parName + ",   d=" + str(i))
                fig.savefig(self.parDir + "d= "+str(i) +"    " + parName)



    def MakeParDir(self, number):
        self.parDir = paramCombDir + (str(number) + "/")
        os.mkdir(self.parDir)



    def WriteExcel(self):
        self.toExcel = CombAn.allParameters.sort_values(by=[self.sortingKey], ascending=False)
        self.toExcel.to_excel(paramXlsx)







MakeDir_diagrams()

# CombAn("r_d0")
CombAn("rAvg", 10)






# allParameters = pd.read_pickle(picklesDir + "ParametersCombinations_good.pickle")
#
# r0 = allParameters["rAvg"]
# r1 = allParameters["r_d1"]
# r2 = allParameters["r_d2"]
# r3 = allParameters["r_d3"]
#
# b =0
# for i in range(len(r0)):
#
#     pred = lambda x: "p" if x >=0 else "m"
#
#
#
#     if pred(r0[i]) == pred(r1[i]) == pred(r2[i]) == pred(r3[i]):
#         pass
#     else:
#         b+=1
#         # print("nema")
#
#
# print(b, len(r0))
























