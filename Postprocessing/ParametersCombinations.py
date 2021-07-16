import pandas as pd
from scipy.stats import linregress
from matplotlib import pyplot as plt
from Preprocessing.SimulationsData import *



ABData = pd.read_pickle(PickleData_AB)







range_1 = [-3,-2,-1, 0, 1,2,3]
range_12 = [-3,-2,-1, 1,2,3]

# range_2 = [1,2]
range_2 = [1,2,4]


allCoeffs = {"coeffName":[], "r_d0":[], "coeffDict":[]}
goodCoeffs = {"coeffName":[], "r_d0":[], "r_d1":[], "r_d2":[], "r_d3":[], "coeffDict":[]}



def Calculate_rValue(inputPickle):
    P = inputPickle["P"]
    L = inputPickle["L"]
    D = inputPickle["D"]
    d0 = inputPickle["d0"]
    d1 = inputPickle["d1"]
    d2 = inputPickle["d2"]
    d3 = inputPickle["d3"]

    dSvi = [d0, d1, d2, d3]
    
    
    
    for iL in range_1:
        for jD in range_1:
            for kd in range_1:
                # for lDd in range_12:
                for mD_d in range_1:
                    for N in range_2:
    
    
                        parameter = L**iL * D**jD * dSvi[0]**kd * (N*D**mD_d-dSvi[0]**mD_d)
    
                        slope, intercept, rValue, pValue, se = linregress(parameter, P)
    
                        coeffName = "iL="+str(iL)+" jD="+str(jD)+" kd="+str(kd)+" mD_d="+str(mD_d)+" N="+str(N)
                        coeffName_Dict = {"iL": iL, "jD":jD, "kd": kd, "mD_d":mD_d, "N":N}
    
            
                        allCoeffs["coeffName"].append(coeffName)
                        allCoeffs["r_d0"].append(rValue)
                        allCoeffs["coeffDict"].append(coeffName_Dict)
    
                        df_all = pd.DataFrame(allCoeffs)
    
    
    
                        if abs(rValue) > 0.85:
    
                            goodCoeffs["coeffName"].append(coeffName)
                            goodCoeffs["r_d0"].append(rValue)
                            goodCoeffs["coeffDict"].append(coeffName_Dict)
    
                            rSvi = []
                            for i in range(1,len(dSvi)):
                                parameterGood = L ** iL * D ** jD * dSvi[0] ** kd * (N * D ** mD_d - dSvi[0] ** mD_d)
                                slope, intercept, rValue, pValue, se = linregress(parameterGood, P)
                                rSvi.append(rValue)
    
    
                            goodCoeffs["r_d1"].append(rSvi[1-1])
                            goodCoeffs["r_d2"].append(rSvi[2-1])
                            goodCoeffs["r_d3"].append(rSvi[3-1])



    df_good = pd.DataFrame(goodCoeffs)

    goodCoeffs["rSuma"] = (goodCoeffs["r_d0"] + goodCoeffs["r_d1"] + goodCoeffs["r_d2"] + goodCoeffs["r_d3"])

    df_all.to_pickle(ParametersCombinations_all)
    df_good.to_pickle(ParametersCombinations_good)



# Calculate_rValue(ABData)












class ParameterCombinations:
    def __init__(self, inputPickle):

        self.inputData = pd.read_pickle(inputPickle)

        self.SetCase()
        self.Calculate_rValue()



    def SetCase(self):
        self.range_1 = [-3, -2, -1, 0, 1, 2, 3]
        self.range_12 = [-3, -2, -1, 1, 2, 3]
        self.range_2 = [1, 2, 4]

        self.allCoeffs = {"coeffName":[], "r_d0":[], "coeffDict":[]}
        self.goodCoeffs = {"coeffName":[], "r_d0":[], "r_d1":[], "r_d2":[], "r_d3":[], "coeffDict":[]}


        self.P = self.inputData["P"]
        self.L = self.inputData["L"]
        self.D = self.inputData["D"]

        d0 = self.inputData["d0"]
        d1 = self.inputData["d1"]
        d2 = self.inputData["d2"]
        d3 = self.inputData["d3"]

        self.dSvi = [d0, d1, d2, d3]



    def Calculate_rValue(self):

        for iL in range_1:
            for jD in range_1:
                for kd in range_1:
                    # for lDd in range_12:
                    for mD_d in range_1:
                        for N in range_2:

                            parameter = self.L ** iL * self.D ** jD * self.dSvi[0] ** kd * (N * self.D ** mD_d - self.dSvi[0] ** mD_d)
                            slope, intercept, rValue, pValue, se = linregress(parameter, self.P)

                            coeffName = "iL=" + str(iL) + " jD=" + str(jD) + " kd=" + str(kd) + " mD_d=" + str(
                                        mD_d) + " N=" + str(N)
                            coeffName_Dict = {"iL": iL, "jD": jD, "kd": kd, "mD_d": mD_d, "N": N}

                            allCoeffs["coeffName"].append(coeffName)
                            allCoeffs["r_d0"].append(rValue)
                            allCoeffs["coeffDict"].append(coeffName_Dict)

                            if abs(rValue) > 0.85:
                                goodCoeffs["coeffName"].append(coeffName)
                                goodCoeffs["r_d0"].append(rValue)
                                goodCoeffs["coeffDict"].append(coeffName_Dict)

                                rSvi = []
                                for i in range(1, len(self.dSvi)):
                                    parameterGood = self.L ** iL * self.D ** jD * self.dSvi[i] ** kd * (
                                                N * self.D ** mD_d - self.dSvi[i] ** mD_d)

                                    slope, intercept, rValue, pValue, se = linregress(parameterGood, self.P)
                                    rSvi.append(rValue)

                                goodCoeffs["r_d1"].append(rSvi[1 - 1])
                                goodCoeffs["r_d2"].append(rSvi[2 - 1])
                                goodCoeffs["r_d3"].append(rSvi[3 - 1])


        df_all = pd.DataFrame(allCoeffs)
        df_all.to_pickle(ParametersCombinations_all)

        goodCoeffs["rSuma"] = goodCoeffs["r_d0"] + goodCoeffs["r_d1"] + goodCoeffs["r_d2"] + goodCoeffs["r_d3"]
        df_good = pd.DataFrame(goodCoeffs)

        df_good.to_pickle(ParametersCombinations_good)




    def DataProcesing(self):
        3





ParameterCombinations(PickleData_AB)






