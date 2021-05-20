from FolderSearch import FolderSearch, PretrazivanjeFolderaSakularna
from DataExtraction import DataExtraction
from SimulationsData import *



# resultsFolder = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna"



def SacularAnalysis_f():
    search = FolderSearch(resultsFolder)
    allNames = FolderSearch.allNames
    n = len(allNames) - 1


    for i in range(n):
        print(allNames[i])

        simulacija_TS = DataExtraction(resultsFolder, i)

SacularAnalysis_f()





def SakularnaFunkcija_TS():
    pretrazivanje = PretrazivanjeFolderaSakularna(resultsFolder)  # A je folderFUZIFORMNA koji u sebi sadrži putanje i imena"
    n = len(pretrazivanje.popisSvihImena) - 1

    for i in range(n):
        simulacija_TS = DataExtraction(resultsFolder, i)  # simulacija_TS je objekt koji ima sve izračunato za tu simulaciju u sebi
# SakularnaFunkcija_TS()