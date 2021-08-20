"""
TimeSteps, dir and data names, critical values are selected here:
   -simulation Dir
   - chosen TimeSteps


"""

resultsDir = "/home/josip/feap/pocetak/parametarskaAnalizaSve/rezultati/sakularna/"   #path to analysis dir





# A_Preprocessing:
chosenTSContours = [-50, -30, -10]
chosenTimeSteps = [190, 208, 226, 244, 262, 280, 298, 316, 334, 352, 370, 388, 406, 424, 442, 460, 478]
allSimulationsAnalysis = True
sameInitalRadius = False


analysisDir = resultsDir + "analysisData/"
PickleData_basic = analysisDir+"SacularData_basic.pickle"                       # just read parameters
picklesDir = analysisDir + ("pickles/")





# B_ParameterCombinations:
flagVersion = "v2"                                 # flag condition version
assert flagVersion in ["v1", "v2"], "Unknown version"

if flagVersion=="v1":
    chosenFlag = "AB"
elif flagVersion=="v2":
    chosenFlag = "A"

# Data for v1: RPI = strenght/sigmaCritical=const
sigmaCritical = 1000
flagCondition_1 = {"S22":{"A-B":500, "B-C":sigmaCritical}, "GR":{"A-B":5, "B-C":10}, "D":55}
S22_condition = False
# Data for v2: RPI = strenght/S_resist
RPI_condition = 1.2
D_condition = True
flagCondition_2 = {"D":60}

sortingKey = "rAvg"                                # rAvg, r_d0, r_d1, r_d2, r_d3
nBestParams = 10

paramCombDir = analysisDir + ("paramComb/")
PickleData_all = picklesDir+"SacularData_all.pickle"                           # derived parameters (A+B+C)
PickleData_A = picklesDir+"SacularData_A.pickle"     #novo
PickleData_AB = picklesDir+"SacularData_AB.pickle"
PickleData_C = picklesDir+"SacularData_C.pickle"
PickleParamCombinations = picklesDir + "ParametersCombinations.pickle"
paramXlsx = paramCombDir + "paramData.xlsx"






# C)  C_Postprocessing:
diagramsDir = analysisDir + ("diagrams/")
contoursDir = analysisDir + ("contours/")
statXlsx = analysisDir + "statData.xlsx"





