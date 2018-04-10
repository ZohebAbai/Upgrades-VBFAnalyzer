#!/usr/bin/env python

import os, sys, ROOT
import numpy as np

ROOT.gROOT.SetBatch(1)
ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetNdivisions(405,"x");
ROOT.gStyle.SetEndErrorSize(0.)
ROOT.gStyle.SetErrorX(0.001)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)



import optparse

def main():

  options = optparse.OptionParser()

  options.add_option('-f', '--files',
      dest="files",
      default="VBF_M125_PU0.txt",
      type="string",
      )
  options.add_option('-n', '--maxEvts',
      dest="maxEvts",
      default=-1,
      type="int",
      )

  evtsel = optparse.OptionGroup(options, "Event selections",
                          "Caution: Do not change by hand")

  evtsel.add_option("--nak8min",
      dest="nak8Min",
      default=1,
      type="int",
      )

  evtsel.add_option("--ptak8_0_Min",
      dest="ptak8_0_Min",
      default=150.,
      type="float",
      )

  evtsel.add_option("--etaak8_0_Max",
      dest="etaak8_0_Max",
      default=3.5,
      type="float",
      )


  options.add_option_group(evtsel)

  opt, remainder = options.parse_args()

  print opt

  fout = ROOT.TFile(opt.files.rstrip().replace('txt', 'root'), 'RECREATE')
  fout.cd()

  h2_msd0_npv                  = ROOT.TH2D("h2_msd0_npv"                  ,";n(PV);Soft dropped mass (leding AK8) [GeV];;"  , 200, 0., 200., 20, 0., 200.)
#  h2_msd1_npv                  = ROOT.TH2D("h2_msd1_npv"                  ,";n(PV);Soft dropped mass (2nd AK8) [GeV];;"     , 200, 0., 200., 20, 0., 200.)

#  h2_bFl_sjpt_sjeta            = ROOT.TH2D("h2_bFl_sjpt_sjeta"            ,";p_{T} (subjet) [GeV]; #eta (subjet);;", 200, 0., 2000, 50, -5, 5)
#  h2_bFl_sjpt_sjeta_btagged    = ROOT.TH2D("h2_bFl_sjpt_sjeta_btagged"    ,";p_{T} (subjet) [GeV]; #eta (subjet);;", 200, 0., 2000, 50, -5, 5)

#  h2_cFl_sjpt_sjeta            = ROOT.TH2D("h2_cFl_sjpt_sjeta"            ,";p_{T} (subjet) [GeV]; #eta (subjet);;", 150, 0., 3000, 50, -5, 5)
#  h2_cFl_sjpt_sjeta_btagged    = ROOT.TH2D("h2_cFl_sjpt_sjeta_btagged"    ,";p_{T} (subjet) [GeV]; #eta (subjet);;", 150, 0., 3000, 50, -5, 5)

#  h2_lFl_sjpt_sjeta            = ROOT.TH2D("h2_lFl_sjpt_sjeta"            ,";p_{T} (subjet) [GeV]; #eta (subjet);;", 150, 0., 3000, 50, -5, 5)
#  h2_lFl_sjpt_sjeta_btagged    = ROOT.TH2D("h2_lFl_sjpt_sjeta_btagged"    ,";p_{T} (subjet) [GeV]; #eta (subjet);;", 150, 0., 3000, 50, -5, 5)

  h2_ak8pt_ak8eta              = ROOT.TH2D("h2_ak8pt_ak8eta"              ,";p_{T} of (AK8Jet) [GeV]; #eta (AK8);;", 50, 0., 1000, 50, -5, 5)
#  h2_ak8pt_ak8eta_htagged      = ROOT.TH2D("h2_ak8pt_ak8eta_htagged"      ,";p_{T} (AK8) [GeV]; #eta (AK8);;", 150, 0., 3000, 50, -5, 5)

#  h2_ak4pt_ak4eta              = ROOT.TH2D("h2_ak4pt_ak4eta"              ,";p_{T} (AK4) [GeV]; #eta (AK4);;", 150, 0., 3000, 50, -5, 5)
#  h2_ak4pt_ak4genjetpt         = ROOT.TH2D("h2_ak4pt_ak4genjetpt"         ,";p_{T} (AK4 jets) [GeV]; p_{T} (AK4 genjets) [GeV];Events;" ,300,0.,3000,300,0.,3000)

