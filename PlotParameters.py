import shutil, os, matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

from SimulationsData import *



def MakeFolder_diagrams():
    try:
        shutil.rmtree(diagramsFolder)
    except:
        FileNotFoundError
    os.mkdir(diagramsFolder)

MakeFolder_diagrams()


NoPos = 0
pos0 = "for healthy $d$"
pos1 = "for $d$ measured at $h$=62 mm"
pos2 = "for $d$ measured at $h$=55 mm"
pos3 = "for $d$ measured at $h$=48 mm"


def pojedinacniPlot(S22_GR_param):
    plt.ylabel("$P$ [-]")
    plt.xlabel(velicine[nGrafa][2])  # , **hfont) # ako se želi mijenjati font

    xVarijabla = velicine[nGrafa][0]
    yVarijabla = P
    popisRadijusa = []
    popisX, popisY = [], []  # vezano uz linReg

    for i in range(len(xVarijabla)):
        for j in range(len(xVarijabla[i])):
            if Flag[i][j][0] in S22_GR_param and sigma[i][j] < 1000:
                popisX.append(xVarijabla[i][j])
                popisY.append(yVarijabla[i][j])

                plt.scatter(xVarijabla[i][j], yVarijabla[i][j], color=bojaR(d[i]), s=14,
                            label=("$r$ = " + str(d[i]) + " mm") if d[i] not in popisRadijusa else "", alpha=0.7)

                popisRadijusa.append(d[i])

    def pomocniIspis():
        slope, intercept, r, p, se = linregress(popisX, popisY)
        pozicijaOznake_x1 = (min(popisX) - (max(popisX) - min(popisX)) * 0.22)

        plt.text(pozicijaOznake_x1, 1.04,
                 'r=' + str(format(r, '.3g')) + "\n" + 'p=' + str(format(p, '.3g')) + "\n" + 'se=' + str(
                     format(se, '.3g')), fontsize=12)

        print("r=", r)
        print(velicine[nGrafa][1], "=", popisX)
        print("P=", popisY)

    # pomocniIspis()

    fig = plt.gcf()
    plt.grid(color='k', linestyle=':', linewidth=0.5)
    # plt.xticks(rotation = 45)
    fig.subplots_adjust(bottom=0.18)  # pomak dolje crte da ne odreže graf
    fig.subplots_adjust(left=0.15)

    pozicijaOznake_x = (min(popisX) - (max(popisX) - min(popisX)) * 0.15)
    plt.text(pozicijaOznake_x, 0.22, velicine[nGrafa][4])

    try:
        if str(velicine[nGrafa][3]).startswith("for "):
            plt.text(min(popisX), 1.05, velicine[nGrafa][3])
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
                   handlelength=1.8, bbox_to_anchor=(1.025, -0.036))

    plt.pause(1)
    plt.draw()
    plt.close()
    fig.savefig(grafovi + velicine[nGrafa][1] + '.png', dpi=300)


pojedinacniPlot(["A", "B"])









