import os, math#, xlsxwriter, openpyxl
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
# from openpyxl.styles import Font, PatternFill

from FolderSearch import FolderSearch

from SimulationsData import *


chosenTimeSteps = [-3]



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

            self.NoAAAFormed()
            # self.chosListTS.remove((self.chosListTS[self.nTSt]))
            # continue

        elif self.CheckAAAFormation() == True:          #if AAA formed
            if self.chosListTS[self.nTSt] <= self.maxTS:  #used for limiting simulation till last TS
                #Calculating d0
                self.Calculating_d0_H_L()
                self.Calculating_D_S22_GR()
                # self.RacunanjeD0_H_L()
                # self.RacunanjeD_S22_GR()


            else:
                # break
                4
                
            self.nTSt += 1
            self.bEx += 1




    def Creating_allTS_Vector(self):                    # vectors to store data
        self.TSName_allTS = []
        self.simName_allTS = []
        self.S22_allTS = []

        self.D_allTS = []
        self.d0_allTS = []

        self.dp1_allTS = []
        self.dp2_allTS = []
        self.dp3_allTS = []

        self.H_allTS = []
        self.L_allTS = []

        self.S_allTS = []
        self.V_allTS = []

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
                self.wholeDocument_ctl = opening_ctl.readlines()
                self.nl_ctl = sum(1 for line in open("res__CENTERLINE__" + suffix))
                self.startLine_ctl = startLine_ctl  # % self.nl_ctl


                opening_rN1704 = open("res__NODE_1704_" + suffix, "r")
                self.wholeDocument_rN1704 = opening_rN1704.readlines()
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

    def NoAAAFormed(self):
        self.TSName = None


        self.S22 = None
        self.D = None
        self.H = None
        self.L = None
        self.S = None
        self.V = None

    def Calculating_d0_H_L(self):

        # auxiliary function for calculating diameter
        def CalculatingDiameter(numberOfLine):
            D = (float(self.wholeDocument_rIl[self.startLine_rIL + numberOfLine].strip().split()[0]) +
                    float(self.wholeDocument_rIl[self.startLine_rIL + numberOfLine].strip().split()[1]) +
                    float(self.wholeDocument_rIl[self.startLine_rIL + numberOfLine].strip().split()[2])) * 2 / 3
            return D


        if sameInitalRadius == True:    #undeformed inital shape
            self.d0 = float(self.wholeDocument_rIl[5].strip().split()[0]) * 2
        elif sameInitalRadius == False:     #deformed inital shape
            self.d0 =  CalculatingDiameter(numberOfLine=0)
        self.d1 =  CalculatingDiameter(numberOfLine=20)          #proximal diameter at height 55m from center
        self.d2 =  CalculatingDiameter(numberOfLine=21)
        self.d3 =  CalculatingDiameter(numberOfLine=22)
        self.HVainTotal = float(self.wholeDocument_rIl[self.startLine_rIL + TSLegnht_rIl - 2].strip().split()[5]) #total vain leght

        # auxiliary lines to find before/after AAA formation lines
        lineA, lineB = 0, 0
        lineBefore = [0, 0, 0]
        self.vectorAAAIndices = []          # AAA formed lines in TS
        nLine_rIL = self.startLine_rIL      # starting line in rIL

        # checking Diameter at every hight to fullfill condition
        for line in self.wholeDocument_rIl[self.startLine_rIL: (self.startLine_rIL + TSLegnht_rIl-1)]:
            nLine_rIL += 1                                                                              # number of line in rIL
            line = line.strip().split()
            D_ = (float(line[0]) + float(line[1]) + float(line[2])) * 2 / 3             # D in every line / height
            Z_ = float(line[4])

            if D_ > self.d0 * 1.05:
                self.vectorAAAIndices.append((nLine_rIL-6) % TSLegnht_rIl)
                if lineB == 0:
                    lineA = lineBefore                  # made to collect elements/heights before and after condition
                    lineB = line
            lineBefore = line

        # linear inteerpolation between before/after forming AAA elements
        try:
            #coordinates of pointA, pointB of line that connects elements before/after condition
            # pA = (rCoord, zCoord)
            pA = [(float(lineA[0]) + float(lineA[1]) + float(lineA[2])) / 3, (float(lineA[3]) + float(lineA[4]) + float(lineA[5])) / 3]
            pB = [(float(lineB[0]) + float(lineB[1]) + float(lineB[2])) / 3, (float(lineB[3]) + float(lineB[4]) + float(lineB[5])) / 3] 
            slope = (pB[1] - pA[1]) / (pB[0] - pA[0])

            dR = pB[0] - 1.05 * self.d0 / 2             # AAA forming point radial offset from coordinates element before
            dH = (dR) * slope                           # AAA forming point axial offset from coordinates element before
            dL = np.sqrt(dR ** 2 + dH ** 2) * 2         #
            dH *= 2                                     # becuase of upper and lower halves
        except TypeError:
            dH, dL = 0, 0

        # AAA points coordinate
        coordAAA = {"z":[], "y":[]}
        for indAn in self.vectorAAAIndices: #iterating over points that fulfill AAA condition, z,y obtained from ctl file !!
            z = float(self.wholeDocument_ctl[self.startLine_ctl + indAn].strip().split()[0])
            y = float(self.wholeDocument_ctl[self.startLine_ctl + indAn].strip().split()[1])
            coordAAA["z"].append(z), coordAAA["y"].append(y)
        try:
            self.H = (coordAAA["z"][len(coordAAA["y"]) - 1] - coordAAA["z"][0]) + 0
            self.L = 0
            for n in range(0, len(coordAAA["y"]) - 1):
                self.L += math.sqrt((coordAAA["z"][n + 1] - coordAAA["z"][n]) ** 2 + (coordAAA["y"][n + 1] - coordAAA["y"][n]) ** 2)
        except IndexError:
            self.H, self.L = 0, 0

        self.H = self.H + dH        # interpolation addition
        self.L = self.L + dL

    # Reading D, GR, S22 from r1704 file
    def Calculating_D_S22_GR(self):
        if self.chosListTS[self.nTSt] > 0:
            nLine = self.wholeDocument_rN1704[self.startLine_rN1704 - 1].strip().split()
        elif self.chosListTS[self.nTSt] < 0:
            nLine = self.wholeDocument_rN1704[self.startLine_rN1704].strip().split()

        self.D = float(nLine[2]) * 2
        self.GR = float(nLine[3]) * 2
        self.S22 = float(nLine[5]) * 1000  # kPa




    #Reading eIW (table of data)

    def MainProgram(self):  # početna funkcija koja ide kroz sve redove ispisa
        self.rjecnikKoraka = {}  # for whole TS
        self.count_eIW = -1  # zato da prvi red s podacima bude na 0

        for self.line in self.wholeDocument_eIW[self.startLine_eIW: self.startLine_eIW + TSLegnht_eIW]:
            self.line = self.line.strip().split()  # red teksta
            if self.line == []: continue  # preskakanje praznih redova, ne ulaze u brojac_eIW
            self.count_eIW += 1
            if self.count_eIW == 0:  # ==Timestep: red
                self.NewTimeStep()  # za svaki novi Timestep
                continue
            self.PojedinaTheta()  # u svakom redu hvata Thetu
            if self.brojac_eIW == self.nZ:
                self.RacunanjeS_V()  # ako je na brojac_eIW==nZ, Timestep je gotov
                self.Resetiranje()

    def NewTimeStep(self):  # f za resetiranje brojača i skupova podataka
        self.imeKoraka = self.redak[0] + self.redak[1]  # Timestep: n
        self.listaZ = []

    def PojedinaTheta(self):  # ide po jednoj liniji u datoteci
        self.listaTheta = []
        tocka = []
        for rijec in self.redak:
            broj = float(rijec)
            tocka.append(broj)
            if len(tocka) == 3:
                self.listaTheta.append(tocka)
                tocka = []
        self.listaZ.append(self.listaTheta)  # resetira se za svaki NoviKorak

    def Resetiranje(self):
        self.brojac_eIW = -1
        self.rjecnikKoraka[self.imeKoraka] = self.listaZ






    # def GlavniProgram(self):  # početna funkcija koja ide kroz sve redove ispisa
    #     self.rjecnikKoraka = {}  # cijeli Timestep je ovdje (->listaZ -> listaTheta->tocka)
    #     self.brojac_eIW = -1  # zato da prvi red s podacima bude na 0
    #
    #     for self.redak in self.cijeli_tekst_eIW[self.startniRed_eIW: self.startniRed_eIW + duljinaStepa_eIW]:
    #         self.redak = self.redak.strip().split()  # red teksta
    #         if self.redak == []: continue  # preskakanje praznih redova, ne ulaze u brojac_eIW
    #         self.brojac_eIW += 1
    #         if self.brojac_eIW == 0:  # ==Timestep: red
    #             self.NoviKorak()  # za svaki novi Timestep
    #             continue
    #         self.PojedinaTheta()  # u svakom redu hvata Thetu
    #         if self.brojac_eIW == self.nZ:
    #             self.RacunanjeS_V()  # ako je na brojac_eIW==nZ, Timestep je gotov
    #             self.Resetiranje()

    # def NoviKorak(self):  # f za resetiranje brojača i skupova podataka
    #     self.imeKoraka = self.redak[0] + self.redak[1]  # Timestep: n
    #     self.listaZ = []
    #
    # def PojedinaTheta(self):  # ide po jednoj liniji u datoteci
    #     self.listaTheta = []
    #     tocka = []
    #     for rijec in self.redak:
    #         broj = float(rijec)
    #         tocka.append(broj)
    #         if len(tocka) == 3:
    #             self.listaTheta.append(tocka)
    #             tocka = []
    #     self.listaZ.append(self.listaTheta)  # resetira se za svaki NoviKorak
    #
    # def Resetiranje(self):
    #     self.brojac_eIW = -1
    #     self.rjecnikKoraka[self.imeKoraka] = self.listaZ







#############################
#   POMOĆNE FUNKCIJE
##############################




DataExtraction(oneSimTestPath)