#  h_genH_pt                    = ROOT.TH1D("h_genH_pt"                    ,"p_{T} (H) [GeV]; Events;;"     ,300  ,0.    ,3000)
#  h_genH_eta                   = ROOT.TH1D("h_genH_eta"                   ,"#eta (H) [GeV]; Events;;"      ,200  ,-5    ,5)

#  h_nak8                       = ROOT.TH1D("h_nak8"                       ,";N(AK8) [GeV]; Events;;"       ,11   ,-0.5  ,10.5 )
#  h_nak4                       = ROOT.TH1D("h_nak4"                       ,";N(AK4) [GeV]; Events;;"       ,501  ,-0.5  ,501.5)

  h_ak4_deepcsv1                = ROOT.TH1D("h_ak4_deepcsv1"                ,";DeepCSV of AK4_jet1;;"        ,100   ,0.    ,1.   )
  h_ak4_deepcsv2                = ROOT.TH1D("h_ak4_deepcsv2"                ,";DeepCSV of AK4_jet2;;"        ,100   ,0.    ,1.   )

  h_ak40pt                     = ROOT.TH1D("h_ak40pt"                     ,";p_{T} of ak4_jet1  [GeV]; Events;;"        ,100  ,0.    ,1000. )
  h_ak41pt                     = ROOT.TH1D("h_ak41pt"                     ,";p_{T} of ak4_jet2  [GeV]; Events;;"        ,100  ,0.    ,1000. )
  h_ak80pt                     = ROOT.TH1D("h_ak80pt"                     ,";p_{T} leading Ak8 jet [GeV]; Events;;"        ,100  ,0.    ,1000. )
#  h_ak81pt                     = ROOT.TH1D("h_ak81pt"                     ,";p_{T} [GeV]; Events;;"        ,300  ,0.    ,3000 )
  h_ak80eta                    = ROOT.TH1D("h_ak80eta"                    ,";#eta Ak8 jet"                       ,200  ,-5    ,5    )
  h_ak40eta                    = ROOT.TH1D("h_ak40eta"                    ,";#eta ak4_jet1 "                       ,200  ,-5    ,5    )
  h_ak41eta                    = ROOT.TH1D("h_ak41eta"                    ,";#eta ak4_jet2 "                       ,200  ,-5    ,5    )
#  h_ak81eta                    = ROOT.TH1D("h_ak81eta"                    ,";#eta;;"                       ,200  ,-5    ,5    )
#  h_ak80_tau2_tau1             = ROOT.TH1D("h_ak80_t2byt1"                ,";#tau_{2}/#tau_{1};;"          ,100  ,0     ,1    )
#  h_ak81_tau2_tau1             = ROOT.TH1D("h_ak81_t2byt1"                ,";#tau_{2}/#tau_{1} ;;"         ,100  ,0     ,1    )
  h_sdmass_ak80                = ROOT.TH1D("h_sdmass_ak80"                ,";softdropped_mass of AK8Jet[GeV];;"      ,100  ,0     ,200 )
