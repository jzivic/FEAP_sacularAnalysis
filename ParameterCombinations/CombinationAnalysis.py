import pandas as pd
from scipy.stats import linregress
from matplotlib import pyplot as plt
from Preprocessing.SimulationsData import *



# abData = pd.read_pickle(PickleData_AB)
# P = abData["P"]
# L = abData["L"]
# D = abData["D"]
# d0 = abData["d0"]
# d1 = abData["d1"]
# d2 = abData["d2"]
# d3 = abData["d3"]
# dSvi = [d0, d1,d2,d3]
#
#
#
#
# goodParameters = pd.read_pickle(picklesDir+"ParametersCombinations_good.pickle")
#
# # r_d0, rAvg, r_d1, r_d2, r_d3,
# def SortingMethod(method):
#     indSorted = list(goodParameters.sort_values(by=method, ascending=True).index)
#     return indSorted
#
# indSorted = SortingMethod("rAvg")

# for i in range(1):
#
#     ind = indSorted[i]
#     parameter = goodParameters.iloc[ind]
#
#
#     coeffDict = parameter["coeffDict"]
#
#     iL = coeffDict["iL"]
#     jD = coeffDict["jD"]
#     kd = coeffDict["kd"]
#     mD_d = coeffDict["mD_d"]
#     N = coeffDict["N"]
#
#
#     parameter = L ** iL * D ** jD * dSvi[0] ** kd * (N * D ** mD_d - dSvi[0] ** mD_d)
#
#     # slope, intercept, rValue, pValue, se = linregress(parameter, P)
#     # print(rValue)
#
#
#     plt.scatter(parameter, P)
#     plt.show()






class CombinationAnalysis:
    abData = pd.read_pickle(PickleData_AB)
    P = abData["P"]
    L = abData["L"]
    D = abData["D"]
    d0 = abData["d0"]
    d1 = abData["d1"]
    d2 = abData["d2"]
    d3 = abData["d3"]
    dSvi = [d0, d1, d2, d3]

    goodParameters = pd.read_pickle(picklesDir + "ParametersCombinations_good.pickle")

    def __init__(self, sortingKey):
        assert sortingKey in ["rAvg", "r_d0", "r_d1", "r_d2","r_d2"],\
            "sortingKey should be: rAvg, r_d0, r_d1, r_d2, r_d2"

        self.sortingKey = sortingKey


    def SortingMethod(self):
        indSorted = list(goodParameters.sort_values(by=self.sortingKey, ascending=True).index)
        return indSorted




CombinationAnalysis()








