from signals import common,pruned,processStamp

t1bbbb_1200_1025_cteq61 = common.signal(xs = 0.00440078, effUncRel = 0.160,
                       label = "#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T1bbbb")["text"]),
                                                                   "(m_{#tilde{g}}= 1200 GeV, m_{#tilde{#chi}^{0}_{1}} = 1025 GeV)"))
t1bbbb_1200_1025_cteq61.insert("2b_ge4j",{"effHad":[0.003200, 0.002100, 0.002200, 0.002700, 0.001400, 0.000700, 0.000800, 0.001200],
                                          "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],})
t1bbbb_1200_1025_cteq61.insert("3b_ge4j",{"effHad":[0.002900, 0.001500, 0.001800, 0.000900, 0.000600, 0.000500, 0.000600, 0.000600],
                                          "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],})
t1bbbb_1200_1025_cteq61.insert("ge4b_ge4j",{"effHad":[0.000400, 0.000300, 0.000800],
                                            "effMuon":[0.000000, 0.000000, 0.000000],})

t1bbbb_1200_1025_cteq66 = common.signal(xs = 0.00440078, effUncRel = 0.160,
                       label = "#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T1bbbb")["text"]),
                                                                   "(m_{#tilde{g}}= 1200 GeV, m_{#tilde{#chi}^{0}_{1}} = 1025 GeV)"))
t1bbbb_1200_1025_cteq66.insert("2b_ge4j",{"effHad":[0.002950, 0.001776, 0.002007, 0.003198, 0.001659, 0.000747, 0.001394, 0.002337],
                                          "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],})
t1bbbb_1200_1025_cteq66.insert("3b_ge4j",{"effHad":[0.002558, 0.001169, 0.001669, 0.000746, 0.000501, 0.000601, 0.000951, 0.001123],
                                          "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],})
t1bbbb_1200_1025_cteq66.insert("ge4b_ge4j",{"effHad":[0.000244, 0.000166, 0.001427],
                                            "effMuon":[0.000000, 0.000000, 0.000000],})


t1bbbb_1225_1050_cteq61 = common.signal(xs = 0.00357858, effUncRel = 0.160,
                       label = "#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T1bbbb")["text"]),
                                                                   "(m_{#tilde{g}}= 1225 GeV, m_{#tilde{#chi}^{0}_{1}} = 1050 GeV)"))
t1bbbb_1225_1050_cteq61.insert("2b_ge4j",{"effHad":[0.004000, 0.003400, 0.003600, 0.002500, 0.001900, 0.000700, 0.000800, 0.001100],
                                          "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],})
t1bbbb_1225_1050_cteq61.insert("3b_ge4j",{"effHad":[0.002800, 0.002000, 0.001200, 0.001600, 0.000600, 0.000800, 0.000500, 0.000700],
                                          "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],})
t1bbbb_1225_1050_cteq61.insert("ge4b_ge4j",{"effHad":[0.000900, 0.000500, 0.001400],
                                            "effMuon":[0.000000, 0.000000, 0.000000],})

t1bbbb_1225_1050_cteq66 = common.signal(xs = 0.00357858, effUncRel = 0.160,
                       label = "#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T1bbbb")["text"]),
                                                                   "(m_{#tilde{g}}= 1225 GeV, m_{#tilde{#chi}^{0}_{1}} = 1050 GeV)"))
t1bbbb_1225_1050_cteq66.insert("2b_ge4j",{"effHad":[0.003003, 0.002763, 0.003816, 0.003531, 0.002742, 0.000862, 0.000727, 0.002197],
                                          "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],})
t1bbbb_1225_1050_cteq66.insert("3b_ge4j",{"effHad":[0.001852, 0.001853, 0.001680, 0.001514, 0.000652, 0.000917, 0.000536, 0.000921],
                                          "effMuon":[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],})
t1bbbb_1225_1050_cteq66.insert("ge4b_ge4j",{"effHad":[0.000556, 0.000247, 0.001450],
                                            "effMuon":[0.000000, 0.000000, 0.000000],})