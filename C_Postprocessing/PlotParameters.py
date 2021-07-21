"""
Plot all diagrams in a loop.
"""

import shutil, os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

from A_Preprocessing.SimulationsData import *


font = {'family' : 'Times New Roman',
        'size'   : 23}
plt.rc('font', **font)
plt.rcParams['mathtext.fontset'] = 'stix'



# Make "diagrams" dir to save pictures
def MakeDir_diagrams():
    try:
        shutil.rmtree(diagramsDir)
    except:
        FileNotFoundError
    os.mkdir(diagramsDir)


# Load chosen data depending on flag
def chosenData_f():
    if chosenFlag =="AB":
        AB_Data = pd.read_pickle(PickleData_AB)
        return AB_Data

    elif chosenFlag =="C":
        C_Data = pd.read_pickle(PickleData_C)
        return C_Data

    elif chosenFlag =="all":
        all_Data = pd.read_pickle(PickleData_all)
        return all_Data
chosenData = chosenData_f()



NoPos = ""                                                  # descriptive text for selected diagram height
pos0 = "for healthy $d$"
pos1 = "for $d$ measured at $h$=62 mm"
pos2 = "for $d$ measured at $h$=55 mm"
pos3 = "for $d$ measured at $h$=48 mm"

"""
plotData: 
    Describing each value, additional informations
        vName - value name on x axis
        txt - additional description in the corner if necessary
"""
plotData = {
         "D":{"vName":"$D$","unit":"mm","heightLabel":NoPos, "letter":"a)"},
         "L":{"vName":"$L$","unit":"mm","heightLabel":NoPos, "letter":"b)"},
         "S":{"vName":"$S$","unit":"mm$^2$","heightLabel":NoPos, "letter":"a)"},
         "V":{"vName":"$V$","unit":"mm$^3$","heightLabel":NoPos, "letter":"b)"},
         "T":{"vName":"$T$","unit":"-","heightLabel":NoPos, "letter":"b)"},

        "d0": {"vName": "d", "unit": "mm", "heightLabel": pos0, "letter":")"},
        "d1": {"vName": "$d$", "unit": "mm", "heightLabel": pos1, "letter":"a)"},
        "d2": {"vName": "$d$", "unit": "mm", "heightLabel": pos2, "letter":"a)"},
        "d3": {"vName": "$d$", "unit": "mm", "heightLabel": pos3, "letter":"a)"},

        "Ddr0": {"vName":"$Ddr$", "unit":"-", "heightLabel": pos0, "letter":"a)"},
        "Ddr1": {"vName":"$Ddr$", "unit":"-", "heightLabel": pos1,  "letter":"b)"},
        "Ddr2": {"vName":"$Ddr$", "unit":"-", "heightLabel": pos2,  "letter":"b)"},
        "Ddr3": {"vName":"$Ddr$", "unit":"-", "heightLabel": pos3,  "letter":"b)"},

        "GRPI0": {"vName":"GRPI", "unit":"mm", "heightLabel":pos0, "letter":"a)"},
        "GRPI1": {"vName":"GRPI", "unit":"mm", "heightLabel":pos1, "letter":"c)"},
        "GRPI2": {"vName":"GRPI", "unit":"mm", "heightLabel":pos2, "letter":"c)"},
        "GRPI3": {"vName":"GRPI", "unit":"mm", "heightLabel":pos3, "letter":"c)"},

        "NAL0": {"vName":"NAL", "unit":"mm", "heightLabel":pos0, "letter":"b)"},
        "NAL1": {"vName":"NAL", "unit":"mm", "heightLabel":pos1, "letter":"d)"},
        "NAL2": {"vName":"NAL", "unit":"mm", "heightLabel":pos2, "letter":"d)"},
        "NAL3": {"vName":"NAL", "unit":"mm", "heightLabel":pos3, "letter":"d)"},
         }


# list of values that have legend in the corner
diagWithLegend = ["D", "Ddr0", "S", "GRPI0", "GRPI1", "GRPI2", "GRPI3" ]


