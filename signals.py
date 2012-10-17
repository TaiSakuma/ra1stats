import common

def scaled(t, factor) :
    return tuple([factor*item for item in t])

simple = common.signal(xs = 1.0, label = "signal")
simple.insert("test", {
        "effSimple": (1.0, ),
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


t1bbbb2 = common.signal(xs = 0.0087, label = "T1bbbb m_{gl} = 1 TeV; m_{LSP} = 0.2 TeV (xs = 8.7 fb)")
t1bbbb2.insert("55_0b", {
        "effHad" :[0.000100, 0.000100, 0.000100, 0.000200, 0.000300, 0.000500, 0.000500, 0.001000],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1bbbb2.insert("55_1b", {
        "effHad" :[0.000000, 0.000100, 0.000300, 0.001400, 0.002800, 0.004400, 0.005200, 0.014100],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1bbbb2.insert("55_2b", {
        "effHad" :[0.000000, 0.000000, 0.001000, 0.002100, 0.006400, 0.010700, 0.009500, 0.031000],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t1bbbb2.insert("55_gt2b", {
        "effHad" :[0.000000, 0.000000, 0.000400, 0.002100, 0.005600, 0.010300, 0.018200, 0.052600],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })

t2tt = common.signal(xs = 0.214149, label = "T2tt m_{stop} = 400 GeV; m_{LSP} = 50 GeV (xs = 214 fb)")
t2tt.insert("55_0b", {
        "effHad": [0.004570, 0.003606, 0.005535, 0.002642, 0.001300, 0.000252, 0.000084, 0.000084],
        "effMuon":[0.000755, 0.000419, 0.000545, 0.000377, 0.000042, 0.000000, 0.000000, 0.000000],
        })
t2tt.insert("55_1b", {
        "effHad": [0.008722, 0.008135, 0.012579, 0.006373, 0.003732, 0.000461, 0.000461, 0.000168],
        "effMuon":[0.001803, 0.001090, 0.001509, 0.000881, 0.000545, 0.000084, 0.000000, 0.000000],
        })
t2tt.insert("55_2b", {
        "effHad": [0.003774, 0.004445, 0.008135, 0.004445, 0.002222, 0.000713, 0.000252, 0.000335],
        "effMuon":[0.001006, 0.000545, 0.000964, 0.000252, 0.000335, 0.000042, 0.000084, 0.000084],
        })
t2tt.insert("55_gt2b", {
        "effHad": [0.000168, 0.000168, 0.000839, 0.000629, 0.000461, 0.000126, 0.000042, 0.000042],
        "effMuon":[0.000042, 0.000000, 0.000084, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })

t2tt2 = common.signal(xs = 0.214149, label = "T2tt m_{stop} = 400 GeV; m_{LSP} = 100 GeV (xs = 214 fb)")
t2tt2.insert("55_0b", {
        "effHad" :[0.005892, 0.004161, 0.003997, 0.001854, 0.000618, 0.000288, 0.000000, 0.000000],
        "effMuon":[0.001112, 0.000536, 0.000577, 0.000288, 0.000124, 0.000041, 0.000000, 0.000000],
        })
t2tt2.insert("55_1b", {
        "effHad" :[0.010342, 0.007993, 0.008281, 0.005150, 0.001978, 0.000659, 0.000124, 0.000247],
        "effMuon":[0.001936, 0.001154, 0.001112, 0.000412, 0.000165, 0.000082, 0.000124, 0.000041],
        })
t2tt2.insert("55_2b", {
        "effHad" :[0.003337, 0.003585, 0.005274, 0.003626, 0.001112, 0.000412, 0.000124, 0.000165],
        "effMuon":[0.000659, 0.000783, 0.001071, 0.000700, 0.000206, 0.000000, 0.000000, 0.000000],
        })
t2tt2.insert("55_gt2b", {
        "effHad" :[0.000412, 0.000536, 0.000536, 0.000494, 0.000124, 0.000041, 0.000041, 0.000000],
        "effMuon":[0.000000, 0.000041, 0.000000, 0.000041, 0.000041, 0.000000, 0.000000, 0.000000],
        })

t2bb = common.signal(xs = 0.1015, label = ["#lower[0.35]{#splitline{SM + SUSY Model D}{(m_{#lower[-0.20]{sbottom}} = 500 GeV, m_{#lower[-0.3]{LSP}} = 150 GeV)}}",
                                           "T2bb m_{sbottom} = 500 GeV; m_{LSP} = 150 GeV (xs = 100 fb)"][0])
t2bb.insert("55_0b", {
        "effHad": [0.003300, 0.003700, 0.006500, 0.003600, 0.002400, 0.000800, 0.000600, 0.000200],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t2bb.insert("55_1b", {
        "effHad": [0.012900, 0.017000, 0.029000, 0.020300, 0.008500, 0.003700, 0.001500, 0.001600],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t2bb.insert("55_2b", {
        "effHad": [0.013100, 0.017200, 0.035600, 0.021700, 0.008300, 0.004800, 0.001800, 0.001600],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })
t2bb.insert("55_gt2b", {
        "effHad": [0.000000, 0.000100, 0.000400, 0.000800, 0.000900, 0.000100, 0.000100, 0.000100],
        "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        })

t2bb_2 = common.signal(xs = 0.0486, label = ["#lower[0.35]{#splitline{SM + SUSY Model D}{(m_{sbottom} = 500 GeV, m_{LSP} = 150 GeV)}}",
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

t1 = common.signal(xs = 0.0651, label = ["#lower[0.35]{#splitline{SM + SUSY Model A}{(m_{#lower[-0.25]{gluino}} = 800 GeV, m_{#lower[-0.3]{LSP}} = 200 GeV)}}",
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

t1tttt_2012 = common.signal(xs=0.0243547, label="T1tttt m_{gluino} = 1000 GeV; m_{LSP} = 200GeV (xs = 24 fb)")
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
t1tttt_2012_2 = common.signal(xs=0.157399, label = "#lower[0.35]{#splitline{SM + SUSY  ( %s )}{(m_{gluino} = 800 GeV, m_{LSP} = 100 GeV)}}"%t1ttttLabel)
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

t1tttt_2012_23 = common.signal(xs=0.157399, label = "#lower[0.35]{#splitline{SM + SUSY  ( %s )}{(m_{gluino} = 800 GeV, m_{LSP} = 100 GeV)}}"%t1ttttLabel)
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

t1tttt_2012_3 = common.signal(xs=0.157399, label = "#lower[0.35]{#splitline{SM + SUSY  ( %s )}{(m_{gluino} = 800 GeV, m_{LSP} = 100 GeV)}}"%t1ttttLabel)
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
