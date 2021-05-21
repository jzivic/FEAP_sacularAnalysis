import os
import pandas as pd

from SimulationsData import *



def DerivedParameters_f(ulaz):
    allData = pd.read_pickle(ulaz)
    allData = allData.dropna()


    # allData["Ddr"] = allData["D"] / allData["d0"]
    # allData["Ddr1"] = allData["D"] / allData["d1"]
    # allData["Ddr2"] = allData["D"] / allData["d2"]
    # allData["Ddr3"] = allData["D"] / allData["d3"]
    #
    # allData["T"] = allData["L"] / allData["H"]
    #
    # allData["GRPI"] = allData["L"]**3*(4*allData["D"]**2-allData["d0"]**2)/allData["d0"]**2
    # allData["GRPI1"] = allData["L"]**3*(4*allData["D"]**2-allData["d1"]**2)/allData["d1"]**2
    # allData["GRPI2"] = allData["L"]**3*(4*allData["D"]**2-allData["d2"]**2)/allData["d2"]**2
    # allData["GRPI3"] = allData["L"]**3*(4*allData["D"]**2-allData["d3"]**2)/allData["d3"]**2
    #
    # allData["NAL"] = allData["L"]*(4*allData["D"]**2-allData["d0"]**2)/allData["d0"]**2
    # allData["NAL"] = allData["L"]*(4*allData["D"]**2-allData["d1"]**2)/allData["d1"]**2
    # allData["NAL"] = allData["L"]*(4*allData["D"]**2-allData["d2"]**2)/allData["d2"]**2
    # allData["NAL"] = allData["L"]*(4*allData["D"]**2-allData["d3"]**2)/allData["d3"]**2




    # def Flag(S22, GR):
    #     if S22 < flagCondition["S22"][0] and GR < flagCondition["GR"][0]:
    #         allData["Flag"] = "A"
    #     elif flagCondition["S22"][0] <= S22 < flagCondition["S22"][1] and GR < flagCondition["GR"][1]:
    #         allData["Flag"] = "B"
    #     elif S22 >= flagCondition["S22"][1] and GR >= flagCondition["GR"][0]:
    #         allData["Flag"] = "C"
    #
    #     print(allData["Flag"])

    v = []
    S22 = allData["S22"]
    GR = allData["GR"]

    for i in range(len(S22)):

        if S22[i] < flagCondition["S22"][0] and GR[i] < flagCondition["GR"][0]:
            flag = "A"
        elif S22[i] < flagCondition["S22"][1] and GR[i] < flagCondition["GR"][1]:
            flag = "B"
        elif S22[i] >= flagCondition["S22"][1] and GR[i] >= flagCondition["GR"][0]:
            flag = "C"

        else:
            flag = "NE ZNAM"
        v.append(flag)


    allData["Flag"] = v

    print(allData["Flag"])






DerivedParameters_f(PickleData)