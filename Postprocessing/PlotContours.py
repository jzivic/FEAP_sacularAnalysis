"""
Plot all countours in a loop for chosen TimeSteps.
Saves pictures to dir

"""

import shutil, os
import pandas as pd
import matplotlib.pyplot as plt

from Preprocessing.SimulationsData import *
from Preprocessing.DirectorySearch import DirectorySearch

# Make "contours" dir to save contour pictures
def MakeDir_contours():
    try:
        shutil.rmtree(contoursDir)
    except: FileNotFoundError
    os.mkdir(contoursDir)

MakeDir_contours()


allPath = DirectorySearch(resultsDir).allPaths
allNames = DirectorySearch(resultsDir).allNames



# Function to plot all contours at chosen TimeSteps in a loop
def PlotAllContours():

    for n in range(len(allPath)):
        os.chdir(allPath[n])

        nl_rIL = sum(1 for line in open("res__INNER_lines__101-2"))     # total number of lines in res__INNER_lines__101 .txt file
        nl_ctl = sum(1 for line in open("res__CENTERLINE__101-2"))
        cut_rIL = [i for i in range(nl_rIL)]                            # copy of lines indices to be excluded
        cut_ctl = [i for i in range(nl_ctl)]

        #Iterate over chosen TimeSteps in each simulation
        for nTS in range(len(chosenTSContours)):

            # Set the rIL file
            startLine_rIL = -2 + (TSLeght+1) * chosenTSContours[nTS] + nl_rIL
            chosenL_rIL = [i for i in range(startLine_rIL, (startLine_rIL + TSLeght + 1))]      # actually used lines indices
            rmLine_rIL = list(cut_rIL)                                                          # lines to be removed
            for i in chosenL_rIL:                                                               # leave only lines that has to be deleted
                rmLine_rIL.remove(i)
            df_rIL = pd.read_csv("res__INNER_lines__101-2", sep='    ', skiprows=rmLine_rIL)    # create DataFrame from rIL, only needed lines
            df_rIL.rename(columns={list(df_rIL)[1]: "r", list(df_rIL)[4]: "z"}, inplace=True)   # (re)name the columns


            # Set the ctl file
            startLine_ctl = -2 + (TSLeght+1) * chosenTSContours[nTS] + nl_ctl
            chosenL_ctl = [i for i in range(startLine_ctl, (startLine_ctl + TSLeght + 1))]
            rmLine_ctl = list(cut_ctl)
            for i in chosenL_ctl:
                rmLine_ctl.remove(i)
            df_ctl = pd.read_csv("res__CENTERLINE__101-2", sep='     ', skiprows=rmLine_ctl)
            df_ctl.rename(columns={list(df_ctl)[0]: "z", list(df_ctl)[1]: "y"}, inplace=True)


            dy = -df_ctl.iloc[:, [1]]                                                       # offstet from centerline
            dyList = [float(dy.iloc[i]) for i in range(len(dy))]                            # list of dy data

            r1 = -df_rIL["r"] + dy["y"] / 2                                                 # left radius
            r2 = df_rIL["r"] + dy["y"] / 2                                                  # left radius
            z = df_rIL["z"]                                                                 # height
            L = {"r": [], "z": []}                                                          # data for L, contains "r" and "z" data

            for i in range(len(r2)):
                if (r2[i] - r1[i]) > (r2[0] - r1[0]) * 1.05:                                # AAA definition condition
                    L["r"].append(dyList[i])
                    L["z"].append(df_rIL["z"][i])


            def onePlot():
                plt.grid(color='k', linestyle=':', linewidth=0.5)
                plt.plot(r1, z, c="k")
                plt.plot(r2, z, c="k", label="Inner\ncontours")
                plt.plot(dy, z, c="r", linestyle='dashed', linewidth=1, label="Centerline")
                plt.plot(L["r"], L["z"], c="blue", label="L", linewidth=1.5)
                plt.xlim(-70, 60)
                plt.ylim(0, 350)

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
                fig.savefig(contoursDir + allNames[n] + " " + str(chosenTSContours[nTS])  + '.png', dpi=300)
            onePlot()

# PlotAllContours()