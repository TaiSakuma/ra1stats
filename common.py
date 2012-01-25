def obs(w) :
    return w.set("obs")

def pdf(w) :
    return w.pdf("model")

def sampleCode(samples) :
    yes = []
    no = []
    for box,considerSignal in samples.iteritems() :
        (yes if considerSignal else no).append(box)

    d = {"had":"h", "phot":"p", "muon":"1", "mumu":"2"}
    out = ""
    for item in yes :
        out+=d[item]
    if no :
        out += "x"
        for item in no : out+=d[item]
    return out

def note(likelihoodSpec = {}) :
    l = likelihoodSpec
    out = ""
    if l["simpleOneBin"] : return "simpleOneBin"
    
    if l["REwk"] : out += "REwk%s_"%l["REwk"]
    out += "RQcd%s"%l["RQcd"]
    if l["constrainQcdSlope"] : out += "Ext"

    out += "_fZinv%s"%l["nFZinv"]
    if l["qcdSearch"] :  out += "_qcdSearch"

    for selection in l["selections"] :
        out += "_%s%s"%(selection.name, sampleCode(selection.samplesAndSignalEff))
    return out
