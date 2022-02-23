import sys
sys.path.append('/Applications/root_v6.20.04/lib')
import ROOT
from xx_mass import xx_mass
from z_mass import z_mass

def reconstruct_vfj(directory, z_products='', w_products='', xx_products='', count_histos=[]):
    """
    Reconstruct events with 4-quark large jets AKA Very-Fat-Jets (VFJ)
    """
    # Open file, get tree, get number of events
    delph_file = ROOT.TFile.Open(directory)
    tree = delph_file.Get('Delphes')

    # amount of events generated in MadGraph
    generated_events = tree.GetEntries()

    z_list = []
    w_list = []

    xx_list = []

    # Amount of Zs wanted per event
    zs_wanted = 0
    for e in z_products:
        if (e == 'muon') or (e == 'electron'):
            zs_wanted += z_products[e] / 2
        elif e == 'fatjet':
            zs_wanted += z_products[e]
    # Amount of Ws wanted per event
    ws_wanted = 0
    for v in w_products:
        if (v == 'muon') or (v == 'electron'):
            ws_wanted += w_products[v] / 2
        elif v == 'fatjet':
            ws_wanted += w_products[v]
    # Amount of photons wanted per event
    ps_wanted = 0
    for p in xx_products:
        if p == 'photon':
            ps_wanted += xx_products[p]

    for i in range(generated_events):
        entry = tree.GetEntry(i)

        # When count is True, the event passes all event selection requirements
        count = True

        # HERE BEGIN RECONSTRUCTIONS
        if 'muon' in z_products:

            muon_amount = tree.Muon.GetEntries()

            # Filling the muon count histogram
            count_histos['muon'].Fill(muon_amount)

            muons = [ROOT.TLorentzVector() for k in range(muon_amount)]

            # Separate the muons by charge
            muons_plus, muons_minus = [], []

            # Setting Pt, Eta, Phi, M
            for j in range(muon_amount):
                muons[j].SetPtEtaPhiM(tree.GetLeaf('Muon.PT').GetValue(j),
                                      tree.GetLeaf('Muon.Eta').GetValue(j),
                                      tree.GetLeaf('Muon.Phi').GetValue(j),
                                      0.1)
                if tree.GetLeaf('Muon.Charge').GetValue(j) == -1:
                    muons_minus.append(muons[j])
                elif tree.GetLeaf('Muon.Charge').GetValue(j) == 1:
                    muons_plus.append(muons[j])

            # Reconstructing the muons into desired amount of Zs
            if (len(muons_plus) >= (z_products['muon']//2)) and (len(muons_minus) >= (z_products['muon']//2)):
                z_list.append(z_mass(plus=muons_plus, minus=muons_minus, amnt=z_products['muon']//2)[0])

            else:
                count = False

        if 'vfatjet' in xx_products:
            vfatjet_amount = tree.FatJet.GetEntries()

            # Filling the count histo
            count_histos['vfatjet'].Fill(vfatjet_amount)

            vfatjets = [ROOT.TLorentzVector() for v in range(vfatjet_amount)]

            # Setting values
            for v in range(vfatjet_amount):
                vfatjets[v].SetPtEtaPhiM(tree.GetLeaf('FatJet.PT').GetValue(v),
                                         tree.GetLeaf('FatJet.Eta').GetValue(v),
                                         tree.GetLeaf('FatJet.Phi').GetValue(v),
                                         tree.GetLeaf('FatJet.Mass').GetValue(v))

            # ALSO TRY WITH EFFIEICNY -> 1 BY ACCEPTING ALL EVENTS WITH >= 1 FATJET
            #R_cut = [2*f.M()/f.Pt() for f in vfatjets]
            cut_vfatjets = vfatjets[:]
            '''
            for i in range(len(vfatjets)):
                if (R_cut[i] >= 1.0):# and (R_cut[i] <= 1.6):
                    cut_vfatjets.append(vfatjets[i])
            '''
            if vfatjet_amount >= 1:
                #r_deltas = [abs(pow(2*f.M()/f.Pt(), 2) - 1.2) for f in cut_vfatjets]
                #xx_list.append(cut_vfatjets[r_deltas.index(min(r_deltas))])

                #masses = [j.M() for j in cut_vfatjets]
                #xx_list.append(cut_vfatjets[masses.index(max(masses))])

                #pt_list = [f.Pt() for f in cut_vfatjets]
                #xx_list.append(cut_vfatjets[pt_list.index(max(pt_list))])
                '''
                pt_cut = [i for i in cut_vfatjets if i.Pt() >= 500]

                if len(pt_cut) > 1:
                    max_pt = [f.Pt() for f in pt_cut]
                    xx_list.append(pt_cut[max_pt.index(max(max_pt))])
                '''
                # FIXME: Set an R cut before the code below too maybe
                r_cut = [i for i in cut_vfatjets if (2*i.M())/i.Pt() > 0.5]
                #r_cut = cut_vfatjets[:]
                if len(r_cut) > 0:
                    pts = [i.Pt() for i in r_cut]
                    xx_list.append(r_cut[pts.index(max(pts))])

            else:
                count = False

    numb_events = len(xx_list)
    boson_list = z_list

    efficiency = float(numb_events)/float(generated_events)
    print 'Generated Events:', generated_events
    print 'Nmb of events:', numb_events
    print 'Efficiency:', efficiency
    print ''
    delph_file.Close()

    return xx_list, efficiency, boson_list

if __name__ == '__main__':
    print 'Done'
