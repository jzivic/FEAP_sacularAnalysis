import os
import pandas as pd

from SimulationsData import *




print()

def Proba():

    allData = pd.DataFrame(pd.read_pickle(PickleData))


    # allData.Index.set_names("pero")



    allData.set_index([allData.index, "level_1"], inplace=True)

    # print(allData.index)

    # print(allData.loc["r=12_k1=1.048","10"])







    # print(allData["level_1"])










Proba()



def DerivedParameters_f(ulaz):
    allData = pd.read_pickle(ulaz)


    allData["Ddr"] = allData["D"] / allData["d0"]
    allData["Ddr1"] = allData["D"] / allData["d1"]
    allData["Ddr2"] = allData["D"] / allData["d2"]
    allData["Ddr3"] = allData["D"] / allData["d3"]

    allData["T"] = allData["L"] / allData["H"]



    allData["GRPI"] = allData["L"]**3*(4*allData["D"]**2-allData["d0"]**2)/allData["d0"]**2
    allData["GRPI1"] = allData["L"]**3*(4*allData["D"]**2-allData["d1"]**2)/allData["d1"]**2
    allData["GRPI2"] = allData["L"]**3*(4*allData["D"]**2-allData["d2"]**2)/allData["d2"]**2
    allData["GRPI3"] = allData["L"]**3*(4*allData["D"]**2-allData["d3"]**2)/allData["d3"]**2

    allData["NAL"] = allData["L"]*(4*allData["D"]**2-allData["d0"]**2)/allData["d0"]**2
    allData["NAL"] = allData["L"]*(4*allData["D"]**2-allData["d1"]**2)/allData["d1"]**2
    allData["NAL"] = allData["L"]*(4*allData["D"]**2-allData["d2"]**2)/allData["d2"]**2
    allData["NAL"] = allData["L"]*(4*allData["D"]**2-allData["d3"]**2)/allData["d3"]**2


    # def Flag():



    # print(allData.loc["r=12_k1=1.048"])
    print(allData.loc[10])





    # for i in allData:
    #     print(i)


    # print(allData["novi"])


# DerivedParameters_f(PickleData)