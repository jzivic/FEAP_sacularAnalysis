import os, math#, xlsxwriter, openpyxl
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
# from openpyxl.styles import Font, PatternFill

from FolderSearch import FolderSearch

from SimulationsData import *


###################################################################################################################
oneSimTestPath = "/home/josip/feap/pocetak/" + parametarskaAnaliza + "/rezultati/sakularna/r=10/parametar_ad/ad=3.63"
###################################################################################################################

duljinaStepa_eIW = duljinaStepa + 3
duljinaStepa_rIl = duljinaStepa + 1
duljinaStepa_ctl = duljinaStepa + 1
duljinaStepa_rN1704 = 1

###################################################################################################################


class DataExtraction:

    def __init__(self, resultsFolder, nSim):  # inicijalizacija i kako ce se sve pozivati
        self.nSim = nSim


        # if analizaSvihSimulacija == True:
        #     self.objektPS = PretrazivanjeFolderaSakularna(putanjaSakularne)  # putanjaSakularne
        #     putanjaSimulacije = self.objektPS.popisSvihPutanja[self.nSimulacije]
        # elif analizaSvihSimulacija == False:
        #     putanjaSimulacije = putanjaPojedinacnogFoldera
        #     os.chdir(putanjaSimulacije)


        if allSimulationsAnalysis == True:
            self.objectDE = FolderSearch(resultsFolder)  # putanjaSakularne
            simPath = self.objectDE.allPaths[self.nSim]

        elif analizaSvihSimulacija == False:
            simPath = oneSimTestPath
            os.chdir(simPath)


























