from FolderSearch import FolderSearch, PretrazivanjeFolderaSakularna
from DataExtraction import DataExtraction
from SimulationsData import *



# resultsFolder = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna"



def SacularAnalysis_f():
    searchData = FolderSearch(resultsFolder)        #svako pozivanje FolderSearch klase puni class varijabel ponovno
    n = len(searchData.allNames) - 1


    for i in range(n):
        print(searchData.allNames[i])
        simulacija_TS = DataExtraction(resultsFolder, i)

SacularAnalysis_f()





