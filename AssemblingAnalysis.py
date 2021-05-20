from FolderSearch import FolderSearch
from DataExtraction import DataExtraction
from SimulationsData import *




def SacularAnalysis_f():
    extractedData = FolderSearch(resultsFolder)        #svako pozivanje FolderSearch klase puni class varijabel ponovno
    n = len(extractedData.allNames) - 1

    for i in range(n):
        # print(extractedData.allNames[i])
        simulacija = DataExtraction(resultsFolder, i)

        print(simulacija.simName)
        print(simulacija.DataFromAllTimeSteps)


SacularAnalysis_f()





