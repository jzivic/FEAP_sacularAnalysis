import shutil, os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

from Preprocessing.SimulationsData import *




def MakeFolder_diagrams():
    try:
        shutil.rmtree(diagramsFolder)
    except:
        FileNotFoundError
    os.mkdir(diagramsFolder)

MakeFolder_diagrams()


abData = pd.read_pickle(PickleData_ab)
cData = pd.read_pickle(PickleData_c)
allData = pd.read_pickle(PickleData_all)


chosenData = abData


NoPos = ""
pos0 = "for healthy $d$"
pos1 = "for $d$ measured at $h$=62 mm"
pos2 = "for $d$ measured at $h$=55 mm"
pos3 = "for $d$ measured at $h$=48 mm"


graphData = {
         "D":{"vName":"D","unit":"mm","txt":NoPos}, "H":{"vName":"H","unit":"mm","txt":NoPos},
         "L":{"vName":"L","unit":"mm","txt":NoPos}, "S":{"vName":"S","unit":"$mm^2$","txt":NoPos},
         "V":{"vName":"V","unit":"$mm^3$","txt":NoPos}, "GR":{"vName":"GR","unit":"mm/y","txt":NoPos},
         "T":{"vName":"T","unit":"-","txt":NoPos},

        "d0": {"vName": "d", "unit": "mm", "txt": pos0},
        "d1": {"vName": "d", "unit": "mm", "txt": pos1},
        "d2": {"vName": "d", "unit": "mm", "txt": pos2},
        "d3": {"vName": "d", "unit": "mm", "txt": pos3},

        "Ddr0": {"vName": "Ddr", "unit": "-", "txt": pos0},
        "Ddr1": {"vName": "Ddr", "unit": "-", "txt": pos1},
        "Ddr2": {"vName": "Ddr", "unit": "-", "txt": pos2},
        "Ddr3": {"vName": "Ddr", "unit": "-", "txt": pos3},

        "GRPI":{"vName":"GRPI","unit":"$mm^3$","txt":pos0},
        "GRPI1":{"vName":"GRPI","unit":"$mm^3$","txt":pos1},
        "GRPI2":{"vName":"GRPI","unit":"$mm^3$","txt":pos2},
        "GRPI3":{"vName":"GRPI","unit":"$mm^3$","txt":pos3},

        "NAL":{"vName":"NAL","unit":"mm","txt":pos0},
        "NAL1":{"vName":"NAL","unit":"mm","txt":pos1},
        "NAL2":{"vName":"NAL","unit":"mm","txt":pos2},
        "NAL3":{"vName":"NAL","unit":"mm","txt":pos3},
         }



def PlotingALLDiagrams():

    def colorR(radius):
        if radius == 8:
            return 'c'
        elif radius == 10:
            return "black"
        elif radius == 12:
            return "m"

    for value in chosenData:
        if value in graphData.keys():

            plt.ylabel("$P$ [-]")
            plt.xlabel("${}$ {}{}{}"  .format(graphData[value]["vName"]," [", graphData[value]["unit"], "]"))#, **hfont) # ako se želi mijenjati font
            xVariable = chosenData[value]
            yVariable = chosenData["P"]

            rList = []
            for i in range(len(chosenData[value])):

                # if chosenData["S22"][i]<800: # ovo je dodatak da reže sve iznad 1000 (800 iz data) da se dobije kao u članku

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


            plt.text(min(chosenData[value]), max(chosenData["P"])+0.1, graphData[value]["txt"])
            fig = plt.gcf()
            plt.grid(color='k', linestyle=':', linewidth=0.5)
            plt.legend()
            plt.pause(1)
            plt.draw()
            plt.close()
            fig.savefig(diagramsFolder + value + '.png', dpi=300)


    # for name, values in chosenData.iteritems():
    #     print('{name}: {value}'.format(name=name, value=values[0]))



PlotingALLDiagrams()













