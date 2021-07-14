import shutil, os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

from Preprocessing.SimulationsData import *



# Make "diagrams" dir to save pictures
def MakeDir_diagrams():
    try:
        shutil.rmtree(diagramsDir)
    except:
        FileNotFoundError
    os.mkdir(diagramsDir)


ABData2 = pd.read_pickle(PickleData_AB)



# ABData2["p"] = L**1*(D-d)**2/d**2
# ABData2["p"] = (d3-d2)/(55-48)*H*(D/d2)**2
# ABData2["p"] = (D-d)/(H/2)/d

# ABData2["p"] = ((D-d)/(H/2))/d
# ABData2["p"] = ((D**2)-(D-d)**2)/(D**2)/L
# ABData2["p"] = (d/D)/L**2
# ABData2["p"] = (d/D)/L**2



L = ABData2["L"]
H = ABData2["H"]
S = ABData2["S"]
V = ABData2["V"]
T = ABData2["T"]
D = ABData2["D"]
d0 = ABData2["d0"]
d1 = ABData2["d1"]
d2 = ABData2["d2"]
d3 = ABData2["d3"]



d = d2

# ABData2["LDd0r"] = L*(D/d0)
# ABData2["LDd1r"] = L*(D/d1)
# ABData2["LDd2r"] = L*(D/d2)
# ABData2["LDd3r"] = L*(D/d3)

# ABData2["1\(LDd0r)"] = 1/(L*(D/d0))
# ABData2["1\(LDd1r)"] = 1/(L*(D/d1))
# ABData2["1\(LDd2r)"] = 1/(L*(D/d2))
# ABData2["1\(LDd3r)"] = 1/(L*(D/d3))

# ABData2["L^2Dd0r"] = L**2*(D/d0)
# ABData2["L^2Dd1r"] = L**2*(D/d1)
# ABData2["L^2Dd2r"] = L**2*(D/d2)
# ABData2["L^2Dd3r"] = L**2*(D/d3)

# ABData2["1\(L^2*Dd0r)"] = 1/(L**2*(D/d0))
# ABData2["1\(L^2*Dd1r)"] = 1/(L**2*(D/d1))
# ABData2["1\(L^2*Dd2r)"] = 1/(L**2*(D/d2))
# ABData2["1\(L^2*Dd3r)"] = 1/(L**2*(D/d3))


ABData2["p"] = 1/(L*(D/d))









# doPos = ""                                                  # descriptive text for selected diagram height
# pos0 = "for healthy $d$"
# pos1 = "for $d$ measured at $h$=62 mm"
# pos2 = "for $d$ measured at $h$=55 mm"
# pos3 = "for $d$ measured at $h$=48 mm"



graphData = {

        "p": {"vName": "p", "unit": "mm", "txt": ""},

        "LDd0r":{"vName":"LDd0r","unit":"mm","txt":""},
        "LDd1r":{"vName":"LDd1r","unit":"mm","txt":""},
        "LDd2r":{"vName":"LDd2r","unit":"mm","txt":""},
        "LDd3r":{"vName":"LDd2r","unit":"mm","txt":""},

        "1\(LDd0r)":{"vName":"1/(LDd0r)","unit":"mm","txt":""},
        "1\(LDd1r)":{"vName":"1/(LDd1r)","unit":"mm","txt":""},
        "1\(LDd2r)":{"vName":"1/(LDd2r)","unit":"mm","txt":""},
        "1\(LDd3r)":{"vName":"1/(LDd3r)","unit":"mm","txt":""},

        "L^2Dd0r": {"vName": "L^2Dd0r", "unit": "mm", "txt": ""},
        "L^2Dd1r": {"vName": "L^2Dd1r", "unit": "mm", "txt": ""},
        "L^2Dd2r": {"vName": "L^2Dd2r", "unit": "mm", "txt": ""},
        "L^2Dd3r": {"vName": "L^2Dd2r", "unit": "mm", "txt": ""},

        "1\(L^2*Dd0r)": {"vName": "1/(L^2*Dd0r)", "unit": "mm", "txt": ""},
        "1\(L^2*Dd1r)": {"vName": "1/(L^2*Dd1r)", "unit": "mm", "txt": ""},
        "1\(L^2*Dd2r)": {"vName": "1/(L^2*Dd2r)", "unit": "mm", "txt": ""},
        "1\(L^2*Dd3r)": {"vName": "1/(L^2*Dd3r)", "unit": "mm", "txt": ""},




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

                # if chosenData["S22"][i]<sigmaCritical: # additional condition to exclude higher values

            #legend is like here to avoid multiple unnecessary dot plotting in legend box
                plt.scatter(xVariable[i], yVariable[i], c=colorR(chosenData["r"][i]),
                            label = ("$r$ = " + str(chosenData["r"][i]) + " mm") if chosenData["r"][i] not in rList else "", alpha=0.7)
                rList.append(chosenData["r"][i])




            def statText():
                slope, intercept, r, p, se = linregress(chosenData[value], chosenData["P"])
                print(r)
                textPosition = (min(chosenData[value]) - (max(chosenData[value]) - min(chosenData[value])) * 0.20)
                plt.text(textPosition, 1.05,
                         'r=' + str(format(r, '.3g')) + "\n" + 'p=' + str(format(p, '.3g')) , fontsize=12)
            statText()


            # plt.text(min(chosenData[value]), max(chosenData["P"])+0.1, graphData[value]["txt"])             # position of x label text
            # fig = plt.gcf()
            # plt.grid(color='k', linestyle=':', linewidth=0.5)
            # plt.legend()
            # plt.pause(1)
            # plt.draw()
            # plt.close()
            # fig.savefig(diagramsDir + str(value) + '.png', dpi=100)

            plt.grid(color='k', linestyle=':', linewidth=0.5)
            plt.show()


MakeDir_diagrams()
TestPlot()









