import sys
sys.path.append('/Applications/root_v6.20.04/lib')
import ROOT
import array

# Create mega-plot that contains all cross-section upper-limits

# NOTE: xs_dic is of form {'zxx>zzz> 4muons 1 fat jet': path}

def xs_mega_plot_original(xs_dic, file_name):
    canvas = ROOT.TCanvas()
    mg = ROOT.TMultiGraph(); mg.SetTitle("; m[GeV]; Limit #sigma (pb)")
    legend = ROOT.TLegend(0.85, 0.7, 0.99, 0.98)
    plot_list = []
    color_count = 1
    for plot in xs_dic:
        crossx_file = open(xs_dic[plot], 'r')
        crossx_limits = [float(x) for x in crossx_file.read().split('\n') if len(x) > 1]

        crossx_lim_array = array.array('d', crossx_limits)
        mass_array = array.array('d', [500, 1000, 1500, 2000])

        crossx_plot = ROOT.TGraph(4, mass_array, crossx_lim_array)

        crossx_plot.SetLineWidth(2)
        crossx_plot.SetMarkerStyle(25); crossx_plot.SetMarkerSize(0.5)
        crossx_plot.SetTitle('')
        crossx_plot.GetXaxis().SetTitle('m[GeV]')
        crossx_plot.GetYaxis().SetTitle('Limit #sigma (pb)')

        if color_count == 10:
            color_count += 1

        crossx_plot.SetLineColor(color_count); color_count += 1

        legend.AddEntry(crossx_plot, plot)
        plot_list.append(crossx_plot)
        crossx_file.close()
    for p in plot_list:
        mg.Add(p)
    mg.Draw("ALP")
    legend.Draw()
    canvas.SetLogy()
    canvas.Print(file_name)
    #return canvas

def to_decimal(numb):
    if "E" in numb:
        ex = int(numb.split('E')[1][-1])
        ints = numb.split('E')[0].split('.')[0] + numb.split('E')[0].split('.')[1]
        final = '0.' + '0'*(ex-1) + ints
    else:
        final = numb
    #print(final)
    return float(final)

def xs_mega_plot(xs_dic, file_name):
	canvas = ROOT.TCanvas()
	mg = ROOT.TMultiGraph(); mg.SetTitle("; m_{\phi}[GeV]; Limit #sigma [pb]");# ROOT.gStyle.SetTitleAlign(22)
	#MODIFY MULTIGRAPH
	#mg.GetXaxis().SetTitleSize(0.7); mg.GetXaxis().SetLabelSize(0.6)
	#mg.GetYaxis().SetTitleSize(0.7); mg.GetYaxis().SetLabelSize(0.6)
	#legend = ROOT.TLegend(0.79, 0.62, 0.99, 0.98) #MegaPlot1
	legend = ROOT.TLegend(0.547, 0.36, 0.91, 0.99)  # MegaPlot2;
	legend.SetBorderSize(0)#; legend.SetFillStyle(0)
	legend.SetTextSize(0.05)
	tgraph_list = []
	for plot in xs_dic:
		crossx_file = open(xs_dic[plot], 'r')
		crossx_limits = [to_decimal(x) for x in crossx_file.read().split('\n') if len(x) > 1]
		crossx_mean = sum(crossx_limits)/len(crossx_limits)
		crossx_lim_array = array.array('d', crossx_limits)
		mass_array = array.array('d', [500, 1000, 1500, 2000])

		crossx_plot = ROOT.TGraph(4, mass_array, crossx_lim_array)

		crossx_plot.SetLineWidth(3); crossx_plot.SetMarkerStyle(25); crossx_plot.SetMarkerSize(0.5)

		#if color_count == 10:
		#    color_count += 1

		#crossx_plot.SetLineColor(color_count); color_count += 1
		#legend.AddEntry(crossx_plot, plot)

		tgraph_list.append((crossx_mean, crossx_plot, plot))
		crossx_file.close()
    #color_count = 14    #MegaPlot1
    #color_count = 16  # MegaPlot2
	color_list = [1, 2, 3, 4, 6, 8, 9, 28, 30, 38, 41, 42, 46, 7]
	color_count = len(color_list)-1
	for p in sorted(tgraph_list, reverse=True):
		p[1].SetLineColor(color_list[color_count]); color_count -= 1
		legend.AddEntry(p[1], p[2], 'l')
		mg.Add(p[1])
        #if color_count in [10, 5]:
        #    color_count -= 1
		#p[1].SetLineColor(color_list[color_count]); color_count -= 1
        #legend.AddEntry(p[1], p[2])
        #mg.Add(p[1])
	print(color_count)
	# MODIFY MULTIHRAPH
	mg.GetXaxis().SetTitleSize(0.055); mg.GetXaxis().SetLabelSize(0.06)
	mg.GetYaxis().SetTitleSize(0.055); mg.GetYaxis().SetLabelSize(0.06)
	
	# lumi text 
	lumi = ROOT.TLatex(550, 1.5, "L=100 fb^{-1}")

	mg.SetMaximum(1); mg.SetMinimum(0.00002)
	mg.Draw("ALP")
	legend.Draw(); lumi.Draw()
	canvas.SetLogy()
	canvas.SetBottomMargin(0.12); canvas.SetLeftMargin(0.15); canvas.SetTopMargin(1)
	#canvas.BuildLegend()
	canvas.Print(file_name)

