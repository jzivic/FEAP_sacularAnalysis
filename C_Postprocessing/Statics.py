"""
Statistical analysis of all data: count, mean and r value, variance, min, max..
Write all to .xlsx file
"""

import pandas as pd
from scipy.stats import linregress
from A_Preprocessing.SimulationsData import *
from PlotParameters import chosenData


def CalculateStatistic():
    statData = pd.DataFrame(round(chosenData.describe(),3))

    # r value from linear regression, calculated for every value over value P
    rValueDict = {value:linregress(chosenData[value],  chosenData["RPI"]).rvalue for value in chosenData if value!="Flag"}
    df_rValue = pd.DataFrame(rValueDict, index=["rValue"])                  #converting to DataFrame

    varianceDict = {value:chosenData[value].var() for value in chosenData if value!="Flag"}
    df_variance = pd.DataFrame(varianceDict, index=["variance"])

    statData = pd.concat([statData,df_variance, df_rValue])                 # connecting to one DataFrame
    statData.to_excel(statXlsx)                                             # write to xlsx file


# CalculateStatistic()