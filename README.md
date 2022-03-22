# Triboson Topologies Experimental Sensitivity Analysis Code
## Author
- [Jesus Manuel Caridad Ramirez](https://github.com/JCaridad108)

## Paper: High-Energy Physics – Phenomenology
* [New physics in triboson event topologies](https://arxiv.org/abs/2112.00137)
* **Abstract**: We present a study of the sensitivity to models of new physics of proton collisions resulting in three electroweak bosons. As a benchmark, we analyze models in which an exotic scalar field ϕ is produced in association with a gauge boson (V=γ or Z). The scalar then decays to a pair of bosons, giving the process pp→ϕV→V′V″V. We interpret our results in a set of effective field theories where the exotic scalar fields couple to the Standard Model through pairs of electroweak gauge bosons. We estimate the sensitivity of the LHC and HL-LHC datasets and find sensitivity to cross sections in the 10 fb -- 0.5 fb range, corresponding to scalar masses of 500 GeV to 2 TeV and effective operator coefficients up to 35 TeV.

## Reconstruction Analysis
The ReconstructionAnalysis directory contains scripts used for reading 
generated Monte Carlo simulated background and signal (500, 1000, 1500, 2000 GeV) 
data (MadGraph+Pythia+Delphes) and reconstructing events according to the 
specified topology. 

## Statistical Analysis
The StatisticalAnalysis directory contains scripts that use the reconstructed 
event data and perform upper-limit calculations on the cross sections using the 
CLs technique with pyhf. Calculations are performed for integrated luminosities
100 fb^-1 and 3000 fb^-1.

* [pyhf repo](https://github.com/scikit-hep/pyhf) : https://github.com/scikit-hep/pyhf

## Histograms
The GenerateHistograms directory contains scripts that normalize signal and 
background histograms to their appropriate yield and output them as PDFs. 
There is also a script that uses the scale factors calculated with the 
Statistical Analysis code to scale the cross-section and plot the stacked
yield-normalized signal and background histograms. These stacked histograms 
are shown in the paper. 

## Plots
The GeneratePlots directory contains scripts that plot the cross-section 
upper-limits calculated by the Statistical Analysis code. It also creates a 
summary plot that plots many topologies together for comparison. These plots 
are also shown in the paper.

## Main Analysis File
The TopologyAnalysis_main.py file is an example of an instruction file containing
all the configurations required for an analysis. The sample file contains
configurations for a 1 photon, 2 large-R jet final state. 