if __name__ == '__main__':
	# Code in triple-quotes are previous file-collections that were plotted
	'''	
    xs_mega_plot({'zxx #rightarrow zzz #rightarrow 4#mu1J': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_J/zxx_zzz_4m1fj/crossx_limits.txt',  # ll_ll_J
                 'zxx #rightarrow zzz #rightarrow 4e1J': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_J/zxx_zzz_4e1fj/crossx_limits.txt',
                 'zxx #rightarrow zzz #rightarrow 2#mu2e1J': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_J/zxx_zzz_2m2e1fj/crossx_limits.txt',
                 'wxx #rightarrow wzz #rightarrow 4#mu1J': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_J/wxx_zzw_4m1fj/crossx_limits.txt',
                 'wxx #rightarrow wzz #rightarrow 4e1J': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_J/wxx_zzw_4e1fj/crossx_limits.txt',
                 'wxx #rightarrow wzz #rightarrow 2#mu2e1J': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_J/wxx_zzw_2m2e1fj/crossx_limits.txt',
                 'zxx #rightarrow zzz #rightarrow 2#mu2J': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_J/zxx_zzz_2m2fj/crossx_limits.txt',   # ll_J_J
                 'zxx #rightarrow zzz #rightarrow 2e2J': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_J/zxx_zzz_2e2fj/crossx_limits.txt',
                 'zxx #rightarrow zww #rightarrow 2#mu2J': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_J/zxx_zww_2m2fj/crossx_limits.txt',
                 'zxx #rightarrow zww #rightarrow 2e2J': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_J/zxx_zww_2e2fj/crossx_limits.txt',
                 'wxx #rightarrow wzz #rightarrow 2#mu2J': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_J/wxx_wzz_2m2fj/crossx_limits.txt',
                  'wxx #rightarrow wzz #rightarrow 2e2J': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_J/wxx_wzz_2e2fj/crossx_limits.txt'},
                file_name='xs_mega_plot.pdf')
    
    xs_mega_plot({'zxx #rightarrow 2#mu2#gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_aa/zxx_2m2a/crossx_limits.txt', # ll_aa
                  'zxx #rightarrow 2e2#gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_aa/zxx_2e2a/crossx_limits.txt',
                  'axx #rightarrow 2#mu2#gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_aa/axx_2m2a/crossx_limits.txt',
                  'axx #rightarrow 2e2#gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_aa/axx_2e2a/crossx_limits.txt',
                  'zxx #rightarrow 2#gamma1J': '/Users/jcaridad/Desktop/Python/Research/Decays/J_aa/zxx_2a1fj/crossx_limits.txt', # J_aa
                  'wxx #rightarrow 2#gamma1J': '/Users/jcaridad/Desktop/Python/Research/Decays/J_aa/wxx_2a1fj/crossx_limits.txt',
                  'axx #rightarrow aza #rightarrow 2#gamma1J': '/Users/jcaridad/Desktop/Python/Research/Decays/J_aa/axx_2a1fj/crossx_limits.txt',
                  'axx #rightarrow azz #rightarrow 1#gamma4#mu': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/axx_1a4m/crossx_limits.txt', # ll_ll_a
                  'axx #rightarrow azz #rightarrow 1#gamma4e': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/axx_1a4e/crossx_limits.txt',
                  'axx #rightarrow azz #rightarrow 1#gamma2#mu2e': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/axx_1a2m2e/crossx_limits.txt',
                  'zxx #rightarrow zza #rightarrow 1#gamma4#mu': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/zxx_1a4m/crossx_limits.txt',
                  'zxx #rightarrow zza #rightarrow 1#gamma4e': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/zxx_1a4e/crossx_limits.txt',
                  'zxx #rightarrow zza #rightarrow 1#gamma2e2#mu': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/zxx_1a2m2e_e_outside/crossx_limits.txt',
                  'zxx #rightarrow zza #rightarrow 1#gamma2#mu2e': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/zxx_1a2m2e_m_outside/crossx_limits.txt'},
                 file_name='xs_mega_plot2.pdf')
    
    xs_mega_plot({
        'axx #rightarrow 3#gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/aaa/axx_3pho/crossx_limits.txt',   # aaa
        'axx #rightarrow azz #rightarrow 1#gamma1J2#mu': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_a/axx_azz_2m1fj1a/crossx_limits.txt', # ll_J_a
        'axx #rightarrow azz #rightarrow 1#gamma1J2#e': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_a/axx_azz_2e1fj1a/crossx_limits.txt',
        'zxx #rightarrow zza #rightarrow 2#mu1J1#gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_a/zxx_zza_2m1fj1a/crossx_limits.txt',
        'zxx #rightarrow zza #rightarrow 2#e1J1#gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_a/zxx_zza_2e1fj1a/crossx_limits.txt',
        'zxx #rightarrow zza #rightarrow 1J2#mu1#gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_a/zxx_zza_1fj2m1a/crossx_limits.txt',
        'zxx #rightarrow zza #rightarrow 1J2#e1#gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_a/zxx_zza_1fj2e1a/crossx_limits.txt',
        'wxx #rightarrow wza #rightarrow 1J2#mu1#gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_a/wxx_wza_1fj2m1a/crossx_limits.txt',
        'wxx #rightarrow wza #rightarrow 1J2#e1#gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_a/wxx_wza_1fj2e1a/crossx_limits.txt'
                }, file_name='xs_mega_plot3.pdf')
	'''
	xs_mega_plot({
		'\phi\gamma#rightarrow(\gamma\gamma) \gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/aaa/axx_3pho/crossx_limits.txt',	# aaa
		'\phiZ#rightarrow(\gamma\gamma)(\mu\mu)': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_aa/zxx_2m2a/crossx_limits.txt',	# ll_aa
		'\phiZ#rightarrow(\gamma\gamma)(ee)': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_aa/zxx_2e2a/crossx_limits.txt',
		'\phi\gamma#rightarrow(\gammaZ) \gamma#rightarrow(\gamma(\mu\mu)) \gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_aa/axx_2m2a/crossx_limits.txt',
		'\phi\gamma#rightarrow(\gammaZ) \gamma#rightarrow(\gamma(ee)) \gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_aa/axx_2e2a/crossx_limits.txt',
		'\phi\gamma#rightarrow(ZZ) \gamma#rightarrow((\mu\mu)(\mu\mu)) #gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/axx_1a4m/crossx_limits.txt', # ll_ll_a
		'\phi\gamma#rightarrow(ZZ) \gamma#rightarrow((ee)(ee)) #gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/axx_1a4e/crossx_limits.txt',
		'\phi\gamma#rightarrow(ZZ) \gamma#rightarrow((ee)(\mu\mu)) #gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/axx_1a2m2e/crossx_limits.txt',
		'\phiZ#rightarrow(Z\gamma)Z#rightarrow((\mu\mu) \gamma)(\mu\mu)': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/zxx_1a4m/crossx_limits.txt',
		'\phiZ#rightarrow(Z\gamma)Z#rightarrow((ee) \gamma)(ee)': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/zxx_1a4e/crossx_limits.txt',
		'\phiZ#rightarrow(Z\gamma)Z#rightarrow((\mu\mu) \gamma)(ee)': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/zxx_1a2m2e_e_outside/crossx_limits.txt',
		'\phiZ#rightarrow(Z\gamma)Z#rightarrow((ee) \gamma)(\mu\mu)': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_ll_a/zxx_1a2m2e_m_outside/crossx_limits.txt',
		'\phi\gamma#rightarrow(ZZ) \gamma#rightarrow(J(\mu\mu)) \gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_a/axx_azz_2m1fj1a/crossx_limits.txt', # ll_J_a
		'\phi\gamma#rightarrow(ZZ) \gamma#rightarrow(J(ee)) \gamma': '/Users/jcaridad/Desktop/Python/Research/Decays/ll_J_a/axx_azz_2e1fj1a/crossx_limits.txt'},
		file_name='xs_limit_summary.pdf')
