# FEAP_sacularAnalysis

In the A_Prerocessing̣->SimulationsData resultsDir has to be specified. Within all other directories will be automatically made

Subrutines made to analyize many FEAP simulations: when ended, all simulation results are stored in notepad documents in different direcories. 
Analysis pogram is diveded into 3 parts thas has to be run (Assembing+A/B/C):

1) A_Prerocessing:
  - Select sonditions, wanted Timesteps for analysis and contor plotting, direcotry and pickle names..  
  - Iterates over the main directory,gets all simulation names and paths from several different subfolders at different levels. 
  - Extract data for every simulation: With several conditions, for selected timesteps from several different files in each simulation directory.
  - Store data to pickle container 
  
2) B_ParameterCombinations:
  - Calculate known derived parameters out of basic
  - Make more than 50000 new (unknown) parameters; Every possible combination up to 3rd power using basic parameters 
  - Calculate the r value and sort parameters by condition. 
  - Write everything to Excel document
  
3) C_Postprocessing:
  - Plot outer contours for all aneurysms
  - Plot paper ready diagrams for selected parameters
  - Make statistical analysis and write it to Excel document
