import os, shutil
from FolderSearch import FolderSearch
from DataExtraction import DataExtraction
from SimulationsData import *
import pandas as pd



def MakeFolder():
    try:
        shutil.rmtree(analysisFolder)
    except:
        FileNotFoundError
    os.mkdir(analysisFolder)


def SacularAnalysis_f():
    extractedData = FolderSearch(resultsFolder)        #svako pozivanje FolderSearch klase puni class varijabel ponovno
    n = len(extractedData.allNames) - 1

    AllSimData = []
    AllNames = []

    for i in range(n):
        currentSimulation = DataExtraction(resultsFolder, i)
        AllSimData.append(currentSimulation.simDataFromAllTS)
        AllNames.append(currentSimulation.simName)


    ContactAllSimData = pd.concat(AllSimData, keys=AllNames, axis = 0).reset_index(level=1) #create one big dataFrame of all df
    ContactAllSimData = ContactAllSimData.rename(columns={"level_1":"TS"})                  #column renamed to TS
    ContactAllSimData.set_index([ContactAllSimData.index, "TS"], inplace=True)              # make indices, 1.(unnamed), 2. TS
    ContactAllSimData.to_pickle(analysisFolder+"SacularData_basic.pickle")                  # save data to .pickle



MakeFolder()
SacularAnalysis_f()

# nova = pd.concat(l, keys=imena, axis=0).reset_index(level=1)

