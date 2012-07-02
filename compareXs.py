#!/usr/bin/env python

import ROOT as r
from utils import threeToTwo

options = {
    'refProcess': 'squark',
    'refXsFile':  'sms_xs/sms_xs.root',
    'limitFile': '~/Projects/ra1ToyResults/2011/1000_toys/T2tt/'
                 'CLs_frequentist_TS3_T2tt_lo_RQcdFallingExpExt_fZinvTwo_55_'
                 '0b-1hx2p_55_1b-1hx2p_55_2b-1hx2p_55_gt2b-1h.root',
    'plotTitle': 'pp#rightarrow#tilde{t} #tilde{t}#; #tilde{t}#rightarrow t+'
                 '#tilde{#chi}    m_{#tilde{#chi}} = 50 GeV/c^{2}',
    'refYRange':    (50.,50.),
    }

plotOptOverrides = { 'xLabel': 'm_{#tilde{q}} [GeV/c^{2}]' }


def drawStamp(canvas):
    canvas.cd()
    tl = r.TLatex()
    tl.SetNDC()
    tl.SetTextAlign(12)
    tl.SetTextSize(0.04)
    tl.DrawLatex(0.35,0.8,'CMS Prelimary')
    tl.DrawLatex(0.55,0.8,'#sqrt{s} = 7 TeV, #int L dt = 4.98 fb^{-1}')
    tl.SetTextSize(0.1)
    tl.DrawLatex(0.55,0.72,'#alpha_{T}')
    return tl

def getReferenceXsHisto(refHistoName, filename):
    refFile = r.TFile(filename,'READ')
    refHisto = refFile.Get(refHistoName).Clone()
    refHisto.SetDirectory(0)
    refFile.Close()
    histoD = {
        'refHisto': {
            'hist': refHisto,
            'LineWidth': 2,
            'LineStyle': 2,
            'LineColor': r.kBlack,
            'label': '{0} pair production'.format(refHistoName.capitalize())
            }
        }
    return histoD


def getExclusionHistos(limitFile, yMinMax=(50,50)):
    limitHistoDict = {
        'UpperLimit': {
            'label': 'Upper Limit',
            'LineWidth': 3,
            'LineColor': r.kBlue+2,
            'opts': 'c',
            'Smooth': True,
            },
        'ExpectedUpperLimit': {
            'label': 'Expected Upper Limit (#pm 1 #sigma)',
            'LineWidth': 2,
            'LineColor': r.kOrange+7,
            'LineStyle': 9,
            'opts': 'c',
            'Smooth': True,
            # for legend
            'FillStyle': 3001,
            'FillColor': r.kBlue-10,
            },
        'ExpectedUpperLimit_+1_Sigma': {
            'label': 'Expected Upper Limit (+1 #sigma)',
            'FillStyle': 3001,
            'LineWidth': 2,
            'LineColor': r.kOrange+7,
            'FillColor': r.kBlue-10,
            'opts': 'c',
            'Smooth': True,
            },
        'ExpectedUpperLimit_-1_Sigma': {
            'label': 'Expected Upper Limit (-1 #sigma)',
            'LineColor': r.kOrange+7,
            'LineWidth': 2,
            'FillColor': 10,
            'opts': 'c',
            'Smooth': True,
            },
        }

    rfile = r.TFile(limitFile,'READ')
    for limitHistoName, opts in limitHistoDict.iteritems():
        limitHisto = threeToTwo(rfile.Get(limitHistoName))
        minYBin = limitHisto.GetYaxis().FindBin(yMinMax[0])
        maxYBin = limitHisto.GetYaxis().FindBin(yMinMax[1])

        opts['hist'] = limitHisto.ProjectionX('T2tt',minYBin,maxYBin).Clone()
        opts['hist'].SetDirectory(0)

    rfile.Close()
    return limitHistoDict


def compareXs(refProcess, refXsFile="sms_xs/sms_xs.root",
              limitFile="xsLimit.root", pdfFile="sms_xs/compareXs.pdf",
              refYRange=(50,50), plotTitle="", plotOptOverrides=None) :
    plotOpts = {
        'yMax': 2e+1,
        'yMin': 2e-4,
        'xMin': 300,
        'xMax': 1200,
        'xLabel': "{p} mass [GeV/c^{{2}}]".format(
            p=refProcess.capitalize().replace('_',' ')),
        'yLabel': '#sigma [pb]',
        'legendPosition': [0.12, 0.12, 0.50, 0.30],
        }
    if plotOptOverrides is not None:
        plotOpts.update(plotOptOverrides)

    refHisto = getReferenceXsHisto(refProcess, refXsFile)
    exclusionHistos = getExclusionHistos(limitFile)

    canvas = r.TCanvas()
    hs = dict(refHisto.items() + exclusionHistos.items())

    leg = r.TLegend(*plotOpts['legendPosition'])
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    histosToDraw = [ 'ExpectedUpperLimit_+1_Sigma',
                     'ExpectedUpperLimit',
                     'ExpectedUpperLimit_-1_Sigma',
                     'UpperLimit',
                     'refHisto' ]
    for iHisto, hname in enumerate(histosToDraw):
        props = hs[hname]
        h = props['hist']
        h.SetStats(False)
        h.SetTitle(plotTitle)
        h.GetXaxis().SetRangeUser(plotOpts['xMin'],plotOpts['xMax'])
        h.SetMinimum(plotOpts['yMin'])
        h.SetMaximum(plotOpts['yMax'])
        if props.get('Smooth', False):
            h.Smooth(1,'R')
        h.Draw("%s%s"%(props.get('opts','c'), "same" if iHisto else ""))
        for attr in ['LineColor', 'LineStyle', 'LineWidth']:
            eval('h.Set{attr}(props.get("{attr}",1))'.format(attr=attr))
        for attr in ['FillStyle', 'FillColor']:
            if attr in props:
                eval('h.Set{attr}(props.get("{attr}",1))'.format(attr=attr))
        if "Sigma" not in hname:
            leg.AddEntry(h, props['label'], "lf")
        h.GetXaxis().SetTitle(plotOpts['xLabel'])
        h.GetYaxis().SetTitle(plotOpts['yLabel'])
    leg.Draw()
    tl = drawStamp(canvas)
    r.gPad.RedrawAxis()
    canvas.SetLogy()
    canvas.SetTickx()
    canvas.SetTicky()
    print "Saving to {file}".format(file=pdfFile)
    canvas.Print(pdfFile)

def setup() :
    r.gROOT.SetBatch(True)
    r.gErrorIgnoreLevel = 2000

def main():
    setup()
    compareXs(plotOptOverrides=plotOptOverrides, **options )

if __name__=="__main__":
    main()
