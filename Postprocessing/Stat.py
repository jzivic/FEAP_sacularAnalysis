import pandas as pd

from scipy.stats import linregress
from Preprocessing.SimulationsData import *

abData = pd.read_pickle(PickleData_ab)
cData = pd.read_pickle(PickleData_c)
allData = pd.read_pickle(PickleData_all)

chosenData = abData

statData = pd.DataFrame(round(abData.describe(),3))

rValueDict = {value:linregress(chosenData[value],  chosenData["P"]).rvalue for value in chosenData if value!="Flag"}
df_rValue = pd.DataFrame(rValueDict, index=["rValue"])

varianceDict = {value:chosenData[value].var() for value in chosenData if value!="Flag"}
df_variance = pd.DataFrame(varianceDict, index=["variance"])



statData = pd.concat([statData,df_variance, df_rValue])
statData.to_excel(statXlsx)



# var = { ime:[vel] for ime,vel in zip(sveVelicine.columns,sveVelicine.var())}