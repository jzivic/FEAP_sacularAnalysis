"""
Calculate all derived from basic parameters
Devide all data by flags to separate pickles (2. condition)

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



def DerivedParameters_v2(basicPickle, S22_condition = False):
    allData = pd.read_pickle(basicPickle)
    allData = allData.dropna()                                                       # exclude data where AAA is not formed

    #transforming units
    allData["S"] /= 100                                    # mm2 to cm2
    allData["V"] /= 1000                                   # mm3 to cm3
    allData["d_round"] = allData["r"] * 2


    # easier to write
    S22 = allData["S22"]
    L, H, D = allData["L"], allData["H"], allData["D"],
    d0, d1, d2, d3 = allData["d0"], allData["d1"], allData["d2"], allData["d3"],
    dAll = [d0, d1, d2, d3]

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
        allData[GRPI[nd]] = L**2 * dAll[nd]**(-1) * (4*D**(-1)-dAll[nd]**(-1))**(-1) / 100 # mm2 to cm2

    allData["S_resist"] = 0.82299 - 0.156*(allData["Ddr0"] - 2.46)
    allData["RPI"] = S22 / allData["S_resist"]                                    # probability of rupture

    flagVector = [] # list to store flag data
    for i in range(len(allData["RPI"])):

        if D_condition == False:
            if allData["RPI"][i] < RPI_condition:
                flag = "A"
            else:
                flag = "C"

        elif D_condition == True:
            if allData["D"][i] < flagCondition_2["D"] and allData["RPI"][i] < RPI_condition:
                flag = "A"
            else:
                flag = "C"
        flagVector.append(flag)

    allData["Flag"] = flagVector

    A_Data = allData.loc[allData["Flag"] == "A"]             # Flag A represents surely ruptured AAA
    C_Data = allData.loc[allData["Flag"] == "C"]             # Flag C represents surely ruptured AAA

    allData.to_pickle(PickleData_all)                       # storing data into separate pickles
    A_Data.to_pickle(PickleData_A)
    C_Data.to_pickle(PickleData_C)



# MakeDir_pickles()
# DerivedParameters_v2(PickleData_basic, S22_condition)