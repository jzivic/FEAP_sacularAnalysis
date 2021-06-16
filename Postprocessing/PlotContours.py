import shutil, os
import pandas as pd
import matplotlib.pyplot as plt

from Preprocessing.SimulationsData import *
from Preprocessing.FolderSearch import FolderSearch


def MakeFolder_contours():
    try:
        shutil.rmtree(contoursFolder)
    except: FileNotFoundError
    os.mkdir(contoursFolder)
    duljinaStepa = 51+1

MakeFolder_contours()


# folderSearch = FolderSearch(resultsFolder)
allPath = FolderSearch(resultsFolder).allPaths
allNames = FolderSearch(resultsFolder).allNames




def PlotAllCont():

    for n in range(len(allPath)):
        os.chdir(allPath[n])

        nl_rIL = sum(1 for line in open("res__INNER_lines__101-2"))
        nl_ctl = sum(1 for line in open("res__CENTERLINE__101-2"))
        sr_rIL = [i for i in range(nl_rIL)]
        sr_ctl = [i for i in range(nl_ctl)]

        for nTS in range(len(chosenTSContours)):
            startLine_rIL = -2 + (TSLeght+1) * chosenTSContours[nTS] + nl_rIL
            startLine_ctl = -2 + (TSLeght+1) * chosenTSContours[nTS] + nl_ctl

            chL_rIL = [i for i in range(startLine_rIL, (startLine_rIL + TSLeght + 1))]
            rmLine_rIL = list(sr_rIL)


            for i in chL_rIL:
                rmLine_rIL.remove(i)
            df_rIL = pd.read_csv("res__INNER_lines__101-2", sep='    ', skiprows=rmLine_rIL)
            # df_rIL.rename(columns={list(df_rIL)[1]: "r", list(df_rIL)[4]: "z"}, inplace=True)

            df_rIL.rename(columns={list(df_rIL)[1]: "r", list(df_rIL)[4]: "z"}, inplace=True)

            ok_ctl = [i for i in range(startLine_ctl, (startLine_ctl + TSLeght + 1))]
            rmLine_ctl = list(sr_ctl)

            for i in ok_ctl:
                rmLine_ctl.remove(i)
                df_ctl = pd.read_csv("res__CENTERLINE__101-2", sep='     ', skiprows=rmLine_ctl)
                df_ctl.rename(columns={list(df_ctl)[0]: "z", list(df_ctl)[1]: "y"}, inplace=True)

                dy = -df_ctl.iloc[:, [1]]
                dy_p = [float(dy.iloc[i]) for i in range(len(dy))]
                r1 = -df_rIL["r"] + dy["y"] / 2
                r2 = df_rIL["r"] + dy["y"] / 2
                z = df_rIL["z"]

                # dodatak za plotanje L po sredini
                L = {"r": [], "z": []}
                for i in range(len(r2)):
                    if (r2[i] - r1[i]) > (r2[0] - r1[0]) * 1.05:
                        L["r"].append(dy_p[i])
                        L["z"].append(df_rIL["z"][i])


            def onePlot():
                plt.grid(color='k', linestyle=':', linewidth=0.5)
                plt.plot(r1, z, c="k")
                plt.plot(r2, z, c="k", label="Inner\ncontours")
                plt.plot(dy, z, c="r", linestyle='dashed', linewidth=1, label="Centerline")
                plt.plot(L["r"], L["z"], c="blue", label="L", linewidth=1.5)
                plt.xlim(-70, 60)
                plt.ylim(0, 350)

                # plt.title("Outer contour curves")
                plt.xlabel("Coordinate $x$ [mm]")
                plt.ylabel("Coordinate $z$ [mm]")
                plt.legend(framealpha=1)
                # plt.subplots_adjust(left=0.2)
                fig = plt.gcf()
                plt.grid(color='k', linestyle=':', linewidth=0.5)
                plt.legend()
                plt.pause(1)
                plt.draw()
                plt.close()
                fig.savefig(contoursFolder + allNames[n] + "_" + str(chosenTSContours[nTS])  + '.png', dpi=300)

            onePlot()


PlotAllCont()