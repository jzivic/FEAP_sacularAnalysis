"""
TimeSteps, dir and data names, critical values are selected here:
   -simulation Dir
   - chosen TimeSteps


"""


parametarskaAnaliza = "parametarskaAnalizaSve"              # main dir with results


chosenTSContours = [-50, -30, -10]                          # contours drawn at these TS
chosenTimeSteps = [190, 208, 226, 244, 262, 280, 298, 316, 334, 352, 370, 388, 406, 424, 442, 460, 478] # TS analyzed

#################################################################################




allSimulationsAnalysis = True                      # if allSimulationsAnalysis==False: only one listed sim will be analyses
sameInitalRadius = False
sigmaCritical = 800
chosenFlag = "AB"                                  # "AB" or "C" or "all

flagCondition = {"S22":{"A-B":500, "B-C":sigmaCritical}, "GR":{"A-B":5, "B-C":10}, "D":55}



resultsDir = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna/"                          #path to analysis dir

analysisDir = resultsDir + "analysisData/"
diagramsDir = analysisDir + ("diagrams/")
contoursDir = analysisDir + ("contours/")
picklesDir = analysisDir + ("pickles/")

paramCombDir = analysisDir + ("paramComb/")


PickleData_basic = analysisDir+"SacularData_basic.pickle"                       # just read parameters

PickleData_all = picklesDir+"SacularData_all.pickle"                           # derived parameters (A+B+C)
PickleData_AB = picklesDir+"SacularData_AB.pickle"
PickleData_C = picklesDir+"SacularData_C.pickle"

PickleParamCombinations = picklesDir + "ParametersCombinations.pickle"

statXlsx = analysisDir + "statData.xlsx"
paramXlsx = paramCombDir + "paramData.xlsx"







