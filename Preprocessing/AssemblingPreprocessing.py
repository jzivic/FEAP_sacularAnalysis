import os, shutil
from DirectorySearch import DirectorySearch
from DataExtraction import DataExtraction
from SimulationsData import *
import pandas as pd


# Function to delete existing Dir and make a new one
def MakeDir():
    try:
        shutil.rmtree(analysisDir)
    except:
        FileNotFoundError
    os.mkdir(analysisDir)

# Analysis function
def SacularAnalysis_f():
    directorySearch = DirectorySearch(resultsDir)                                                # all search data
    n = len(DirectorySearch.allNames) - 1

    AllSimData = []                                                                              # data from all simulatons
    AllNames = []

    for i in range(n):
        currentSimulation = DataExtraction(resultsDir, i)                                        # each simulation analysis
        AllSimData.append(currentSimulation.simDataFromAllTS)                                    # collecting every simulations data (all TimeSteps)
        AllNames.append(currentSimulation.simName)

    ContactAllSimData = pd.concat(AllSimData, keys=AllNames, axis = 0).reset_index(level=1)      # create one big DataFrame of all df
    ContactAllSimData = ContactAllSimData.rename(columns={"level_1":"TS"})                       # column with number renamed to TimeStep (as it is)
    ContactAllSimData.set_index([ContactAllSimData.index, "TS"], inplace=True)                   # make indices, 1.(unnamed), 2. TS
    ContactAllSimData.to_pickle(PickleData_basic)                                                # save data to .pickle (as sql)


MakeDir()
SacularAnalysis_f()


