"""
Everything is chosen from here:
   -simulation Dir
   - chosen TimeSteps


"""

# parametarskaAnaliza = "parametarskaAnalizaPojedinacna"
# parametarskaAnaliza="parametarskaAnaliza_2"
parametarskaAnaliza = "parametarskaAnalizaSve"


# chosenTimeSteps = [190, 208, 226, 244, 262, 280, 298, 316, 334, 352, 370, 388, 406, 424, 442, 460, 478]
chosenTimeSteps = [333,  666, ]

chosenTSContours = [-50, -30, -10]

#################################################################################




allSimulationsAnalysis = True                      # if allSimulationsAnalysis==False: only one listed sim will be analyses
sameInitalRadius = False
sigmaCritical = 1000
TSLeght = 51
suffixList = ["101-2", "102-3"]
flagCondition = {"S22":[500, 800], "GR":[5, 10], "D":45}


resultsDir = "/home/josip/feap/pocetak/"+parametarskaAnaliza+"/rezultati/sakularna"                          #path to analysis dir

analysisDir = resultsDir + "/analysisData/"
diagramsDir = analysisDir + ("diagrams/")
contoursDir = analysisDir + ("contours/")

PickleData_basic = analysisDir+"SacularData_basic.pickle"                       # just read parameters
PickleData_all = analysisDir+"SacularData_all.pickle"                           # derived parameters (A+B+C)
PickleData_AB = analysisDir+"SacularData_ab.pickle"
PickleData_C = analysisDir+"SacularData_c.pickle"
statXlsx = analysisDir + "statData.xlsx"




