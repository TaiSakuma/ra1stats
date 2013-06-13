import ROOT as r
import common
from configuration.signal import pruned, processStamp

simple = common.signal(xs = 1.0, effUncRel = 0.0, label = "signal")
simple.insert("test", {
        "effSimple": (1.0, ),
        })

zeroB_le3j_ht875 = common.signal(xs = 1.0e-3, effUncRel = 0.0001, label = "0b_le3j_ht875, 100% eff. (xs = 1 fb)")
zeroB_le3j_ht875.insert("0b_le3j", {"effHad":[0.0]*7+[1.0]})

t1_1 = common.signal(xs = 0.0243547, effUncRel = 0.14,
                     label = ["SM + T1 m_{gl} = 1.0 TeV; m_{LSP} = 0.4 TeV (xs = 24 fb)",
                              "#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T1")["text"]),
                                                                  "(m_{#tilde{g}}= 1000 GeV, m_{#tilde{#chi}^{0}_{1}} = 400 GeV)")][1])
t1_1.insert("0b_ge4j", {"effHad":[0.000000, 0.000200, 0.000800, 0.005200, 0.013100, 0.024600, 0.032000, 0.065700],})
t1_1.insert("0b_le3j", {"effHad":[0.000600, 0.000800, 0.002100, 0.004000, 0.007800, 0.010700, 0.007300, 0.008000],})
t1_1.insert("1b_ge4j", {"effHad":[0.000100, 0.000000, 0.000000, 0.001100, 0.001100, 0.002200, 0.003200, 0.006000],})
t1_1.insert("1b_le3j", {"effHad":[0.000000, 0.000000, 0.000200, 0.000300, 0.000700, 0.000400, 0.000200, 0.000100],})
t1_1.insert("2b_ge4j", {"effHad":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000200, 0.000400],})
t1_1.insert("2b_le3j", {"effHad":[0.000000, 0.000000, 0.000000, 0.000000, 0.000100, 0.000000, 0.000000, 0.000000],})
t1_1.insert("3b_ge4j", {"effHad":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],})
t1_1.insert("3b_le3j", {"effHad":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],})
t1_1.insert("ge4b_ge4j",{"effHad":[0.000000, 0.000000, 0.000000],})

t2_1 = common.signal(xs = 0.0799667, effUncRel = 0.134, lineColor = r.kRed+1,
                     label = ["SM + T1 m_{sq} = 700 GeV; m_{LSP} = 200 GeV (xs = 80 fb)",
                              "#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2")["text"]),
                                                                  "(m_{#tilde{q}}= 700 GeV, m_{#tilde{#chi}^{0}_{1}} = 200 GeV)")][1])
t2_1.insert("0b_le3j", {"effHad":[0.004800, 0.006300, 0.027900, 0.044500, 0.050100, 0.037000, 0.018900, 0.011600],})

t1bbbb_1 = common.signal(xs = 0.0101744, effUncRel = 0.160, lineStyle = 5,
                         label = ["SM + T1bbbb m_{gl} = 1.1 TeV; m_{LSP} = 0.5 TeV (xs = 10 fb)",
                                  "#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T1bbbb")["text"]),
                                                                     "(m_{#tilde{g}}= 1100 GeV, m_{#tilde{#chi}^{0}_{1}} = 500 GeV)")][1])
t1bbbb_1.insert("0b_ge4j", {"effHad" :[0.000000, 0.000000, 0.000000, 0.000200, 0.000300, 0.001000, 0.000400, 0.001400],})
t1bbbb_1.insert("0b_le3j", {"effHad" :[0.000000, 0.000100, 0.000300, 0.000300, 0.000800, 0.000600, 0.000200, 0.000500],})
t1bbbb_1.insert("1b_ge4j", {"effHad" :[0.000000, 0.000000, 0.000500, 0.000600, 0.002700, 0.003700, 0.004200, 0.010000],})
t1bbbb_1.insert("1b_le3j", {"effHad" :[0.000300, 0.000800, 0.001900, 0.002200, 0.003200, 0.002600, 0.002100, 0.001800],})
t1bbbb_1.insert("2b_ge4j", {"effHad" :[0.000000, 0.000100, 0.000400, 0.002800, 0.007300, 0.010900, 0.010000, 0.019000],})
t1bbbb_1.insert("2b_le3j", {"effHad" :[0.000100, 0.000300, 0.001800, 0.004100, 0.005700, 0.004900, 0.003200, 0.004400],})
t1bbbb_1.insert("3b_ge4j", {"effHad" :[0.000000, 0.000100, 0.000600, 0.002500, 0.006800, 0.011200, 0.010100, 0.021400],})
t1bbbb_1.insert("3b_le3j", {"effHad" :[0.000000, 0.000200, 0.001200, 0.002300, 0.003800, 0.002800, 0.002200, 0.002000],})
t1bbbb_1.insert("ge4b_ge4j",{"effHad":[0.000000, 0.000000, 0.017600],})

