from A_Preprocessing.SimulationsData import *


from DerivedParameters_v1 import DerivedParameters_f1, MakeDir_pickles
from DerivedParameters_v2 import DerivedParameters_f2, MakeDir_pickles


MakeDir_pickles()

if flagVersion == "v1":
    DerivedParameters_f1(PickleData_basic)
elif flagVersion == "v2":
    DerivedParameters_f2(PickleData_basic)



from MakeCombinations import MakeCombinations
MakeCombinations(PickleData_AB)
if chosenFlag == "A":
    MakeCombinations(PickleData_A)
elif chosenFlag == "AB":
    MakeCombinations(PickleData_AB)


from CombinationAnalysis import MakeDir_combParam, CombinationAnalysis
MakeDir_combParam()
CombinationAnalysis(sortingKey, nBestParams)




