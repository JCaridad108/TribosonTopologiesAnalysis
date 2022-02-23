import sys
sys.path.append('/Applications/root_v6.20.04/lib')
import ROOT
import array

"""
Create a TGraph line graph using the crossx_limits.txt values
	output by stat analysis code.
"""
crossx_file = open('crossx_limits.txt', 'r')
crossx_limits = []

for x in crossx_file.read().split('\n'):
    if len(x) > 1:
        crossx_limits.append(float(x))
crossx_file.close() # FIXME: This better not break it

crossx_lim_array = array.array('d', crossx_limits)
mass_array = array.array('d', [500, 1000, 1500, 2000])

crossx_plot = ROOT.TGraph(4, mass_array, crossx_lim_array)
crossx_plot.SetMarkerStyle(25)
crossx_plot.SetTitle('')
crossx_plot.GetXaxis().SetTitle('m_{XX}[GeV]')
crossx_plot.GetYaxis().SetTitle('Limit #sigma (pb)')
#crossx_plot.SetMinimum(-0.0005)


canvas = ROOT.TCanvas()
#canvas.SetLogy()
crossx_plot.Draw()
canvas.Print('crossx.tex')

#canvas = ROOT.TCanvas()
#crossx_plot.Draw()
#canvas.Print('crossx_limits.pdf')