t2tt_1 = common.signal(xs = 0.0452067, effUncRel = 0.139, label = "T2tt m_{st} = 550 GeV; m_{LSP} = 20 GeV (xs = 45 fb)")
t2tt_1.insert("0b_ge4j", {"effHad" :[0.000340, 0.000840, 0.002900, 0.005400, 0.003980, 0.002460, 0.001140, 0.000680],
                          "effMuon":[0.000140, 0.000100, 0.000300, 0.000380, 0.000160, 0.000300, 0.000040, 0.000060]})
t2tt_1.insert("0b_le3j", {"effHad" :[0.003420, 0.002620, 0.005000, 0.002940, 0.001160, 0.000380, 0.000080, 0.000020],
                          "effMuon":[0.000740, 0.000720, 0.000960, 0.000300, 0.000220, 0.000180, 0.000000, 0.000020]})
t2tt_1.insert("1b_ge4j", {"effHad" :[0.000700, 0.002040, 0.007820, 0.014240, 0.012180, 0.006900, 0.003560, 0.002440],
                          "effMuon":[0.000140, 0.000180, 0.000880, 0.000900, 0.000680, 0.000320, 0.000160, 0.000220]})
t2tt_1.insert("1b_le3j", {"effHad" :[0.004280, 0.005960, 0.009640, 0.005920, 0.002200, 0.000660, 0.000200, 0.000140],
                          "effMuon":[0.001400, 0.001380, 0.001680, 0.001300, 0.000680, 0.000320, 0.000080, 0.000200]})
t2tt_1.insert("2b_ge4j", {"effHad" :[0.000360, 0.000960, 0.004960, 0.009560, 0.007800, 0.004780, 0.003160, 0.002260],
                          "effMuon":[0.000060, 0.000080, 0.000520, 0.001000, 0.000560, 0.000280, 0.000300, 0.000200]})
t2tt_1.insert("2b_le3j", {"effHad" :[0.001720, 0.002280, 0.004320, 0.002580, 0.001080, 0.000360, 0.000080, 0.000000],
                          "effMuon":[0.000760, 0.000600, 0.000860, 0.000660, 0.000500, 0.000120, 0.000100, 0.000080]})
t2tt_1.insert("3b_ge4j", {"effHad" :[0.000060, 0.000080, 0.000640, 0.001340, 0.001360, 0.000560, 0.000400, 0.000220],
                          "effMuon":[0.000000, 0.000000, 0.000040, 0.000060, 0.000060, 0.000000, 0.000000, 0.000000]})
t2tt_1.insert("ge4b_ge4j",{"effHad" :[0.000000, 0.000000, 0.000240],
                           "effMuon":[0.000000, 0.000000, 0.000000]})

t2tt_2 = common.signal(xs = 0.305512, effUncRel = 0.139, label = "T2tt m_{st} = 410 GeV; m_{LSP} = 20 GeV (xs = 305 fb)")
t2tt_2.insert("1b_ge4j", {"effHad":[0.001480, 0.002920, 0.006900, 0.006960, 0.003540, 0.000880, 0.000300, 0.000320],
                          "effMuon":[0.000160, 0.000200, 0.000400, 0.000420, 0.000240, 0.000120, 0.000060, 0.000040],})
t2tt_2.insert("2b_ge4j", {"effHad":[0.001040, 0.002180, 0.004220, 0.004420, 0.002160, 0.001020, 0.000320, 0.000120],
                          "effMuon":[0.000060, 0.000300, 0.000400, 0.000520, 0.000280, 0.000080, 0.000060, 0.000020],})

t2tt_3 = common.signal(xs = 0.262683, effUncRel = 0.139, label = "T2tt m_{st} = 420 GeV; m_{LSP} = 20 GeV (xs = 262 fb)")
t2tt_3.insert("1b_ge4j", {"effHad":[0.001800, 0.003240, 0.007760, 0.008220, 0.004580, 0.001500, 0.000440, 0.000380],
                          "effMuon":[0.000160, 0.000180, 0.000580, 0.000660, 0.000480, 0.000020, 0.000040, 0.000040],})
