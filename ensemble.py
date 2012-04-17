import ROOT as r
import math
import utils,plotting
from common import pdf,pseudoData

def collect(wspace, results, extraStructure = False) :
    def lMax(results) :
        #return math.exp(-results.minNll())
        return -results.minNll()

    out = {}
    out["lMax"] = lMax(results)
    funcBestFit,funcLinPropError = utils.funcCollect(wspace)
    parBestFit,parError,parMin,parMax = utils.parCollect(wspace)

    if extraStructure :
        out["funcBestFit"] = funcBestFit
        out["parBestFit"] = parBestFit
        out["parError"] = parError
        return out
    
    assert set(funcBestFit.keys()).isdisjoint(set(parBestFit.keys()))
    for d in [funcBestFit, parBestFit] :
        for key,value in d.iteritems() :
            out[key] = value
    return out

def ntupleOfFitToys(wspace = None, data = None, nToys = None, cutVar = ("",""), cutFunc = None ) :
    results = utils.rooFitResults(pdf(wspace), data)
    wspace.saveSnapshot("snap", wspace.allVars())

    obs = collect(wspace, results, extraStructure = True)

    toys = []
    for i,dataSet in enumerate(pseudoData(wspace, nToys)) :
        wspace.loadSnapshot("snap")
        #dataSet.Print("v")
        results = utils.rooFitResults(pdf(wspace), dataSet)

        if all(cutVar) and cutFunc and cutFunc(getattr(wspace,cutVar[0])(cutVar[1]).getVal()) :
            wspace.allVars().assignValueOnly(dataSet.get())
            wspace.saveSnapshot("snapA", wspace.allVars())
            return obs,results,i
        
        toys.append( collect(wspace, results) )
        utils.delete(results)
    return obs,toys

def pValue(wspace, data, nToys = 100, note = "", plots = True) :
    graph = r.TGraph()
    lMaxs = []

    obs,toys = ntupleOfFitToys(wspace, data, nToys)
    lMaxData = obs["lMax"]
    for i,toy in enumerate(toys) :
        lMaxs.append(toy["lMax"])
        graph.SetPoint(i, i, utils.indexFraction(lMaxData, lMaxs))
    
    out = utils.indexFraction(lMaxData, lMaxs)
    if plots : plotting.pValuePlots(pValue = out, lMaxData = lMaxData, lMaxs = lMaxs, graph = graph, note = note)
    return out

def parHistos(obs = None, toys = None, pars = None, shift = True) :
    histos = {}
    factor = 2.0
    for par in pars :
        mean  = obs["parBestFit"][par]
        error = obs["parError"][par]
        h = histos[par] = r.TH1D(par, par, 100, mean - factor*error, mean + factor*error)
        h.Sumw2()
        for toy in toys : h.Fill(toy[par])
    if shift : utils.shiftUnderAndOverflows(1, histos.values())
    return histos

def funcHistos(obs = None, toys = None, funcs = None, shift = True) :
    histos = {}
    factor = 3.0
    for func in funcs :
        mean  = obs["funcBestFit"][func]
        error = math.sqrt(mean)
        h = histos[func] = r.TH1D(func, func, 100, mean - factor*error, mean + factor*error)
        h.Sumw2()
        for toy in toys : h.Fill(toy[func])
    if shift : utils.shiftUnderAndOverflows(1, histos.values())
    return histos

def otherHistos(obs = None, toys = None, keys = [], shift = True) :
    histos = {}
    for key in keys :
        h = histos[key] = r.TH1D(key, key, 100, 1.0, -1.0)
        h.Sumw2()
        for toy in toys : h.Fill(toy[key])
    if shift : utils.shiftUnderAndOverflows(1, histos.values())
    return histos

def parHistos2D(obs = None, toys = None, pairs = [], suffix = "") :
    histos = {}

    for pair in pairs :
        name = "_".join(pair)
        name += suffix
        title = ";".join([""]+list(pair))
        h = histos[name] = r.TH2D(name, title, 100, 1.0, -1.0, 100, 1.0, -1.0)
        h.Sumw2()
        h.SetStats(False)
        h.SetTitleOffset(1.3)
        for toy in toys :
            if (pair[0] not in toy) or (pair[1] not in toy) : continue
            h.Fill(toy[pair[0]], toy[pair[1]])
    return histos

def ensemble(wspace, data, nToys = None, note = "", plots = True, plotsDir = "plots") :
    #obs,toys,i = ntupleOfFitToys(wspace, data, nToys, cutVar = ("var", "A_qcd"), cutFunc = lambda x:x>90.0); return toys,i
    #obs,toys,i = ntupleOfFitToys(wspace, data, nToys, cutVar = ("var", "rhoPhotZ"), cutFunc = lambda x:x>2.0); return toys,i
    obs,toys = ntupleOfFitToys(wspace, data, nToys)
    
    pHistos =    parHistos(obs = obs, toys = toys, pars = utils.parCollect(wspace)[0].keys())
    fHistos =   funcHistos(obs = obs, toys = toys, funcs = utils.funcCollect(wspace)[0].keys())
    oHistos =  otherHistos(obs = obs, toys = toys, keys = ["lMax"])
    pHistos2 = parHistos2D(obs = obs, toys = toys, pairs = [("A_qcd","k_qcd"), ("A_ewk","A_qcd"), ("A_ewk","k_qcd"), ("A_ewk","fZinv0")])

    canvas = utils.numberedCanvas()
    psFileName = "%s/ensemble_%s.ps"%(plotsDir, note)
    canvas.Print(psFileName+"[")

    utils.cyclePlot(d = pHistos, f = plotting.histoLines, canvas = canvas, psFileName = psFileName,
                       args = {"bestColor":r.kGreen, "quantileColor":r.kRed, "bestDict":obs["parBestFit"], "errorDict":obs["parError"], "errorColor":r.kGreen})
    utils.cyclePlot(d = fHistos, f = plotting.histoLines, canvas = canvas, psFileName = psFileName,
                       args = {"bestColor":r.kGreen, "quantileColor":r.kRed, "bestDict":obs["funcBestFit"], "errorColor":r.kGreen, "print":True, "latexTable": []})
    utils.cyclePlot(d = oHistos, canvas = canvas, psFileName = psFileName)
    #utils.cyclePlot(d = pHistos2, canvas = canvas, psFileName = psFileName)
        
    canvas.Print(psFileName+"]")        
    utils.ps2pdf(psFileName, sameDir = True)
    
