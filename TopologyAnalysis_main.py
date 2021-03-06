import sys
sys.path.append('/Applications/root_v6.20.04/lib')
import ROOT
from ReconstructionAnalysis.TopologyReconstruction import reconstruct
from GenerateHistograms.Scaled_SignalBackground.py import background_histo, signal_histo

# 1 photon, 2 fat jet final state
# gamma XX -> gamma Z Z -> gamma J J

if __name__ == '__main__':

    pdf_tex = str(input('pdf or tex:'))
    
    ###----------------Background----------------###
    directories_bkg = ['/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_bkg/tag_1_delphes_events.root',
                       '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_bkg/tag_2_delphes_events.root',
                       '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_bkg/tag_3_delphes_events.root',
                       '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_bkg/tag_4_delphes_events.root',
                       '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_bkg/tag_5_delphes_events.root',
                       '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_bkg/tag_6_delphes_events.root',
                       '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_bkg/tag_7_delphes_events.root',
                       '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_bkg/tag_8_delphes_events.root',
                       '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_bkg/tag_9_delphes_events.root',
                       '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_bkg/tag_10_delphes_events.root',
                       '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_bkg/tag_11_delphes_events.root',
                       '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_bkg/tag_12_delphes_events.root']

    # Cross-section corresponding to each file
    xs_list = [11480, 11480, 11480, 11470, 11400, 11360, 11480, 11540, 11540, 11560, 11550, 11540]

    # dictionaries with histograms to count particles
    count_histos_bkg = {'fatjet': ROOT.TH1F('Bkg Fat Jet Count', ' ; amount; events', 6, 0, 6),
                        'photon': ROOT.TH1F('Bkg Photon Count', ' ; amount; events', 6, 0, 6)}

    # creating list output_bkg with reconstruct() output of each file in directory_bkg
    output_bkg = [reconstruct(d, z_products={'fatjet': 2}, extra_ps={'photon': 1},
                              count_histos=count_histos_bkg) for d in directories_bkg]

    # Mass Histograms for the 3 bosons
    bkg_boson_hists = [ROOT.TH1F('Bkg FatJet-Z1', ' ; mass [GeV]; events', 50, 0, 200),
                       ROOT.TH1F('Bkg FatJet-Z2', ' ; mass [GeV]; events', 50, 0, 200),
                       ROOT.TH1F('Bkg Photon', ' ; mass [GeV]; events', 50, 0, 200)]

    bkg_canvas = ROOT.TCanvas()
    bkg_histo = background_histo(output_bkg, xs_list, boson_histos=bkg_boson_hists)
    bkg_root = ROOT.TFile('1pho2fatjet_bkg.root', 'recreate')
    bkg_histo.Draw('HISTO')
    bkg_histo.Write()
    bkg_canvas.SetLogy()
    bkg_canvas.Print('1pho2fatjet_bkg_histo.' + pdf_tex)
    bkg_root.Close()

    # Printing out counting histograms
    count_canv1 = ROOT.TCanvas()
    count_histos_bkg['fatjet'].Draw()
    count_canv1.Print('bkg_fatjet_count.' + pdf_tex)
    count_canv2 = ROOT.TCanvas()
    count_histos_bkg['photon'].Draw()
    count_canv2.Print('bkg_photon_count.' + pdf_tex)

    bc_1 = ROOT.TCanvas(); bkg_boson_hists[0].Draw(); bc_1.Print('bkg_boson1.' + pdf_tex)
    bc_2 = ROOT.TCanvas(); bkg_boson_hists[1].Draw(); bc_2.Print('bkg_boson2.' + pdf_tex)
    bc_3 = ROOT.TCanvas(); bkg_boson_hists[2].Draw(); bc_3.Print('bkg_boson3.' + pdf_tex)

    bkg_boson_file = ROOT.TFile('bkg_boson_file.root', 'recreate')
    bkg_boson_hists[0].Write(); bkg_boson_hists[1].Write(); bkg_boson_hists[2].Write(); bkg_boson_file.Close()

    # Getting bin content and writing them to txt file
    bin_content_file = open('bkg_bin_content.txt', 'w')
    for bi in range(52):
        bin_content_file.write(str(bkg_histo.GetBinContent(bi)) + '\n')
    bin_content_file.close()
    
    ###----------------Signal----------------###
    directories = ['/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_sig/tag_1_delphes_events.root',
                   '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_sig/tag_2_delphes_events.root',
                   '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_sig/tag_3_delphes_events.root',
                   '/Volumes/JMCR_SSD/Research/Decays/a_J_J/axx_azz_1a2fj/1a2fj_sig/tag_4_delphes_events.root']

    # dictionaries with histograms to count particles
    count_histos_sig = {'fatjet': ROOT.TH1F('Signal FatJet Count', ' ; amount; events', 6, 0, 6),
                        'photon': ROOT.TH1F('Signal Photon Count', ' ; amount; events', 6, 0, 6)}

    # list of outputs from reconstruct() function for each file
    output = [reconstruct(d, z_products={'fatjet': 2}, extra_ps={'photon' : 1},
                          count_histos=count_histos_sig) for d in directories]

    # Masses and xs lists correpsonding to each file
    sig_xs = [0.00002514, 0.0000359, 0.0000289, 0.00001916]
    mass_list = [500, 1000, 1500, 2000]

    # Mass Histograms for the 3 bosons
    sig_boson_hists = [ROOT.TH1F('Signal FatJet-Z1', ' ; mass [GeV]; events', 50, 0, 200),
                       ROOT.TH1F('Signal FatJet-Z2', ' ; mass [GeV]; events', 50, 0, 200),
                       ROOT.TH1F('Signal Photon-2', ' ; mass [GeV]; events', 50, 0, 200)]

    # Run the reconstruct() output through the signal function, and extract the outputted histogram, legend, and graph
    sig_histo_eff_graph = signal_histo(output, mass_list, sig_xs, boson_histos=sig_boson_hists)
    sig_histos, sig_legend, efficiency_plot = sig_histo_eff_graph[0], sig_histo_eff_graph[1], sig_histo_eff_graph[2]

    # Printing out coutning histograms
    count_canv1 = ROOT.TCanvas()
    count_histos_sig['fatjet'].Draw()
    count_canv1.Print('sig_fatjet_count.' + pdf_tex)
    count_canv2 = ROOT.TCanvas()
    count_histos_sig['photon'].Draw()
    count_canv2.Print('sig_photon_count.' + pdf_tex)

    bc_1 = ROOT.TCanvas(); sig_boson_hists[0].Draw(); bc_1.Print('sig_boson1.' + pdf_tex)
    bc_2 = ROOT.TCanvas(); sig_boson_hists[1].Draw(); bc_2.Print('sig_boson2.' + pdf_tex)
    bc_3 = ROOT.TCanvas(); sig_boson_hists[2].Draw(); bc_3.Print('sig_boson3.' + pdf_tex)

    sig_boson_file = ROOT.TFile('sig_boson_file.root', 'recreate')
    sig_boson_hists[0].Write(); sig_boson_hists[1].Write(); sig_boson_hists[2].Write(); sig_boson_file.Close()

    sig_histo_canvas = ROOT.TCanvas()
    sig_histo_file = ROOT.TFile('1pho2fatjet_sig_histo_file.root', 'recreate')

    sig_histos[1].Draw('Histo')
    sig_histos[1].Write()
    for h in sig_histos:
        if h != sig_histos[1]:
            h.Draw("HISTO SAME")
            h.Write()
    sig_legend.Draw()
    sig_histo_canvas.Print('1pho2fatjet_sig_histogram.' + pdf_tex)
    sig_histo_file.Close()

    # Creating eff plot canvas and root file, drawing and writing eff plot
    eff_canvas = ROOT.TCanvas()
    eff_plot_file = ROOT.TFile('1pho2fatjet_signal_efficiency.root', 'recreate')
    efficiency_plot.SetMinimum(0)
    efficiency_plot.SetMaximum(1.0)
    efficiency_plot.Draw()
    efficiency_plot.Write()
    eff_canvas.Print('signal_eff.' + pdf_tex)
    eff_plot_file.Close()

    # Writing all signal bin contents to txt files
    sig_file1, sig_file2 = open('sig_content1.txt', 'w'), open('sig_content2.txt', 'w')
    sig_file3, sig_file4 = open('sig_content3.txt', 'w'), open('sig_content4.txt', 'w')
    sig_files = [sig_file1, sig_file2, sig_file3, sig_file4]
    for j in range(len(sig_histos)):
        for bi in range(52):
            sig_files[j].write(str(sig_histos[j].GetBinContent(bi)) + '\n')
    sig_file1.close()
    sig_file2.close()
    sig_file3.close()
    sig_file4.close()

    print 'Done'
