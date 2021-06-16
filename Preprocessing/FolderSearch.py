"""
Class made to iterate over listed dirs and all subdirs:

    1. Iterates over all dirs and subdirs
    2. Simulations is not analyzed if it is in the "PRESKOCI" dir
    3. Dir is classified as simulations dir if there are "iparameters" file. Analysis starts
    4. Get simulations path and name, store it into  FolderSearch.allPaths and FolderSearch.allNames

"""

import os

class FolderSearch:
    allPaths, allNames = [], []         # class variables

    def pathToStrings(self, path):
        path = path[1::] if path[0] == "/" else path[0::]           # throws out "/" from name
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
            if "iparameters" in files and "PRESKOCI" not in self.pathToStrings(root):
                sufix = self.pathToStrings(root)[-1][:3] if self.pathToStrings(root)[-1] == "orginal" else self.pathToStrings(root)[-1]
                simName = self.pathToStrings(root)[7] + "_" + sufix

                FolderSearch.allPaths.append(root)
                FolderSearch.allNames.append(simName)

# a = FolderSearch(resultsFolder)
# for i in a.allNames:
#     print(i)














