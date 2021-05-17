import os
from os import path
from SimulationsData import *








simPath = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna/"




class FolderSearch:

    allPaths = []
    allNames = []


    def __init__(self, folder):
        self.folder = folder
        self.iteratingOverFolder()


    def iteratingOverFolder(self):
        for root, dirs, files in os.walk(self.folder):

            for lvl1 in dirs:
                if str(lvl1).startswith("r="):
                    rFolder = lvl1
                    # print(i)
                    os.chdir(simPath+"/"+rFolder)
                    print(os.getcwd())


            break















FolderSearch(simPath)

















