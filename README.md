# FEAP_sacularAnalysis


Python scripts made to analyze FEAP simulations. 

Input simulations and processed output data are stored at: https://drive.google.com/drive/folders/13ZakNl0kf7Y5AIffglaOynaulLBCIVw-?usp=sharing.
When finished, all FEAP simulation results are stored in notepad documents in several different (sub)direcories. 
Analysis pogram is diveded into 3 parts that have to be run (Assembing+A/B/C) separately:

In the A_Preprocessing̣->SimulationsData: resultsDir has to be specified(uploaded to drive⨪>inputData). 
1) A_Preprocessing:
  - Select conditions, wanted Timesteps for analysis and contour plotting, direcotry and pickle names.
  - Iterates over the main directory, gets all simulation names and paths from several different subfolders at different levels. 
  - Extract data for every simulation: With several conditions, for selected timesteps from several different files in each simulation directory.
  - Store data to pickle container .
  
  
2) B_ParameterCombinations:
  - Calculate known derived parameters out of basic parameters.
  - Make more than 50000 new (unknown) parameters; Every possible combination up to 3rd power using basic parameters.
  - Calculate the r value and sort parameters by condition. 
  - Write everything to Excel document.
  
  
3) C_Postprocessing:
  - Plot outer contours for all aneurysms
  - Plot paper ready diagrams for selected parameters
  - Make statistical analysis and write it to Excel document