#  h_sdmass_ak81                = ROOT.TH1D("h_sdmass_ak81"                ,";softdropped_mass[GeV];;"      ,100  ,0     ,1000 )

  h_nvbfpairs                  = ROOT.TH1D("h_nvbfpairs"                  ,";N(VBF pairs); Events;;"       ,201  ,-0.5  ,200.5 )
  h_vbf0pt                     = ROOT.TH1D("h_vbf0pt"                     ,";p_{T} (VBF) [GeV]; Events;;"  ,100  ,0.    ,1000 )
  h_vbf1pt                     = ROOT.TH1D("h_vbf1pt"                     ,";p_{T} (VBF) [GeV]; Events;;"  ,100  ,0.    ,1000 )
  h_vbf0eta                    = ROOT.TH1D("h_vbf0eta"                    ,";#eta (VBF); Events;"          ,200  ,-5    ,5    )
  h_vbf1eta                    = ROOT.TH1D("h_vbf1eta"                    ,";#eta (VBF); Events;"          ,200  ,-5    ,5    )
  h_deltaEta                   = ROOT.TH1D("h_deltaEta"                   ,";#delta#eta of VBF jets;;"     ,20   ,0     ,10   )
  h_mjjvbf                     = ROOT.TH1D("h_mjjvbf"                     ,";M(jj) (VBF) [GeV]; Events;"   ,200  ,0.    ,2000 )
  h_sj0_etas                    = ROOT.TH1D("h_sj0_etas"                    ,";Eta of AK8_subjet1;;"          ,200   ,-5     ,5 )
  h_sj1_etas                    = ROOT.TH1D("h_sj1_etas"                    ,";Eta of AK8_subjet2;;"          ,200   ,-5     ,5 )

  h_sj0_pts                    = ROOT.TH1D("h_sj0_pts"                    ,";p_{T} of AK8_subjet1;;"          ,300   ,0     ,3000 )
  h_sj1_pts                    = ROOT.TH1D("h_sj1_pts"                    ,";p_{T} of AK8_subjet2;;"          ,300   ,0     ,3000 )
  h_sj0_csvv2                  = ROOT.TH1D("h_sj0_csvv2"                  ,";CSVv2 of AK8_subjet1;;"          ,100   ,0.    ,1.   )
  h_sj1_csvv2                  = ROOT.TH1D("h_sj1_csvv2"                  ,";CSVv2 of AK8_subjet2;;"          ,100   ,0.    ,1.   )
  h_sj0_deepcsv                = ROOT.TH1D("h_sj0_deepcsv"                ,";DeepCSV of AK8_subjet1;;"        ,100   ,0.    ,1.   )
  h_sj1_deepcsv                = ROOT.TH1D("h_sj1_deepcsv"                ,";DeepCSV of AK8_subjet2;;"        ,100   ,0.    ,1.   )

  h_mjj_vbfsel                 = ROOT.TH1D("h_mjj_vbfsel"                 ,";M(jj) [GeV]; Events;"         ,400  ,500.   ,4500 )
  h_mjj_vbfsel_scaledHTagEff   = ROOT.TH1D("h_mjj_vbfsel_scaledHTagEff"   ,";M(jj) [GeV]; Events;"         ,400  ,500.   ,4500 )
  h_mjj_novbf_nosjbtag         = ROOT.TH1D("h_mjj_novbf_nosjbtag"         ,";M(jj) [GeV]; Events;"         ,400  ,500.   ,4500 )
  h_mjj_novbf_2sjbtag          = ROOT.TH1D("h_mjj_novbf_2sjbtag"          ,";Mass of AK8 jets [GeV]; Events;"         ,400  ,500.   ,4500 )
  h_mjj                        = ROOT.TH1D("h_mjj"                        ,";Mass of AK8Jets [GeV]; Events;"         ,100  ,0.   ,200 )
  h_higgs_invariantMassb       = ROOT.TH1D("h_higgs_invariantMassb"       ,";M(higgs_invariantMass_with_1b-tag) [GeV]; Events;"         ,100  ,0.   ,200 )
  h_higgs_invariantMassbb      = ROOT.TH1D("h_higgs_invariantMassbb"       ,";M(higgs_invariantMass_with_bb-tag) [GeV]; Events;"         ,100  ,0.   ,200 )
  h_cutflow                    = ROOT.TH1D("h_cutflow"                    ,";;Events;"                     ,10   ,0.5    ,10.5 )

  h_cutflow.GetXaxis().SetBinLabel(1 ,"All evts") ;
  h_cutflow.GetXaxis().SetBinLabel(2 ,"AK8 jets") ;
  h_cutflow.GetXaxis().SetBinLabel(3 ,"p_{T}+#eta") ;
