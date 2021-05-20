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


    def __init__(self, folder):
        for root, dirs, files in os.walk(folder):
            if "iparameters" in files and "PRESKOCI" not in self.pathToStrings(root):   #dobre dat koje se anal

                sufix = self.pathToStrings(root)[-1][:3] if self.pathToStrings(root)[-1] == "orginal" else self.pathToStrings(root)[-1]
                simName = self.pathToStrings(root)[7] + "_" + sufix

                FolderSearch.allPaths.append(root)
                FolderSearch.allNames.append(simName)












