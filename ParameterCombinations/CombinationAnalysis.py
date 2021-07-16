import pandas as pd
from scipy.stats import linregress
from matplotlib import pyplot as plt
from Preprocessing.SimulationsData import *





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




        self.Iteration(nBestParams)
        self.WriteExcel()





    def Iteration(self, nBestParams):

        for i in range(nBestParams):

            ind = self.indSorted[i]
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
                # fig.savefig(contoursDir + allNames[n] + " " + str(chosenTSContours[nTS])  + '.png', dpi=300)


                # plt.show()




    def WriteExcel(self):
        self.toExcel = CombAn.allParameters.sort_values(by=[self.sortingKey], ascending=False)
        self.toExcel.to_excel(paramXlsx)









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
