#  h_cutflow.GetXaxis().SetBinLabel(4 ,"#Delta#Eta(JJ)") ;
  h_cutflow.GetXaxis().SetBinLabel(5 ,"#tau_{21}") ;
  h_cutflow.GetXaxis().SetBinLabel(6 ,"M(J)") ;
  h_cutflow.GetXaxis().SetBinLabel(7 ,"> 1 Subjet b") ;
  h_cutflow.GetXaxis().SetBinLabel(8 ,"> 2 Subjet b") ;
 # h_cutflow.GetXaxis().SetBinLabel(9 ,"> 3 Subjet b") ;
  h_cutflow.GetXaxis().SetBinLabel(10,"VBF") ;

  fnames = [line.strip() for line in open(opt.files, 'r')]

  try: doqcdmaps = bool(sys.argv[2])
  except: doqcdmaps = False

  ievt = 0
  for fname in fnames:
    if opt.maxEvts > 0 and ievt > opt.maxEvts: break
    if ievt%100 == 0: print " Processing evt %i" % ievt

    print 'Opening file %s' % fname
    f = ROOT.TFile.Open(fname)
    print f.ls()

    tree = f.Get("ana/anatree")
    entries = tree.GetEntriesFast()
    count=[]
    x=0
    deepcsvMWP = 0.4941
    deepcsvLWP = 0.1522
    for event in tree:

      if opt.maxEvts > 0 and ievt > opt.maxEvts: break
      if ievt%100 == 0: print " Processing evt %i" % ievt

      ievt += 1


      pts             = event.AK8JetsPuppi_pt
#      pts_ak4         = event.AK4JetsCHS_pt
#      sj0_pts         = event.AK8JetsPuppi_sj0pt
#      sj1_pts         = event.AK8JetsPuppi_sj1pt

      nak8 = len(pts)
#      nak4 = len(pts_ak4)

      h_cutflow.Fill(1)

      ### Selecting at least two AK8 jets with two subjets, and at least two AK4 jets per event:
      if nak8 >= opt.nak8Min: #and len(sj0_pts) >= 2 and len(sj1_pts) >= 2:
        h_cutflow.Fill(2)
      else: continue
#Define AK4Jets variable
      all_ak4jetpT        = event.AK4JetsCHS_pt
      all_ak4jetEta       = event.AK4JetsCHS_eta
      all_ak4jetphi       = event.AK4JetsCHS_phi
      all_ak4jetmass      = event.AK4JetsCHS_mass
      all_ak4deepcsv      = event.AK4JetsCHS_deepcsv
      p4_ak4 = ROOT.TLorentzVector()

      my_ak4P4            = []
      for i in range(len(all_ak4jetpT)):
          p4_ak4.SetPtEtaPhiM(all_ak4jetpT[i],all_ak4jetEta[i],all_ak4jetphi[i],all_ak4jetmass[i])
          my_ak4P4.append(p4_ak4)


      ak4jetindex         = [i for i in range(len(all_ak4jetpT ))]
      sorted_ak4jets      = [jet for pt,jet in sorted(zip(all_ak4jetpT,my_ak4P4) , reverse=True)]
      sorted_ak4deepcsv   = [csv for pt, csv in sorted(zip(all_ak4jetpT,all_ak4deepcsv ),reverse=True)]
      #sorted_ak4jetindex  = [jetindex for pt,jetindex in sorted(zip(all_ak4jetpT,ak4jetindex))]


      if len(my_ak4P4) >=2:
          ak4jet1 = sorted_ak4jets[0]
          ak4jet2 = sorted_ak4jets[1]
          ak4csvjet1 = sorted_ak4deepcsv[0]
          ak4csvjet2 = sorted_ak4deepcsv[1]

          if ak4jet1.Pt() > 50 and  ak4jet2.Pt() > 50 and  ak4jet1.Eta() < 3.5 and ak4jet2.Eta() < 3.5 :
              h_ak40pt.Fill(ak4jet1.Pt())
              h_ak41pt.Fill(ak4jet2.Pt())
              h_ak40eta.Fill(ak4jet1.Eta())
              h_ak41eta.Fill(ak4jet2.Eta())
              h_ak4_deepcsv1.Fill(ak4csvjet1)
              h_ak4_deepcsv2.Fill(ak4csvjet2)
              count.append(x)
              x +=1



#   Define AK8  variable
      npv             = event.npv
      etas            = event.AK8JetsPuppi_eta
      sd_masses       = event.AK8JetsPuppi_softDropMassPuppi
      masses          = event.AK8JetsPuppi_mass
      phis            = event.AK8JetsPuppi_phi
