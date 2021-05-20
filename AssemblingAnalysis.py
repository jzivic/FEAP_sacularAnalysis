from FolderSearch import FolderSearch
from DataExtraction import DataExtraction
from SimulationsData import *



# resultsFolder = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna"



def SacularAnalysis_f():
    extractedData = FolderSearch(resultsFolder)        #svako pozivanje FolderSearch klase puni class varijabel ponovno
    n = len(extractedData.allNames) - 1

    for i in range(n):
        print(extractedData.allNames[i])
        simulacija_TS = DataExtraction(resultsFolder, i)


SacularAnalysis_f()





