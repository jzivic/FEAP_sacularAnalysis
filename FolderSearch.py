import os
from os import path
from SimulationsData import *


# simPath = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna/"



class FolderSearch:

    allPaths = []
    allNames = []

    def pathToStrings(self, path):
        path = path[1::] if path[0] == "/" else path[0::]
        l, lDirString, s = [],[], None
        for ch in [i for i in path]:
            if ch != "/":
                l.append(ch)
                s = "".join(l)
            else:
                lDirString.append(s)
                l = []
        lDirString.append(s)
        return lDirString


    def __init__(self, directory):
        for root, dirs, files in os.walk(directory):
            if "iparameters" in files and "PRESKOCI" not in self.pathToStrings(root):   #dobre dat koje se anal

                sufix = self.pathToStrings(root)[-1][:3] if self.pathToStrings(root)[-1] == "orginal" else self.pathToStrings(root)[-1]
                simName = self.pathToStrings(root)[7] + "_" + sufix

                FolderSearch.allPaths.append(root)
                FolderSearch.allNames.append(simName)
                # print(2)

                # print(simName)


# FolderSearch(resultsFolder)



# for i in FolderSearch(resultsFolder).allNames:
#     print(i)








nemijenjane = []
folder1 = "r="
folder2A = "param"
folder2B = ""
folderIzuzmi = "PRESKOCI"

class PretrazivanjeFolderaSakularna:
    def __init__(self, putanjaSakularne):
        os.chdir(putanjaSakularne)
        self.putanja = putanjaSakularne
        self.popisSvihPutanja = []
        self.popisSvihImena = []
        self.pretrazivajeFoldera()

    def pretrazivajeFoldera(self):
        for radijus in os.listdir(self.putanja):
            if radijus.startswith(folder1):
                os.chdir(self.putanja + "/" + radijus)
                for parametar_ in os.listdir(self.putanja + "/" + radijus):

                    if parametar_ == folderIzuzmi:
                        continue

                    if parametar_.startswith(folder2A):
                        os.chdir(self.putanja + "/" + radijus + "/" + parametar_)
                        for vrijednost in os.listdir(self.putanja + "/" + radijus + "/" + parametar_):
                            os.chdir(self.putanja + "/" + radijus + "/" + parametar_+"/"+vrijednost)
                            path = self.putanja + "/" + radijus + "/" + parametar_+"/"+vrijednost
                            self.popisSvihPutanja.append(path)
                            self.ime = radijus+"_"+vrijednost
                            self.popisSvihImena.append(self.ime)

                    elif parametar_.startswith(folder2B):
                        os.chdir(self.putanja + "/" + radijus + "/" + parametar_)
                        path = self.putanja + "/" + radijus + "/" + parametar_
                        self.popisSvihPutanja.append(path)
                        nemijenjane.append(path)
                        self.ime = radijus + "_org"
                        self.popisSvihImena.append(self.ime)



                    # print(self.ime)