def PlotanjeSvega():

    def bojaR(rad):
        if rad == 8:
            return 'c'
        elif rad == 10:
            return "black"
        elif rad == 12:
            return "m"

    for nGrafa in range(len(velicine)):
        def pojedinacniPlot(S22_GR_param):
            plt.ylabel("$P$ [-]")
            plt.xlabel(velicine[nGrafa][2])#, **hfont) # ako se želi mijenjati font

            xVarijabla = velicine[nGrafa][0]
            yVarijabla = allData["P"]
            popisRadijusa = []
            # popisX, popisY = [],[] # vezano uz linReg

            for i in range(len(xVarijabla)):
                for j in range(len(xVarijabla[i])):
                    if Flag[i][j][0] in S22_GR_param and sigma[i][j]<1000:
                        popisX.append(xVarijabla[i][j])
                        popisY.append(yVarijabla[i][j])

                        plt.scatter(xVarijabla[i][j], yVarijabla[i][j], color=bojaR(d[i]), s=14,
                                    label=("$r$ = "+str(d[i])+" mm") if d[i] not in popisRadijusa else "", alpha=0.7)

                        popisRadijusa.append(d[i])

            def pomocniIspis():
                slope, intercept, r, p, se = linregress(popisX, popisY)
                pozicijaOznake_x1 = (min(popisX) - (max(popisX) - min(popisX)) * 0.22)

                plt.text(pozicijaOznake_x1, 1.04,
                         'r=' + str(format(r, '.3g')) + "\n" + 'p=' + str(format(p, '.3g')) + "\n" + 'se=' + str(
                             format(se, '.3g')), fontsize=12)

                print("r=",r)
                print(velicine[nGrafa][1],"=",popisX)
                print("P=",popisY)
            # pomocniIspis()

            fig = plt.gcf()
            plt.grid(color='k', linestyle=':', linewidth=0.5)
            # plt.xticks(rotation = 45)
            fig.subplots_adjust(bottom=0.18) #pomak dolje crte da ne odreže graf
            fig.subplots_adjust(left=0.15)

            pozicijaOznake_x = (min(popisX) - (max(popisX) -min(popisX))*0.15)
            plt.text(pozicijaOznake_x, 0.22, velicine[nGrafa][4])

            try:
                if str(velicine[nGrafa][3]).startswith("for "):
                    plt.text(min(popisX), 1.05,velicine[nGrafa][3] )
            except IndexError:
                pass
            try:
                plt.xlim(velicine[nGrafa][5]) if type(velicine[nGrafa][5]) == list else print()
            except IndexError:
                pass
            if velicine == velicineLegenda:
                """
                handletextpad - razmak mark do r
                labelspacing - između r vertikalno
                borderpad - od sredine do ruba okvira
                """
                plt.legend(loc='lower right', framealpha=1, labelspacing=0, borderpad=0.1, handletextpad=-0.5,
                           handlelength=1.8,  bbox_to_anchor=(1.025, -0.036))

            plt.pause(1)
            plt.draw()
            plt.close()
            fig.savefig(grafovi + velicine[nGrafa][1]+'.png', dpi=300)
        pojedinacniPlot(["A", "B"])

# PlotanjeSvega()










def PlotingALLDiagrams():

    def colorR(radius):
        if radius == 8:
            return 'c'
        elif radius == 10:
            return "black"
        elif radius == 12:
            return "m"

    for value in chosenData:
        if value in units.keys():

            print(units[value]["txt"])

            # plt.ylabel("$P$ [-]")
            # plt.xlabel("${}$ {}{}{}"  .format(chosenData[value].name," [", units[chosenData[value]]["vName"], "]"))#, **hfont) # ako se želi mijenjati font
            # xVariable = chosenData[value]
            # yVariable = chosenData["P"]
            #
            # rList = []
            # for i in range(len(chosenData[value])):
            #     plt.scatter(xVariable[i], yVariable[i], c=colorR(chosenData["r"][i]),
            #                 label = ("$r$ = " + str(chosenData["r"][i]) + " mm") if chosenData["r"][i] not in rList else "", alpha=0.7)
            #     rList.append(chosenData["r"][i])
            #
            #
            # def statText():
            #     slope, intercept, r, p, se = linregress(chosenData[value], chosenData["P"])
            #     textPosition = (min(chosenData[value]) - (max(chosenData[value]) - min(chosenData[value])) * 0.20)
            #     plt.text(textPosition, 0.9,
            #              'r=' + str(format(r, '.3g')) + "\n" + 'p=' + str(format(p, '.3g')) + "\n" + 'se=' + str(
            #                  format(se, '.3g')), fontsize=12)
            # # statText()
            #
            #
            # def hText():
            #     print(units[value][1].startswith("for"))


            # hText()



# """
#             try:
#                 if str(velicine[nGrafa][3]).startswith("for "):
#                     plt.text(min(popisX), 1.05,velicine[nGrafa][3] )
#             except IndexError:
#                 pass
# """






            # fig = plt.gcf()
            # plt.grid(color='k', linestyle=':', linewidth=0.5)
            # plt.legend()
            # plt.pause(1)
            # plt.draw()
            # plt.close()
            # fig.savefig(diagramsFolder + value + '.png', dpi=300)


    # for name, values in chosenData.iteritems():
    #     print('{name}: {value}'.format(name=name, value=values[0]))



# PlotingALLDiagrams()



