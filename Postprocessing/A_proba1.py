import shutil, os
import pandas as pd
import matplotlib.pyplot as plt
# from scipy.stats import linregress

from Preprocessing.SimulationsData import *



# Make "diagrams" dir to save pictures
def MakeDir_diagrams():
    try:
        shutil.rmtree(diagramsDir)
    except:
        FileNotFoundError
    os.mkdir(diagramsDir)





ABData2 = pd.read_pickle(PickleData_AB)



# ABData2["p1"] = ABData2["L"]**3*(5*ABData2["Ddr2"]**2 -1)

# ABData2["p1"] = ABData2["V"] / (ABData2["L"]*ABData2["d2"]**2)

# ABData2["p1"] = ABData2["L"]**3 * (1* ABData2["D"]**2 - ABData2["d2"]**2) / ABData2["d2"]**2
# ABData2["p2"] = ABData2["L"]**3 * (2* ABData2["D"]**2 - ABData2["d2"]**2) / ABData2["d2"]**2
# ABData2["p4"] = ABData2["L"]**3 * (4* ABData2["D"]**2 - ABData2["d2"]**2) / ABData2["d2"]**2


# ABData2["p"] = ABData2["L"]**3 * (4* ABData2["D"]**2 - ABData2["d2"]**2)**2 / ABData2["d2"]**2

# ABData2["p"] = ABData2["L"]**3 * (4*ABData2["D"]**2 - ABData2["d2"]**2)**1 / ABData2["d2"]**2









# NoPos = ""                                                  # descriptive text for selected diagram height
# pos0 = "for healthy $d$"
# pos1 = "for $d$ measured at $h$=62 mm"
# pos2 = "for $d$ measured at $h$=55 mm"
# pos3 = "for $d$ measured at $h$=48 mm"



graphData = {
         "D":{"vName":"D","unit":"mm","txt":"NoPos"},
        # "H":{"vName":"H","unit":"mm","txt":NoPos},
        #  "L":{"vName":"L","unit":"mm","txt":NoPos}, "S":{"vName":"S","unit":"$mm^2$","txt":NoPos},
        #  "V":{"vName":"V","unit":"$mm^3$","txt":NoPos}, "GR":{"vName":"GR","unit":"mm/y","txt":NoPos},
        #  "T":{"vName":"T","unit":"-","txt":NoPos},
        #
        # "d0": {"vName": "d", "unit": "mm", "txt": pos0},
        # "d1": {"vName": "d", "unit": "mm", "txt": pos1},
        # "d2": {"vName": "d", "unit": "mm", "txt": pos2},
        # "d3": {"vName": "d", "unit": "mm", "txt": pos3},
        #
        # "Ddr0": {"vName": "Ddr", "unit": "-", "txt": pos0},
        # "Ddr1": {"vName": "Ddr", "unit": "-", "txt": pos1},
        # "Ddr2": {"vName": "Ddr", "unit": "-", "txt": pos2},
        # "Ddr3": {"vName": "Ddr", "unit": "-", "txt": pos3},

        # "GRPI":{"vName":"GRPI","unit":"$mm^3$","txt":pos0},
        # "GRPI1":{"vName":"GRPI","unit":"$mm^3$","txt":pos1},
        # "GRPI2":{"vName":"GRPI","unit":"$mm^3$","txt":pos2},
        # "GRPI3":{"vName":"GRPI","unit":"$mm^3$","txt":pos3},

        # "NAL":{"vName":"NAL","unit":"mm","txt":pos0},
        # "NAL1":{"vName":"NAL","unit":"mm","txt":pos1},
        # "NAL2":{"vName":"NAL","unit":"mm","txt":pos2},
        # "NAL3":{"vName":"NAL","unit":"mm","txt":pos3},


        # "p1":{"vName":"p1","unit":"mm","txt":""},
        # "p2":{"vName":"p2","unit":"mm","txt":""},
        # "p4":{"vName":"p4","unit":"mm","txt":""},
        "p":{"vName":"p","unit":"mm","txt":""},

         }

chosenData = ABData2


# Plot all values in chosen TimeSteps in loop
def TestPlot():

    # Determine dot color depending on radius size
    def colorR(radius):
        if radius == 8:
            return 'c'
        elif radius == 10:
            return "black"
        elif radius == 12:
            return "m"

    # Iterate all values
    for value in chosenData:
        if value in graphData.keys():                    # made to exclude logistic values

            plt.ylabel("$P$ [-]")
            plt.xlabel("${}$ {}{}{}"  .format(graphData[value]["vName"]," [", graphData[value]["unit"], "]"))       # x axis line
            xVariable = chosenData[value]
            yVariable = chosenData["P"]

            rList = []      # aid, made to store radius of analyzed simulations
            for i in range(len(chosenData[value])):

                if chosenData["S22"][i]<sigmaCritical: # additional condition to exclude higher values

                #legend is like here to avoid multiple unnecessary dot plotting in legend box
                    plt.scatter(xVariable[i], yVariable[i], c=colorR(chosenData["r"][i]),
                                label = ("$r$ = " + str(chosenData["r"][i]) + " mm") if chosenData["r"][i] not in rList else "", alpha=0.7)
                    rList.append(chosenData["r"][i])




            # def statText():
            #     slope, intercept, r, p, se = linregress(chosenData[value], chosenData["P"])
            #     textPosition = (min(chosenData[value]) - (max(chosenData[value]) - min(chosenData[value])) * 0.20)
            #     plt.text(textPosition, 0.9,
            #              'r=' + str(format(r, '.3g')) + "\n" + 'p=' + str(format(p, '.3g')) + "\n" + 'se=' + str(
            #                  format(se, '.3g')), fontsize=12)
            # # statText()


            plt.text(min(chosenData[value]), max(chosenData["P"])+0.1, graphData[value]["txt"])             # position of x label text
            fig = plt.gcf()
            plt.grid(color='k', linestyle=':', linewidth=0.5)
            plt.legend()
            plt.pause(10)
            plt.draw()
            plt.close()
            fig.savefig(diagramsDir + value + '.png', dpi=100)

MakeDir_diagrams()
TestPlot()









