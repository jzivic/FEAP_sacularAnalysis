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
            self.simPath = self.objectDE.allPaths[self.nSim]
            self.simName = self.objectDE.allNames[self.nSim]
            os.chdir(self.simPath)

        elif allSimulationsAnalysis == False:
            self.simPath = oneSimTestPath
            self.simName = "TestName"
            os.chdir(self.simPath)


        self.chosListTS = list(chosenTimeSteps)
        self.nTSt = 0
        self.bEx = 0
        self.Creating_allTS_Vector()                                #OVO SE RADI





        # while self.nTSt < len(self.chosListTS):      # as long as there is steps in list

        self.SettingAnalysisFiles() #"putanja koja je zapravo simPath uvijek"


        if self.CheckAAAFormation() == False:
            self.bEx +=1
            self.chosListTS.remove(self.chosListTS[self.nTSt])

            # self.NoAAA()
            # continue


        elif self.CheckAAAFormation() == True:

            if self.chosListTS[self.nTSt] <= self.maxTS:  #used for limiting simulation till last TS
                3
                #sve ostalo se računa
                
                
                
            else:
                # break
                4
                
            self.nTSt += 1
            self.bEx += 1




    def Creating_allTS_Vector(self):




    def SettingAnalysisFiles(self):
        os.chdir(self.simPath)
        for suffix in suffixList:
            try:
                opening_eIW = open("export__INNER_WALL__" + suffix, "r")
                self.wholeDocument_eIW = opening_eIW.readlines()                                # whole txt read
                self.nl_eIW = sum(1 for line in open("export__INNER_WALL__" + suffix))          #number of lines in export Inner Wall
                self.maxTS = int(self.wholeDocument_eIW[-TSLegnht_eIW + 1].strip().split()[1])  #last TimeStep in simulation

                if self.chosListTS[self.nTSt] <= self.maxTS:                                     #chosenTimeStep = chosen or  maxTS if chosen bigger
                    chosenTimeStep = self.chosListTS[self.nTSt]
                elif self.chosListTS[self.nTSt] > self.maxTS:
                    chosenTimeStep = self.maxTS

                if self.chosListTS[self.nTSt] > 0:      # in past : def SettingChosenTimeStep(self)       # setting starting line in each document
                    startLine_eIW = 68 + TSLegnht_eIW * (self.chosListTS[self.nTSt] - 1)
                    startLine_rIL = 5 + TSLegnht_rIl * (self.chosListTS[self.nTSt] - 1)
                    startLine_ctl = 4 + TSLegnht_ctl * (self.chosListTS[self.nTSt] - 1)
                    startLine_rN1704 = 5 + TSLegnht_rN1704 * (self.chosListTS[self.nTSt] - 1)

                elif self.chosListTS[self.nTSt] < 0:  # negative timesteps counts from the last
                    startLine_eIW = 1 + TSLegnht_eIW * self.chosListTS[self.nTSt]  # number of line in
                    startLine_rIL = 0 + TSLegnht_rIl * self.chosListTS[self.nTSt]
                    startLine_ctl = 0 + TSLegnht_ctl * self.chosListTS[self.nTSt]
                    startLine_rN1704 = 0 + TSLegnht_rN1704 * self.chosListTS[self.nTSt]


                self.startLine_eIW = startLine_eIW % self.nl_eIW
                nNodes = self.wholeDocument_eIW[2].strip().split()                      # number of nodes, written in eIW file
                self.nTheta, self.nZ = int(nNodes[0]), int(nNodes[1])


                opening_rIL = open("res__INNER_lines__" + suffix, "r")
                self.wholeDocument_rIl = opening_rIL.readlines()
                self.nl_rIL = sum(1 for line in open("res__INNER_lines__" + suffix))
                self.startLine_rIL = startLine_rIL  # % self.nl_rIL

                opening_ctl = open("res__CENTERLINE__" + suffix, "r")
                self.cijeli_tekst_ctl = opening_ctl.readlines()
                self.nl_ctl = sum(1 for line in open("res__CENTERLINE__" + suffix))
                self.startLine_ctl = startLine_ctl  # % self.nl_ctl


                opening_rN1704 = open("res__NODE_1704_" + suffix, "r")
                self.cijeli_tekst_rN1704 = opening_rN1704.readlines()
                self.nl_rN1704 = sum(1 for line in open("res__NODE_1704_" + suffix))
                self.startLine_rN1704 = startLine_rN1704 #% self.nl_rN1704

            except:
                FileNotFoundError
                continue


    def CheckAAAFormation(self):
        if sameInitalRadius == True:
            self.D0 = float(self.wholeDocument_rIl[5].strip().split()[0]) * 2               # initial radius D0, deformed or non deformed
        elif sameInitalRadius == False:
            self.D0 = (float(self.wholeDocument_rIl[self.startLine_rIL].strip().split()[0]) +
                       float(self.wholeDocument_rIl[self.startLine_rIL].strip().split()[1]) +
                       float(self.wholeDocument_rIl[self.startLine_rIL].strip().split()[2])) * 2 / 3

        nLine_rIL = self.startLine_rIL

        # iterating over TS, checking in AAA condition is fulfilled
        for line in self.wholeDocument_rIl[self.startLine_rIL: (self.startLine_rIL + TSLegnht_rIl - 1)]:
            nLine_rIL += 1
            line = line.strip().split()
            D = (float(line[0]) + float(line[1]) + float(line[2])) * 2 / 3
            if D >= self.D0 * 1.5:
                return True
        return False












DataExtraction(oneSimTestPath)







