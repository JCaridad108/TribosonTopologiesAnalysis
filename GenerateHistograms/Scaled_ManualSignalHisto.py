import sys
sys.path.append('/Applications/root_v6.20.04/lib')
import ROOT
import array

def manual_signal(outputs, masses, crossx, boson_histos, type=''):
    '''
    outputs will be of the form:
    [ [[xx_list, efficiency, boson_list], [xx_list, effiency, boson_list]], ...]
    where efficiency is of the form [[passed, total], [passed, total], ...]
    '''
    # Creating empty list of efficiency for each output
    efficiency_list = [[], [], [], []]

    # List of boson histograms
    boson_list = []

    # Making a histogram for each output and giving each a different color
    if (type == '4l1fatjet') or (type == '6mu'):
        histos = [ROOT.TH1F('', ' ; m_{XX}[GeV]; events', 50, 100, 2500) for i in outputs]
    elif type == '2l2fatjet':
        histos = [ROOT.TH1F('', ' ; m_{XX}[GeV]; events', 50, 100, 2500) for i in outputs]
    else:
        histos = [ROOT.TH1F('', ' ; m_{XX}[GeV]; events', 50, 100, 2200) for i in outputs]

    for k in range(len(histos)):
        histos[k].SetLineColor(k + 1)

    for s in range(len(outputs)):
        xx_list = []
        for o in range(len(outputs[s])):
            xx_list += outputs[s][o][0]
            efficiency_list[s].append(outputs[s][o][1])
            boson_list += outputs[s][o][2]
        for xx in xx_list:
            histos[s].Fill(xx.M())

    for b in boson_list:
        boson_histos[0].Fill(b.M())

    # Normalizing histograms
    lumi = 100000  # (picobarns)
    for i in range(len(outputs)):
        N_list = []
        for e in range(len(efficiency_list[i])):
            N_list.append(crossx[i][e] * efficiency_list[i][e] * lumi)
        N = sum(N_list)/len(N_list)

        histos[i].Scale(N / histos[i].Integral())

    # Making legend for histogram
    legend = ROOT.TLegend(0.65, 0.7, 0.99, 0.95)
    for p in range(len(histos)):
        legend.AddEntry(histos[p], 'm_{XX} = '+'{} GeV'.format(masses[p]))
    legend.SetBorderSize(0)

    # List of efficiency: divided events/gen_events
    eff_list = [sum(efficiency_list[0])/len(efficiency_list[0]), sum(efficiency_list[1])/len(efficiency_list[1]),
                sum(efficiency_list[2])/len(efficiency_list[2]), sum(efficiency_list[3])/len(efficiency_list[3])]

    # Making efficiency and masses arrays to use in efficiency TGraph
    eff_array = array.array('d', eff_list)
    mass_array = array.array('d', masses)

    # Making eff_graph, titling it, and customizing it. Ready to be drawn.
    eff_graph = ROOT.TGraph(len(masses), mass_array, eff_array)
    eff_graph.SetMarkerStyle(4)
    eff_graph.SetTitle('')
    eff_graph.GetXaxis().SetTitle('m_{XX}[GeV]')
    eff_graph.GetYaxis().SetTitle('Efficiency')

    # Printing efficiency list
    print 'Efficiency List:', eff_list

    return histos, legend, eff_graph



