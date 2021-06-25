"""
Calculate all derived from basic parameters
Devide all data by flags to separate pickles

"""

import pandas as pd
import shutil, os
from Preprocessing.SimulationsData import *


def MakeDir_pickles():
    try:
        shutil.rmtree(picklesDir)
    except:
        FileNotFoundError
    os.mkdir(picklesDir)






def DerivedParameters_f(basicPickle):
    allData = pd.read_pickle(basicPickle)
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

        # if allData["D"][i] < flagCondition["D"]:

        if allData["S22"][i] < flagCondition["S22"]["A-B"] and allData["GR"][i] < flagCondition["GR"]["A-B"]:
            flag = "A"
        elif allData["S22"][i] < flagCondition["S22"]["B-C"] and allData["GR"][i] < flagCondition["GR"]["B-C"]:
            flag = "B"

        # elif allData["S22"][i] >= flagCondition["S22"]["B-C"] and allData["GR"][i] >= flagCondition["GR"]["A-B"]:
        #     flag = "C"
        else:
            flag = "C"
        flagVector.append(flag)

    allData["Flag"] = flagVector

    C_Data = allData.loc[allData["Flag"] == "C"]             # Flag C represents surely ruptured AAA
    AB_Data = allData.loc[allData["Flag"] != "C"]            # Flags A,B represents AAA that should not rupture

    allData.to_pickle(PickleData_all)                       # storing data into separate pickles
    AB_Data.to_pickle(PickleData_AB)
    C_Data.to_pickle(PickleData_C)

    shutil.copyfile(basicPickle,  picklesDir+"SacularData_basicCopy.pickle")


# MakeDir_pickles()
# DerivedParameters_f(PickleData_basic)