t2tt_3.insert("2b_ge4j", {"effHad":[0.001220, 0.001740, 0.004380, 0.005180, 0.002720, 0.001220, 0.000340, 0.000220],
                          "effMuon":[0.000080, 0.000160, 0.000220, 0.000380, 0.000340, 0.000100, 0.000080, 0.000060],})


t2bb = common.signal(xs = 0.0452067, effUncRel = 0.131, lineColor = r.kRed+1, lineStyle = 7,
                     label = ["SM + T2bb m_{sb} = 550 GeV; m_{LSP} = 100 GeV (xs = 45 fb)",
                              "#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2bb")["text"]),
                                                                  "(m_{#tilde{b}}= 550 GeV, m_{#tilde{#chi}^{0}_{1}} = 100 GeV)")][1])
t2bb.insert("1b_le3j", {"effHad":[0.006300, 0.007900, 0.024800, 0.021300, 0.013400, 0.003900, 0.001800, 0.000900],})
t2bb.insert("2b_le3j", {"effHad":[0.005700, 0.008900, 0.023700, 0.025200, 0.011700, 0.005100, 0.001100, 0.000900],})


## old points below here ##
effUncRelOld = 0.13
t2bb_2 = common.signal(xs = 0.0486, effUncRel = effUncRelOld,
                       label = ["#lower[0.35]{#splitline{SM + SUSY Model D}{(m_{sbottom} = 500 GeV, m_{LSP} = 150 GeV)}}",
                                "T2bb m_{sbottom} = 500 GeV; m_{LSP} = 150 GeV (xs = 49 fb)"][0])