# Plot all values in chosen TimeSteps in loop
def PlotingAllDiagrams():

    # Determine dot color depending on radius size
    def colorR(radius):
        if radius == 8:
            return 'c'
        elif radius == 10:
            return "black"
        elif radius == 12:
            return "m"

    # Iterate over all values
    for value in chosenData:
        if value in plotData.keys():

            plt.ylabel("RPI [-]")
            plt.xlabel("{} {}{}{}"  .format(plotData[value]["vName"]," [", plotData[value]["unit"], "]"))       # x axis line
            xVariable = chosenData[value]
            yVariable = chosenData["RPI"]

            # # iterates over all points to get color and get rid of unnecessary legend data
            rList = []                                                                 # aid, made to store radius of analyzed simulations
            for i in range(len(chosenData[value])):
                # legend to avoid multiple unnecessary dot plotting in legend box
                plt.scatter(xVariable[i], yVariable[i], c=colorR(chosenData["r"][i]), s=14,
                            label = ("$r$ = " + str(chosenData["r"][i]) + " mm") if chosenData["r"][i] not in rList else "", alpha=0.7)
                rList.append(chosenData["r"][i])


            fig = plt.gcf()
            plt.grid(color='k', linestyle=':', linewidth=0.5)
            fig.subplots_adjust(bottom=0.18)                        # empty space on the bottom
            fig.subplots_adjust(left=0.20)

            heightLabelPosition_x = min(xVariable) - abs(max(xVariable) - min(xVariable))*0.05          # txt position
            heightLabelPosition_y = max(yVariable)*1.06
            plt.text(heightLabelPosition_x, heightLabelPosition_y, plotData[value]["heightLabel"])      # h,d values

            letterPosition_x = (min(xVariable) - (max(xVariable) - min(xVariable)) * 0.25)              # label in article
            letterPosition_y = (min(yVariable) - (max(yVariable) - min(yVariable)) * 0.25)
            plt.text(letterPosition_x, letterPosition_y, plotData[value]["letter"])

            if value in diagWithLegend:
                plt.legend(loc='upper left', framealpha=1, labelspacing=0, borderpad=0.1, handletextpad=-0.5,
                           handlelength=1.8, bbox_to_anchor=(-0.03, 1.04))
            plt.pause(1)
            plt.draw()
            plt.close()
            fig.savefig(diagramsDir + value + '.png', dpi=300)


# MakeDir_diagrams()
# PlotingAllDiagrams()












































"""



# Plot all values in chosen TimeSteps in loop
def PlotingAllDiagrams():

    # Determine dot color depending on radius size
    def colorR(radius):
        if radius == 8:
            return 'c'
        elif radius == 10:
            return "black"
        elif radius == 12:
            return "m"

    # Iterate over all values
    for value in chosenData:
        if value in plotData.keys():               # made to exclude logistic values (flag)

            print(type(plotData[value]))
        
            # print()



            # plt.ylabel("$P$ [-]")
            # plt.xlabel("${}$ {}{}{}"  .format(plotData[value]["vName"]," [", plotData[value]["unit"], "]"))       # x axis line
            # xVariable = chosenData[value]
            # yVariable = chosenData["P"]
            #
            # # iterates over all points to get color and get rid of unnecessary legend data
            # rList = []                                                                 # aid, made to store radius of analyzed simulations
            # for i in range(len(chosenData[value])):
            #
            #     # legend to avoid multiple unnecessary dot plotting in legend box
            #     plt.scatter(xVariable[i], yVariable[i], c=colorR(chosenData["r"][i]),
            #                 label = ("$r$ = " + str(chosenData["r"][i]) + " mm") if chosenData["r"][i] not in rList else "", alpha=0.7)
            #     rList.append(chosenData["r"][i])
            #
            # # Statistical values written on upper left corner
            # def statText():
            #     slope, intercept, r, p, se = linregress(chosenData[value], chosenData["P"])
            #     textPosition = (min(chosenData[value]) - (max(chosenData[value]) - min(chosenData[value])) * 0.20)
            #     plt.text(textPosition, 0.9,
            #              'r=' + str(format(r, '.3g')) + "\n" + 'p=' + str(format(p, '.3g')) + "\n" + 'se=' + str(
            #                  format(se, '.3g')), fontsize=12)
            # # # statText()
            #
            #
            # plt.text(min(chosenData[value]), max(chosenData["P"]) + (max(chosenData["P"])-min(chosenData["P"]))*0.1, plotData[value]["txt"])  # position of x label text
            # fig = plt.gcf()
            # plt.grid(color='k', linestyle=':', linewidth=0.5)
            # plt.legend()
            # plt.pause(1)
            # plt.draw()
            # plt.close()
            # fig.savefig(diagramsDir + value + '.png', dpi=300)


"""




