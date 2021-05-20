from FolderSearch import FolderSearch
from DataExtraction import DataExtraction
from SimulationsData import *



# resultsFolder = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna"



def SacularAnalysis_f():
    search = FolderSearch(resultsFolder)
    n = len(FolderSearch.allNames) - 1


    for i in range(n):
        # print(FolderSearch.allNames[i])
        simulacija_TS = DataExtraction(resultsFolder, i)


        # print(simulacija_TS.simName)






SacularAnalysis_f()