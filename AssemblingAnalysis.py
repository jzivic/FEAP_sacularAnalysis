import os, shutil
from FolderSearch import FolderSearch
from DataExtraction import DataExtraction
from SimulationsData import *
import pandas as pd


def MakeFolder(destination):
    try:
        shutil.rmtree(destination)
    except:
        FileNotFoundError
    os.mkdir(destination)


def SacularAnalysis_f():
    extractedData = FolderSearch(resultsFolder)        #svako pozivanje FolderSearch klase puni class varijabel ponovno
    n = len(extractedData.allNames) - 1

    AllSimData = []
    AllNames = []

    for i in range(n):
        currentSimulation = DataExtraction(resultsFolder, i)

        AllSimData.append(currentSimulation.simDataFromAllTS)
        AllNames.append(currentSimulation.simName)


    ContactAllSimData = pd.concat(AllSimData, keys=AllNames, axis = 0).reset_index(level=1)

    ContactAllSimData.to_pickle(analysisFolder+"SacularData1.pickle")



MakeFolder(analysisFolder)
SacularAnalysis_f()

# nova = pd.concat(l, keys=imena, axis=0).reset_index(level=1)

