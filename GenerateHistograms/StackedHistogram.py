import sys
sys.path.append('/Applications/root_v6.20.04/lib')
import ROOT
## visual.py
### CHANGE FILE PATHS FOR DIFFERENT FILES ###
"""
Used to create stacked histograms in EXPERIMENTAL SENSITIVITY section of:
	https://arxiv.org/pdf/2112.00137.pdf
"""
# Opening root files outputted by main code, create legend and canvas
sig_file = ROOT.TFile.Open('2pho1fatjet_sig_histo_file.root')
bkg_file = ROOT.TFile.Open('2pho1fatjet_bkg.root')
legend = ROOT.TLegend(0.7, 0.7, 0.98, 0.95)
canvas = ROOT.TCanvas()

# Get-ing signal histograms from signal .root file and creating copies (clones) of them because ROOT sucks
sig_histo500, sig_histo1000, sig_histo1500, sig_histo2000 = sig_file.Get(';2').Clone(), sig_file.Get(';1').Clone(), \
                                                            sig_file.Get(';3').Clone(), sig_file.Get(';4').Clone()

# Scaling the signals to their corresponding scale-factors
sig_histo500.Scale(144)
sig_histo1000.Scale(6.11)
sig_histo1500.Scale(4.16)
sig_histo2000.Scale(3.6)

# Get-ing background histogram from bkg .root file and creating clone. Setting line and fill color
bkg_histo = bkg_file.Get('XX Mass Background;1').Clone()
bkg_histo.SetLineColor(11)
bkg_histo.SetFillColor(11)


# Printing integrals of histograms
print 'sig1:', sig_histo500.Integral()
print 'sig2:', sig_histo1000.Integral()
print 'sig3:', sig_histo1500.Integral()
print 'sig4:', sig_histo2000.Integral()
print 'bkg:', bkg_histo.Integral()

# Adding the histograms to the legend, including XS's
legend.AddEntry(sig_histo500, 'm_{XX}=500; #sigma=0.01380 pb')
legend.AddEntry(sig_histo1000, 'm_{XX}=1000; #sigma=6.5927e-04 pb')
legend.AddEntry(sig_histo1500, 'm_{XX}=1500; #sigma=3.3696e-04 pb')
legend.AddEntry(sig_histo2000, 'm_{XX}=2000; #sigma=1.8504e-04 pb')
legend.AddEntry(bkg_histo, '#gamma+#gamma')
legend.SetBorderSize(0)

# Drawing histograms and legend
bkg_histo.Draw('HISTO')
sig_histo500.Draw('HISTO SAME')
sig_histo1000.Draw('HISTO SAME')
sig_histo1500.Draw('HISTO SAME')
sig_histo2000.Draw('HISTO SAME')

bkg_histo.SetMinimum(1)

legend.Draw()

canvas.SetLogy()
canvas.Print('visual.tex')
sig_file.Close()
bkg_file.Close()
