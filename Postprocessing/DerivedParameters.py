import pandas as pd

from Preprocessing.SimulationsData import *



def DerivedParameters_f(ulaz):
    allData = pd.read_pickle(ulaz)
    allData = allData.dropna()

    allData["P"] = allData["S22"] / sigmaCritical

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
    allData["NAL1"] = allData["L"]*(4*allData["D"]**2-allData["d1"]**2)/allData["d1"]**2
    allData["NAL2"] = allData["L"]*(4*allData["D"]**2-allData["d2"]**2)/allData["d2"]**2
    allData["NAL3"] = allData["L"]*(4*allData["D"]**2-allData["d3"]**2)/allData["d3"]**2

    allData["HNeck"] = 160 - allData["H"]
    allData["Hb"] = allData["H"] + allData["HNeck"]/2
    allData["Hr"] = allData["HNeck"] / (allData["HNeck"]+allData["H"])
    allData["HDr"] = allData["H"] / allData["d0"]

    flagVector = []
    for i in range(len(allData["S22"])):
        if allData["S22"][i] < flagCondition["S22"][0] and allData["GR"][i] < flagCondition["GR"][0]:
            flag = "A"
        elif allData["S22"][i] < flagCondition["S22"][1] and allData["GR"][i] < flagCondition["GR"][1]:
            flag = "B"
        elif allData["S22"][i] >= flagCondition["S22"][1] and allData["GR"][i] >= flagCondition["GR"][0]:
            flag = "C"
        else:
            flag = "NE ZNAM"
        flagVector.append(flag)
    allData["Flag"] = flagVector

    cData = allData.loc[allData["Flag"] == "C"]
    abData = allData.loc[allData["Flag"] != "C"]


    allData.to_pickle(PickleData_all)
    abData.to_pickle(PickleData_ab)
    cData.to_pickle(PickleData_c)




# DerivedParameters_f(PickleData_basic)