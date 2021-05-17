import os, math#, xlsxwriter, openpyxl
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
# from openpyxl.styles import Font, PatternFill

from SimulationsData import *


###################################################################################################################
oneSimTest = "/home/josip/feap/pocetak/" + parametarskaAnaliza + "/rezultati/sakularna/r=10/parametar_ad/ad=3.63"

###################################################################################################################

duljinaStepa_eIW = duljinaStepa + 3
duljinaStepa_rIl = duljinaStepa + 1
duljinaStepa_ctl = duljinaStepa + 1
duljinaStepa_rN1704 = 1

###################################################################################################################


class DataExtraction:
    3
    def __init__(self, simPath, nSimulacije):  # inicijalizacija i kako ce se sve pozivati
        self.nSimulacije = nSimulacije