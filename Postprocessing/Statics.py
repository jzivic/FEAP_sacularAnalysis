import openpyxl
import pandas as pd

from scipy.stats import linregress
from Preprocessing.SimulationsData import *
from PlotParameters import chosenData


# abData = pd.read_pickle(PickleData_AB)
# cData = pd.read_pickle(PickleData_C)
# allData = pd.read_pickle(PickleData_all)



def CalculateStatistic():
    statData = pd.DataFrame(round(chosenData.describe(),3))               #

    # r value from linear regression, calculated for every value over value P
    rValueDict = {value:linregress(chosenData[value],  chosenData["P"]).rvalue for value in chosenData if value!="Flag"}
    df_rValue = pd.DataFrame(rValueDict, index=["rValue"])                  #converting to DataFrame

    varianceDict = {value:chosenData[value].var() for value in chosenData if value!="Flag"}
    df_variance = pd.DataFrame(varianceDict, index=["variance"])


    statData = pd.concat([statData,df_variance, df_rValue])
    statData.to_excel(statXlsx)



# var = { ime:[vel] for ime,vel in zip(sveVelicine.columns,sveVelicine.var())}