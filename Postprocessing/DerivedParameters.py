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






def DerivedParameters_f(basicPickle, S22_condition = False):
# def DerivedParameters_f(basicPickle, condition = {"D_Gr":True, S=None}):
    allData = pd.read_pickle(basicPickle)
    allData = allData.dropna()                                                       # exclude data where AAA is not formed

    S22 = allData["S22"]
    L, H, D = allData["L"], allData["H"], allData["D"], 
    d0, d1, d2, d3 = allData["d0"], allData["d1"], allData["d2"], allData["d3"], 
    dAll = [d0, d1, d2, d3]


    allData["RPI"] = S22 / sigmaCritical                                    # probability of rupture
    # allData["P"] = S22 / sigmaCritical                                    # probability of rupture

    allData["T"] = L / H
    allData["HNeck"] = 160 - H
    allData["Hb"] = H + allData["HNeck"]/2
    allData["Hr"] = allData["HNeck"] / (allData["HNeck"]+ H)
    allData["HDr"] = allData["H"] / d0



    NAL = ["NAL0", "NAL1", "NAL2", "NAL3"]
    GRPI = ["GRPI0", "GRPI1", "GRPI2", "GRPI3"]
    Ddr = ["Ddr0", "Ddr1", "Ddr2", "Ddr3"]
    for nd in range(len(dAll)):
        allData[Ddr[nd]] = D * dAll[nd]**(-1)
        allData[NAL[nd]] = L * D * dAll[nd]**(-1)
        allData[GRPI[nd]] = L * D**2 * dAll[nd]**(-1) * (4*D-dAll[nd])**(-1)





    flagVector = []
    # iterate over all data, divide into A,B,C flags
    # Flag C represents surely ruptured AAA
    # Flags A,B represents AAA that should not rupture
    for i in range(len(allData["S22"])):
        if S22_condition == True:
            if allData["S22"][i] < flagCondition["S22"]["A-B"] and allData["GR"][i] < flagCondition["GR"]["A-B"] and allData["D"][i] < flagCondition["D"]:
                flag = "A"
            elif allData["S22"][i] < flagCondition["S22"]["B-C"] and allData["GR"][i] < flagCondition["GR"]["B-C"] and allData["D"][i] < flagCondition["D"]:
                flag = "B"
            else:
                flag = "C"

        elif S22_condition == False:
            if allData["D"][i] < flagCondition["D"] and allData["GR"][i] < flagCondition["GR"]["A-B"]:
                flag = "A"
            elif allData["D"][i] < flagCondition["D"] and allData["GR"][i] < flagCondition["GR"]["B-C"]:
                flag = "B"
            else:
                flag = "C"
        flagVector.append(flag)


    # allData = allData.dropna()                                                       # exclude data where AAA is not formed
    allData["Flag"] = flagVector
    C_Data = allData.loc[allData["Flag"] == "C"]             # Flag C represents surely ruptured AAA
    AB_Data = allData.loc[allData["Flag"] != "C"]            # Flags A,B represents AAA that should not rupture

    allData.to_pickle(PickleData_all)                       # storing data into separate pickles
    AB_Data.to_pickle(PickleData_AB)
    C_Data.to_pickle(PickleData_C)

    shutil.copyfile(basicPickle,  picklesDir+"SacularData_basicCopy.pickle")            # copy and move to pickles dir


MakeDir_pickles()
DerivedParameters_f(PickleData_basic, S22_condition=False)