import os, math#, xlsxwriter, openpyxl
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
# from openpyxl.styles import Font, PatternFill

from FolderSearch import FolderSearch

from SimulationsData import *


###################################################################################################################
# analyzing just one simulation for testing
oneSimTestPath = "/home/josip/feap/pocetak/" + parametarskaAnaliza + "/rezultati/sakularna/r=10/parametar_k1/k1=1.06"
###################################################################################################################

TSLenght = 51
TSLegnht_eIW = TSLenght + 3
TSLegnht_rIl = TSLenght + 1
TSLegnht_ctl = TSLenght + 1
TSLegnht_rN1704 = 1

###################################################################################################################


class DataExtraction:

    def __init__(self, resultsFolder, nSim=0):
        self.nSim = nSim


        if allSimulationsAnalysis == True:               # ovo se tek poslije konstruktora izvodi ????

            self.objectDE = FolderSearch(resultsFolder)  # putanjaSakularne
            simPath = self.objectDE.allPaths[self.nSim]
            self.simPath = self.objectDE.allPaths[self.nSim]
            self.simName = self.objectDE.allNames[self.nSim]
            os.chdir(simPath)

        elif analizaSvihSimulacija == False:
            simPath = oneSimTestPath
            self.simPath = oneSimTestPath
            self.simName = "TestName"

            print(self.simPath)
            os.chdir(simPath)



        self.chosenTStSim = list(chosenTimeSteps)
        self.nTSt = 0
        self.bEx = 0
        # self.Creating_aTS_Vector()


        # print(simPath)


        while self.nTSt < len(self.chosenTStSim):

            self.SettingChosenTimeStep()
            self.SettingAnalysisFiles() #"putanja koja je zapravo simPath uvijek"
            # self.SettingAnalysisFiles(self.simPath)






    def SettingChosenTimeStep(self):
        if self.chosenTStSim[self.nTSt] > 0:
            startingLine_eIW = 69 -1 + TSLegnht_eIW * (self.chosenTStSim[self.nTSt] - 1 )
            startingLine_rIL = 6 - 1 + TSLegnht_rIl * (self.chosenTStSim[self.nTSt] - 1 )
            startingLine_ctl = 5 - 1 + TSLegnht_ctl * (self.chosenTStSim[self.nTSt] - 1 )
            startingLine_rN1704 = 6 - 1 + TSLegnht_rN1704 * (self.chosenTStSim[self.nTSt] - 1 )

        elif self.chosenTStSim[self.nTSt] < 0:  #negative timesteps counts from the last
            startingLine_eIW = 1 + TSLegnht_eIW * self.chosenTStSim[self.nTSt]  # number of line in
            startingLine_rIL = 0 + TSLegnht_rIl * self.chosenTStSim[self.nTSt]
            startingLine_ctl = 0 + TSLegnht_ctl * self.chosenTStSim[self.nTSt]
            startingLine_rN1704 = 0 + TSLegnht_rN1704 * self.chosenTStSim[self.nTSt]





    def SettingAnalysisFiles(self, pathParameter):
        # os.chdir(self.simPath)


        print(pathParameter)

        for suffix in suffixList:
            try:

                opening_eIW = open("export__INNER_WALL__" + suffix, "r")
                self.wholeDocument_eIW = opening_eIW.readlines()
                self.nl_eIW = sum(1 for line in open("export__INNER_WALL__" + suffix))          #number of lines in export Inner Wall
                self.maxTS = int(self.wholeDocument_eIW[-TSLegnht_eIW + 1].strip().split()[1])  #last TimeStep in simulation


                if self.chosenTStSim[self.nTSt] <= self.maxTS:
                    chosenTimeStep = self.oKorSim[self.bK]                  # BEZ s!!!!!
                elif self.oKorSim[self.bK] > self.maxTS:
                    odabraniKorak = self.maxTS





            except:
                FileNotFoundError
                continue













DataExtraction(oneSimTestPath)







