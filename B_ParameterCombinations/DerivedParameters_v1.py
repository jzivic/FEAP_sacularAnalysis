"""
Calculate all derived from basic parameters
Devide all data by flags to separate pickles (1. condition)

"""

import pandas as pd
import shutil, os
from A_Preprocessing.SimulationsData import *


def MakeDir_pickles():
    try:
        shutil.rmtree(picklesDir)
    except:
        FileNotFoundError
    os.mkdir(picklesDir)



def DerivedParameters_v1(basicPickle, S22_condition = False):
    allData = pd.read_pickle(basicPickle)
    allData = allData.dropna()                                                       # exclude data where AAA is not formed

    #transforming units
    allData["S22"] *= 1000                                 # Pa to kPa
    allData["S"] /= 100                                    # mm2 to cm2
    allData["V"] /= 1000                                   # mm3 to cm3
    allData["d_round"] = allData["r"] * 2


    # easier to write
    S22 = allData["S22"]
    L, H, D = allData["L"], allData["H"], allData["D"],
    d0, d1, d2, d3 = allData["d0"], allData["d1"], allData["d2"], allData["d3"],
    dAll = [d0, d1, d2, d3]


    allData["RPI"] = S22 / sigmaCritical                                    # probability of rupture

    allData["T"] = L / H
    allData["HNeck"] = 160 - H
    allData["Hb"] = H + allData["HNeck"]/2
    allData["Hr"] = allData["HNeck"] / (allData["HNeck"]+ H)
    allData["HDr"] = allData["H"] / d0

    # to avoid multiple lines
    NAL = ["NAL0", "NAL1", "NAL2", "NAL3"]
    GRPI = ["GRPI0", "GRPI1", "GRPI2", "GRPI3"]
    Ddr = ["Ddr0", "Ddr1", "Ddr2", "Ddr3"]
    for nd in range(len(dAll)):
        allData[Ddr[nd]] = D * dAll[nd]**(-1)
        allData[NAL[nd]] = L * D * dAll[nd]**(-1)
        allData[GRPI[nd]] = L * D**2 * dAll[nd]**(-1) * (4*D-dAll[nd])**(-1)

    flagVector = [] # list to store flag data

    # iterate over all data, divide into A,B,C flags
    # Flag C represents surely ruptured AAA
    # Flags A,B represents AAA that should not rupture
    for i in range(len(allData["S22"])):
        if S22_condition == True:
            if allData["S22"][i] < flagCondition_1["S22"]["A-B"] and allData["GR"][i] < flagCondition_1["GR"]["A-B"] and allData["D"][i] < flagCondition_1["D"]:
                flag = "A"
            elif allData["S22"][i] < flagCondition_1["S22"]["B-C"] and allData["GR"][i] < flagCondition_1["GR"]["B-C"] and allData["D"][i] < flagCondition_1["D"]:
                flag = "B"
            else:
                flag = "C"

        elif S22_condition == False:
            if allData["D"][i] < flagCondition_1["D"] and allData["GR"][i] < flagCondition_1["GR"]["A-B"]:
                flag = "A"
            elif allData["D"][i] < flagCondition_1["D"] and allData["GR"][i] < flagCondition_1["GR"]["B-C"]:
                flag = "B"
            else:
                flag = "C"
        flagVector.append(flag)

    allData["Flag"] = flagVector

    C_Data = allData.loc[allData["Flag"] == "C"]             # Flag C represents surely ruptured AAA
    AB_Data = allData.loc[allData["Flag"] != "C"]            # Flags A,B represents AAA that should not rupture

    allData.to_pickle(PickleData_all)                       # storing data into separate pickles
    AB_Data.to_pickle(PickleData_AB)
    C_Data.to_pickle(PickleData_C)


# MakeDir_pickles()
# DerivedParameters_v1(PickleData_basic, S22_condition)


