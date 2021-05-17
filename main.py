import os
from os import path
from SimulationsData import *




simPath = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna/"
# simPath = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna/r=10/"




def iteratingOverFolder():
    for root, dirs, files in os.walk(simPath):
        print(root)












# iteratingOverFolder()



# pathAnalysis = "/home/josip/feap/pocetak/parametarskaAnaliza_2/rezultati/sakularna/r=12/parametar_k1/k1=1.06"
pathAnalysis = "/home/josip/feap/pocetak/parametarskaAnaliza_2/rezultati/sakularna/"


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





def iteratingOverFolder():

    for root, dirs, files in os.walk(pathAnalysis):

        if "iparameters" in files and "PRESKOCI" not in pathToStrings(root) :

            print(pathToStrings(root))





iteratingOverFolder()








