import os, shutil
from FolderSearch import FolderSearch
from DataExtraction import DataExtraction
from SimulationsData import *
import pandas as pd


# Function to delete existing folder and make a new one
def MakeFolder():
    try:
        shutil.rmtree(analysisFolder)
    except:
        FileNotFoundError
    os.mkdir(analysisFolder)


def SacularAnalysis_f():
    folderSearch = FolderSearch(resultsFolder)                                                   # all search data
    n = len(folderSearch.allNames) - 1

    AllSimData = []                                                                             # data from all simulatons
    AllNames = []

    for i in range(n):
        currentSimulation = DataExtraction(resultsFolder, i)                                     # each simulation analysis
        AllSimData.append(currentSimulation.simDataFromAllTS)
        AllNames.append(currentSimulation.simName)

    ContactAllSimData = pd.concat(AllSimData, keys=AllNames, axis = 0).reset_index(level=1)      #create one big dataFrame of all df
    ContactAllSimData = ContactAllSimData.rename(columns={"level_1":"TS"})                       #column renamed to TS
    ContactAllSimData.set_index([ContactAllSimData.index, "TS"], inplace=True)                   # make indices, 1.(unnamed), 2. TS
    ContactAllSimData.to_pickle(PickleData_basic)                       # save data to .pickle



MakeFolder()
SacularAnalysis_f()

# nova = pd.concat(l, keys=imena, axis=0).reset_index(level=1)
