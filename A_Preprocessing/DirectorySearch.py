"""
Class made to iterate over dirs and all subdirs:

    1. Iterates over all dirs and subdirs in main dir
    2. Simulations is not analyzed if it is located in "PRESKOCI" dir
    3. Dir is classified as simulations dir if there are "iparameters" file. Analysis starts
    4. Get simulations path and name, store it into  DirectorySearch.allPaths and DirectorySearch.allNames

"""

import os

class DirectorySearch:
    allPaths, allNames = [], []         # class variables to store data from all simulations

    def pathToStrings(self, path):
        path = path[1::] if path[0] == "/" else path[0::]           # throws out "/" from start
        l, lDirString, s = [],[], None

        # iterates over path string and throws out all "/" chars. Makes list from path string
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
            if "iparameters" in files and "PRESKOCI" not in self.pathToStrings(root): # find simulations folder
                sufix = self.pathToStrings(root)[-1][:3] if self.pathToStrings(root)[-1] == "orginal" else self.pathToStrings(root)[-1]
                simName = self.pathToStrings(root)[7] + "_" + sufix

                DirectorySearch.allPaths.append(root)
                DirectorySearch.allNames.append(simName)

# a = DirectorySearch(resultsDir)
# for i in a.allNames:
#     print(i)














