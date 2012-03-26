#!/usr/bin/env python

import common,workspace
import likelihoodSpec

def signal(i) :

    def scaled(t, factor) :
        return tuple([factor*item for item in t])

    simple = common.signal(xs = 1.0e-2, label = "signal")
    simple.insert("test", {
            "effSimple": (0.30, ),
            })
    
    lm6 = common.signal(xs = 0.3104, label = "LM6 (LO)")
    lm6.insert("55", {
            "effHad": (0.0,     0.0,     0.005,   0.012,  0.019,  0.022,  0.018,  0.029),
            "effMuon":scaled((0.045, 0.045, 0.1568, 0.245, 0.3254, 0.3481, 0.2836, 0.3618), 1.0e-2)})
    lm6.insert("2010_55", { #mocked up from 2011
            "effHad": (0.0,     0.0,     0.005,   0.012 + 0.019 + 0.022 + 0.018 + 0.029),
            "effMuon":scaled((0.045, 0.045, 0.1568, 0.245 + 0.3254 + 0.3481 + 0.2836 + 0.3618), 1.0e-2)})
    
    p_33_53 = common.signal(xs = 0.050740907, label = "RM1")#, label = "m_{0}=320 GeV, m_{1/2}=520 GeV (NLO)")
    p_33_53.insert("52", {
            "effHad": [0.000866, 0.000601, 0.000772, 0.001045, 0.000395, 0.001344, 0.001069, 0.013154],
            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000166, 0.000778]})
    p_33_53.insert("53", {
            "effHad": [0.001115, 0.000943, 0.001116, 0.001193, 0.001496, 0.001408, 0.002023, 0.021827],
            "effMuon":[0.000000, 8.59e-05, 0.000000, 0.000000, 0.000259, 0.000177, 0.000000, 0.001152]})
    p_33_53.insert("55", {
            "effHad": [0.008697, 0.004366, 0.004120, 0.005746, 0.007165, 0.011060, 0.014814, 0.079827],
            "effMuon":[0.000498, 0.000514, 0.000512, 0.000850, 0.000758, 0.000766, 0.001994, 0.004008]})
    p_33_53.insert("55b_mixed", {
            "effHad": [0.003522, 0.001881, 0.001108, 0.001453, 0.002007, 0.002189, 0.003275, 0.021969],
            "effMuon":[0.000334, 8.59e-05, 0.000170, 0.000494, 0.000429, 0.000343, 0.000678, 0.001018]})

    p_181_29 = common.signal(xs = 0.6430277062, label = "m_{0}=1800 GeV, m_{1/2}=280 GeV (NLO)")
    p_181_29.insert("55b_mixed", { # >=1 btag
            "effHad": [0.000271, 0.000000, 0.000765, 0.000605, 0.001009, 0.000707, 0.000807, 0.001211],
            "effMuon":[0.000000, 0.000292, 9.05e-05, 0.000292, 0.000000, 0.000201, 0.000000, 0.000000]})
    p_181_29.insert("55", {
            "effHad": [0.001630, 0.000473, 0.001420, 0.001079, 0.002310, 0.001313, 0.001211, 0.001595],
            "effMuon":[9.05e-05, 0.000382, 0.000473, 0.000382, 0.000292, 0.000909, 0.000000, 0.000000]})
    p_181_29.insert("52", {
            "effHad": [0.000362, 9.05e-05, 0.000654, 0.000181, 0.000506, 0.000201, 0.001211, 0.002422],
            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000201]})
    p_181_29.insert("53", {
            "effHad": [0.000835, 9.05e-05, 0.000362, 0.000403, 0.001192, 0.001009, 0.001009, 0.001080],
            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000201, 0.000201, 0.000000, 0.000000]})
    p_181_29.insert("55_0b", {
            "effHad": [0.000815, 0.000473, 0.000654, 0.000473, 0.001301, 0.000605, 0.000403, 0.000384],
            "effMuon":[9.05e-05, 9.05e-05, 0.000382, 9.05e-05, 0.000292, 0.000707, 0.000000, 0.000000]})
    p_181_29.insert("55_1b", {
            "effHad": [0.000181, 0.000000, 0.000675, 0.000403, 0.000201, 0.000304, 0.000605, 0.000605],
            "effMuon":[0.000000, 9.05e-05, 9.05e-05, 0.000292, 0.000000, 0.000201, 0.000000, 0.000000]})
    p_181_29.insert("55_2b", {
            "effHad": [9.05e-05, 0.000000, 0.000000, 0.000201, 0.000403, 0.000201, 0.000201, 0.000403],
            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]})
    p_181_29.insert("55_gt2b", {
            "effHad": [0.000000, 0.000000, 9.05e-05, 0.000000, 0.000403, 0.000201, 0.000000, 0.000201],
            "effMuon":[0.000000, 0.000201, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]})

    t1bbbb = common.signal(xs = 0.0087, label = "T1bbbb m_{gl} = 1 TeV; m_{LSP} = 0.5 TeV (xs = 8.7 fb)")
    t1bbbb.insert("55_0b", {
            "effHad" :[0.000000, 0.000300, 0.000900, 0.000900, 0.001800, 0.001000, 0.000600, 0.000500],
            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            })
    t1bbbb.insert("55_1b", {
            "effHad": [0.000500, 0.001200, 0.004000, 0.007100, 0.008600, 0.008000, 0.004500, 0.003200],
            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            })
    t1bbbb.insert("55_2b", {
            "effHad" :[0.001000, 0.000900, 0.006600, 0.016800, 0.018100, 0.017600, 0.009500, 0.008600],
            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            })
    t1bbbb.insert("55_gt2b", {
            "effHad":[0.000300, 0.000600, 0.004900, 0.013300, 0.026900, 0.025700, 0.015500, 0.011800],
            "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            })

    return [simple, lm6, p_33_53,  p_181_29, t1bbbb][i]

f = workspace.foo(likelihoodSpec = likelihoodSpec.spec(),
                  #signalToTest = signal(-1),
                  signalExampleToStack = signal(-1),
                  #signalToInject = signal(-1),

                  #trace = True
                  #rhoSignalMin = 0.1,
                  #fIniFactor = 0.1,
                  #extraSigEffUncSources = ["effHadSumUncRelMcStats"],
                  )

cl = 0.95 if f.likelihoodSpec.standardPoi() else 0.68
#out = f.interval(cl = cl, method = ["profileLikelihood", "feldmanCousins"][0], makePlots = True); print out
#out = f.cls(cl = cl, plusMinus = {"OneSigma": 1.0, "TwoSigma": 2.0},makePlots = True,
#            calculatorType = ["frequentist", "asymptotic", "asymptoticNom"][1],
#            testStatType = 3, nToys = 50, nWorkers = 1); print out
#f.profile()
#f.writeMlTable()
f.bestFit(printValues = True)
#f.bestFit(drawMc = False, printValues = False)
#f.bestFit(drawMc = False, printValues = False, drawComponents = False)
#f.bestFit(printPages = True)
#f.qcdPlot()
#f.pValue(nToys = 300)
#f.ensemble(nToys = 1000)
#print f.clsCustom(nToys = 500, testStatType = 1)
#f.expectedLimit(cl = 0.95, nToys = 300, plusMinus = {"OneSigma": 1.0, "TwoSigma": 2.0}, makePlots = True)
#f.debug()
