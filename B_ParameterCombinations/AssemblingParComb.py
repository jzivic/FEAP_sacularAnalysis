from A_Preprocessing.SimulationsData import *


from DerivedParameters_v1 import DerivedParameters_v1, MakeDir_pickles
from DerivedParameters_v2 import DerivedParameters_v2, MakeDir_pickles


MakeDir_pickles()
if flagVersion == "v1":
    DerivedParameters_v1(PickleData_basic)
elif flagVersion == "v2":
    DerivedParameters_v2(PickleData_basic)



from MakeCombinations import MakeCombinations
if flagVersion == "v1":
    MakeCombinations(PickleData_AB)
elif flagVersion == "v2":
    MakeCombinations(PickleData_A)


from CombinationAnalysis import MakeDir_combParam, CombinationAnalysis
MakeDir_combParam()
if flagVersion == "v1":
    CombinationAnalysis(PickleData_AB,sortingKey, nBestParams)
elif flagVersion == "v2":
    CombinationAnalysis(PickleData_A,sortingKey, nBestParams)