t2bb_2.insert("55_0b", {
        "effHad": [0.003599, 0.004056, 0.007274, 0.004042, 0.002711, 0.000908, 0.000688, 0.000195],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t2bb_2.insert("55_1b", {
        "effHad": [0.013004, 0.017577, 0.029381, 0.019993, 0.008749, 0.003636, 0.001679, 0.001369],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t2bb_2.insert("55_2b", {
        "effHad": [0.013788, 0.017518, 0.032410, 0.019653, 0.007640, 0.004892, 0.001398, 0.001219],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t2bb_2.insert("55_gt2b", {
        "effHad": [0.000000, 0.000123, 0.000618, 0.001586, 0.001702, 0.000179, 0.000156, 0.000228],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })

t1 = common.signal(xs = 0.0651, effUncRel = effUncRelOld,
                   label = ["#lower[0.35]{#splitline{SM + SUSY Model A}{(m_{gluino} = 800 GeV, m_{LSP} = 200 GeV)}}",
                            "T1 m_{gluino} = 800 GeV; m_{LSP} = 200 GeV (xs = 65 fb)"][0])
t1.insert("55_0b", {
    "effHad": [0.000200, 0.001200, 0.005500, 0.013000, 0.028600, 0.040800, 0.035300, 0.040400],
    })
t1.insert("55_1b", {
    "effHad": [0.000000, 0.000000, 0.000200, 0.000800, 0.001000, 0.001900, 0.002200, 0.002700],
    })
t1.insert("55_2b", {
    "effHad": [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000300],
    })
t1.insert("55_gt2b", {
    "effHad": [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000100, 0.000000, 0.000000],
    })

t1tttt_2012 = common.signal(xs=0.0243547, effUncRel = effUncRelOld,
                            label="T1tttt m_{gluino} = 1000 GeV; m_{LSP} = 200GeV (xs = 24 fb)")
t1tttt_2012.insert( "55_0b", {
        "effHad": [0.000000, 0.000000, 0.000082, 0.000439, 0.000505, 0.000805, 0.000505, 0.001351],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1tttt_2012.insert( "55_1b", {
        "effHad": [0.000000, 0.000101, 0.000223, 0.001161, 0.001688, 0.003061, 0.002830, 0.006204],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1tttt_2012.insert( "55_2b", {
        "effHad": [0.000000, 0.000037, 0.000418, 0.001075, 0.002313, 0.003854, 0.004511, 0.010442],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1tttt_2012.insert( "55_gt2b", {
        "effHad": [0.000000, 0.000000, 0.000155, 0.000893, 0.002082, 0.002905, 0.005776, 0.014815],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })

ttch = "t#bar{t} #tilde{#chi}^{0}"
t1ttttLabel = "#tilde{g}#tilde{g} #rightarrow %s %s"%(ttch, ttch)
t1tttt_2012_2 = common.signal(xs=0.157399, effUncRel = effUncRelOld,
                              label = "#lower[0.35]{#splitline{SM + SUSY  ( %s )}{(m_{gluino} = 800 GeV, m_{LSP} = 100 GeV)}}"%t1ttttLabel)
t1tttt_2012_2.insert( "55_0b", {
        "effHad": [0.000040, 0.000000, 0.000189, 0.000429, 0.001074, 0.000405, 0.000323, 0.000367],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1tttt_2012_2.insert( "55_1b", {
        "effHad": [0.000121, 0.000224, 0.000694, 0.001554, 0.002514, 0.002789, 0.001555, 0.001644],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1tttt_2012_2.insert( "55_2b", {
        "effHad": [0.000119, 0.000131, 0.000575, 0.001417, 0.003898, 0.003822, 0.003127, 0.003162],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1tttt_2012_2.insert( "55_gt2b", {
        "effHad": [0.000000, 0.000000, 0.000165, 0.001438, 0.002540, 0.003726, 0.003030, 0.003359],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })

t1tttt_2012_23 = common.signal(xs=0.157399, effUncRel = effUncRelOld,
                               label = "#lower[0.35]{#splitline{SM + SUSY  ( %s )}{(m_{gluino} = 800 GeV, m_{LSP} = 100 GeV)}}"%t1ttttLabel)
t1tttt_2012_23.insert( "55_0b", {
        "effHad": [0.000040, 0.000000, 0.000189, 0.000429, 0.001074, 0.000405, 0.000323, 0.000367],
        "effMuon":[0.000050, 0.000000, 0.000150, 0.000200, 0.000200, 0.000150, 0.000150, 0.000150],
        })
t1tttt_2012_23.insert( "55_1b", {
        "effHad": [0.000121, 0.000224, 0.000694, 0.001554, 0.002514, 0.002789, 0.001555, 0.001644],
        "effMuon":[0.000200, 0.000150, 0.000450, 0.000800, 0.001050, 0.000650, 0.000550, 0.000450],
        })
t1tttt_2012_23.insert( "55_2b", {
        "effHad": [0.000119, 0.000131, 0.000575, 0.001417, 0.003898, 0.003822, 0.003127, 0.003162],
        "effMuon":[0.000000, 0.000100, 0.000400, 0.001100, 0.001550, 0.001500, 0.000600, 0.000900],
        })
t1tttt_2012_23.insert( "55_gt2b", {
        "effHad": [0.000000, 0.000000, 0.000165, 0.001438, 0.002540, 0.003726, 0.003030, 0.003359],
        "effMuon":[0.000000, 0.000000, 0.000100, 0.000450, 0.000900, 0.001000, 0.000500, 0.001150],
        })

t1tttt_2012_3 = common.signal(xs=0.157399, effUncRel = effUncRelOld,
                              label = "#lower[0.35]{#splitline{SM + SUSY  ( %s )}{(m_{gluino} = 800 GeV, m_{LSP} = 100 GeV)}}"%t1ttttLabel)
t1tttt_2012_3.insert( "55_0b", {
        "effHad": [0.000000, 0.000000, 0.000250, 0.000350, 0.001050, 0.000400, 0.000350, 0.000400],
        "effMuon":[0.000050, 0.000000, 0.000150, 0.000200, 0.000200, 0.000150, 0.000150, 0.000150],
        })
t1tttt_2012_3.insert( "55_1b", {
        "effHad": [0.000150, 0.000200, 0.000900, 0.001550, 0.002350, 0.003250, 0.001750, 0.001900],
        "effMuon":[0.000200, 0.000150, 0.000450, 0.000800, 0.001050, 0.000650, 0.000550, 0.000450],
        })
t1tttt_2012_3.insert( "55_2b", {
        "effHad": [0.000200, 0.000150, 0.000550, 0.001750, 0.004250, 0.004000, 0.002950, 0.003300],
        "effMuon":[0.000000, 0.000100, 0.000400, 0.001100, 0.001550, 0.001500, 0.000600, 0.000900],
        })
t1tttt_2012_3.insert( "55_gt2b", {
        "effHad": [0.000000, 0.000000, 0.000200, 0.001150, 0.002450, 0.003450, 0.002650, 0.003250],
        "effMuon":[0.000000, 0.000000, 0.000100, 0.000450, 0.000900, 0.001000, 0.000500, 0.001150],
        })