#define AK8subjet variable      
      sj0_pts         = event.AK8JetsPuppi_sj0pt
      sj1_pts         = event.AK8JetsPuppi_sj1pt
      sj0_etas        = event.AK8JetsPuppi_sj0eta
      sj1_etas        = event.AK8JetsPuppi_sj1eta
      sj0_phi        = event.AK8JetsPuppi_sj0phi
      sj1_phi        = event.AK8JetsPuppi_sj1phi
      sj0_mass        = event.AK8JetsPuppi_sj0mass
      sj1_mass        = event.AK8JetsPuppi_sj1mass
      sj0_fls         = event.AK8JetsPuppi_sj0partonflavour
      sj1_fls         = event.AK8JetsPuppi_sj1hadronflavour
      deepcsv_sj0s    = event.AK8JetsPuppi_sj0deepcsv
      deepcsv_sj1s    = event.AK8JetsPuppi_sj1deepcsv
      #print len(sj0_etas)
      csvv2_sj0s = event.AK8JetsPuppi_sj0csvv2
      csvv2_sj1s = event.AK8JetsPuppi_sj1csvv2

      my_AK8subjet1P4=ROOT.TLorentzVector()
      my_AK8subjet2P4=ROOT.TLorentzVector()
      subjet_sel= len(sj0_pts) > 0 
      if subjet_sel:
          my_AK8subjet1P4.SetPtEtaPhiM(sj0_pts[0],sj0_etas[0],sj0_phi[0],sj0_mass[0])
          my_AK8subjet2P4.SetPtEtaPhiM(sj1_pts[0],sj1_etas[0],sj1_phi[0],sj1_mass[0])
          Higgs_invmass = (my_AK8subjet1P4 + my_AK8subjet2P4).Mag()
      p4_ak80 = ROOT.TLorentzVector()
      p4_ak80.SetPtEtaPhiM(pts[0], etas[0], phis[0], masses[0])
      mjj = (p4_ak80).Mag()

      ptsel  = pts[0] > opt.ptak8_0_Min # and pts[1] > opt.ptak8_1_Min
      etasel = abs(etas[0]) < opt.etaak8_0_Max # and abs(etas[1]) < opt.etaak8_1_Max
      h2_ak8pt_ak8eta.Fill(pts[0], etas[0])
      #subjet_sel= len(sj0_pts) > 0
      if ptsel and etasel and subjet_sel:
     	h_ak80pt.Fill(pts[0])
    	h_ak80eta.Fill(etas[0])
    	h2_msd0_npv.Fill(npv, sd_masses[0])
        h_sdmass_ak80.Fill(sd_masses[0])
    	h_mjj.Fill(mjj)
        #h_higgs_invariantMass.Fill(Higgs_invmass)
        h_sj0_pts.Fill(sj0_pts[0])
        h_sj1_pts.Fill(sj1_pts[0])
        h_sj0_etas.Fill(sj0_etas[0])
        h_sj1_etas.Fill(sj1_etas[0])
        h_sj0_deepcsv.Fill(deepcsv_sj0s[0])
        h_sj1_deepcsv.Fill(deepcsv_sj1s[0])
        h_cutflow.Fill(3)
      else: continue

      if deepcsv_sj0s[0] > deepcsvMWP:
          h_higgs_invariantMassb.Fill(Higgs_invmass)
      if deepcsv_sj0s[0] > deepcsvMWP and deepcsv_sj1s[0] > deepcsvMWP:
          h_higgs_invariantMassbb.Fill(Higgs_invmass)
#define AK8subjet variable
      #Higgs_invmass = (my_AK8subjet1P4 + my_AK8subjet2P4).Mag()



#      h_mjj_vbfsel.Fill(mjj)
#      hjet1eff = getHTagEff(pts[0], etas[0])
#      hjet2eff = getHTagEff(pts[1], etas[1])
#      h_mjj_vbfsel_scaledHTagEff.Fill(mjj, hjet1eff*hjet2eff)


  fout.cd()

  h_cutflow_eff = h_cutflow.Clone("h_cutflow_eff")
  h_cutflow_eff.SetTitle(";;Efficiency;")

  h_cutflow_eff.Scale(1./h_cutflow.GetBinContent(1))

  for i in range(1,h_cutflow_eff.GetNbinsX()):
    print h_cutflow_eff.GetXaxis().GetBinLabel(i), h_cutflow_eff.GetBinContent(i)

  fout.Write()
  fout.Close()

if __name__ == "__main__":
  main()
