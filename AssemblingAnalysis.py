from FolderSearch import FolderSearch
from DataExtraction import DataExtraction
from SimulationsData import *

resultsFolder = 3



resultsFolder = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna"







def SacularAnalysis_f():
    search = FolderSearch(resultsFolder)
    n = len(FolderSearch.allNames) - 1

    for i in range(n):
        print(FolderSearch.allNames[i])









SacularAnalysis_f()