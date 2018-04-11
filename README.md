Analyzer to process PhaseII VBFHbb MiniAOD samples for upgrade studies. 

Instructions to check out code and run:
Set up CMSSW area:
```
setenv SCRAM_ARCH slc6_amd64_gcc630
cmsrel CMSSW_9_3_7
cd CMSSW_9_3_7/src
cmsenv
```
Check out code:
```
git clone https://github.com/ZohebAbai/Upgrades-VBFAnalyzer.git
```
Put you `MiniAod.root` file inside `test` folder.

Compile:
```
cd Upgrades/VBFAnalyzer
scramv1 b -k -j8
```
To run:
```
cd test
cmsRun runAnalysisRD.py
```
The output is a ROOT file containing a TTree.


```
cd ../macros/
In VBF_M125_PU0.txt, copy paste the address of the above produces ROOT file. 
EDIT analyze.py as required for your analysis.

python analyze.py
```
This will create a ROOT file named as `VBF_M125_PU0.root` containing plots.
It will also mention the efficiency of your signal samples.
```
EDIT plot.py as required.

python plot.py

```
This shall produce the required plots.
