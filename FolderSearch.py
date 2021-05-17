import os
from os import path
from SimulationsData import *








simPath = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna/"
# simPath = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna/r=10/"




class FolderSearch:

    allPaths = []
    allNames = []


    def __init__(self, folder):

        for root, dirs, files in os.walk(folder):

            if "iparameters" in files and "PRESKOCI" not in self.pathToStrings(root):   #dobre dat koje se anal
                print(root)




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
        return lDirString




"""
def pathToStrings(path):

    path = path[1::] if path[0]=="/" else path[0::]
    l, lDirString, s = [],[], None

    for ch in [i for i in path]:
        if ch != "/":
            l.append(ch)
            s = "".join(l)
        else:
            lDirString.append(s)
            l = []
    # print(lDirString)
    return lDirString

# pathToStrings(pathAnalysis)
"""



FolderSearch(simPath)

















