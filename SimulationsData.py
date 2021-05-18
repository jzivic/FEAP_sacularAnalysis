# analizaTS = False
# analizaD = True


# parametarskaAnaliza = "parametarskaAnalizaPojedinacna"
parametarskaAnaliza="parametarskaAnaliza_2"
# parametarskaAnaliza = "parametarskaAnalizaSve"


folder1 = "r="

# chosenTimeSteps = [190, 208, 226, 244, 262, 280, 298, 316, 334, 352, 370, 388, 406, 424, 442, 460, 478]
# chosenTimeSteps = [190, 220,280, 316, 350]
# chosenTimeSteps = [222, 300]
chosenTimeSteps = [-1]


analizaSvihSimulacija = True
istiPocetniRadijus = False
plotanjeKonture = False


sigmaKriticno = 1000
popisNastavaka = ["101-2", "102-3"]

uvjetFlagova = {"S22":[500, 800], "GR":[5, 10], "D":45}




#################################################################################

parametarskaAnaliza="parametarskaAnaliza_2"




allSimulationsAnalysis = False

sameInitalRadius = False


sigmaCritical = 1000
TSLeght = 51
suffixList = ["101-2", "102-3"]

flagCondition = {"S22":[500, 800], "GR":[5, 10], "D":45}













"""
/home/josip/PycharmProjects/racunanjeFEAP/venv/bin/python /home/josip/PycharmProjects/racunanjeFEAP/racunanjeSakularna/sklapanjeAnalizeSakularne.py
Traceback (most recent call last):
  File "/home/josip/PycharmProjects/racunanjeFEAP/racunanjeSakularna/sklapanjeAnalizeSakularne.py", line 332, in <module>
    SakularnaFunkcija_TS()
  File "/home/josip/PycharmProjects/racunanjeFEAP/racunanjeSakularna/sklapanjeAnalizeSakularne.py", line 81, in SakularnaFunkcija_TS
    simulacija_TS = SakularnaAnaliza_TS(rezultatiFolder, i)  # simulacija_TS je objekt koji ima sve izračunato za tu simulaciju u sebi
  File "/home/josip/PycharmProjects/racunanjeFEAP/racunanjeSakularna/RacunanjeSakularna.py", line 49, in __init__
    if self.ProvjeraNastankaAAA()==False: #provjerava jel nastala AAA
  File "/home/josip/PycharmProjects/racunanjeFEAP/racunanjeSakularna/RacunanjeSakularna.py", line 181, in ProvjeraNastankaAAA
    self.D0 = (float(self.cijeli_tekst_rIL[self.startniRed_rIL].strip().split()[0]) +
AttributeError: 'SakularnaAnaliza_TS' object has no attribute 'cijeli_tekst_rIL'

Process finished with exit code 1

"""