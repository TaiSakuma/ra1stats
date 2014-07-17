import math
from configuration.signal import pruned, processStamp
from inputData import pb
from . import point


dm10_225 = point(xs=9.9*pb, sumWeightIn=709041, x=225.0, y=215.0,
             label="#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2cc")["text"])  + "(xs = %s pb)"% (9.9*pb),
                                                       "(m_{#tilde{t}}= 225 GeV, m_{#tilde{#chi}^{0}_{1}} = 215 GeV)"))
dm10_225.insert("0b_ge4j", {
    "effHad":    [2.36e-06, 4.43e-05, 9.52e-05, 1.61e-04, 1.67e-04, 1.03e-04, 7.19e-05, 4.20e-05, 1.06e-05, 8.15e-06, 1.08e-05],
    "effHadErr": [1.71e-06, 6.86e-06, 1.01e-05, 1.25e-05, 1.37e-05, 1.01e-05, 9.81e-06, 6.46e-06, 3.13e-06, 2.68e-06, 3.30e-06],
    "effHadSum": 0.000715671,
    "effUncRel": 0.248298,
    })
dm10_225.insert("0b_le3j", {
    "effHad":    [3.27e-03, 1.79e-03, 1.28e-03, 1.29e-03, 5.70e-04, 2.05e-04, 1.01e-04, 4.85e-05, 1.80e-05, 9.27e-06, 1.59e-06],
    "effHadErr": [5.96e-05, 4.32e-05, 3.75e-05, 3.58e-05, 2.42e-05, 1.42e-05, 9.99e-06, 7.02e-06, 4.30e-06, 3.15e-06, 1.13e-06],
    "effHadSum": 0.00857845,
    "effUncRel": 0.201592,
    })
dm10_225.insert("1b_ge4j", {
    "effHad":    [0.00e+00, 8.37e-06, 1.42e-05, 2.33e-05, 2.43e-05, 2.36e-05, 1.27e-05, 3.75e-06, 6.70e-06, 1.83e-06, 2.15e-06],
    "effHadErr": [0.00e+00, 2.77e-06, 3.92e-06, 4.99e-06, 4.82e-06, 5.03e-06, 3.55e-06, 1.90e-06, 2.82e-06, 1.31e-06, 1.53e-06],
    "effHadSum": 0.000120884,
    "effUncRel": 0.241425,
    })

dm40_225 = point(xs=9.9*pb, sumWeightIn=703696, x=225.0, y=185.0,
             label="#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2cc")["text"])  + "(xs = %s pb)"% (9.9*pb),
                                                       "(m_{#tilde{t}}= 225 GeV, m_{#tilde{#chi}^{0}_{1}} = 185 GeV)"))
dm40_225.insert("0b_ge4j", {
    "effHad":    [1.76e-06, 5.32e-05, 1.45e-04, 2.15e-04, 2.66e-04, 1.46e-04, 9.03e-05, 3.43e-05, 1.88e-05, 1.19e-05, 5.77e-06],
    "effHadErr": [1.25e-06, 7.51e-06, 1.41e-05, 1.59e-05, 1.76e-05, 1.22e-05, 9.55e-06, 5.97e-06, 4.19e-06, 3.31e-06, 2.24e-06],
    "effHadSum": 0.000988556,
    "effUncRel": 0.241227,
    })
dm40_225.insert("0b_le3j", {
    "effHad":    [1.75e-03, 9.37e-04, 7.01e-04, 6.85e-04, 2.67e-04, 9.75e-05, 4.14e-05, 1.22e-05, 8.23e-06, 1.33e-06, 2.23e-06],
    "effHadErr": [4.43e-05, 3.20e-05, 2.81e-05, 2.64e-05, 1.65e-05, 9.83e-06, 6.48e-06, 3.47e-06, 2.83e-06, 1.33e-06, 1.57e-06],
    "effHadSum": 0.0045058,
    "effUncRel": 0.179097,
    })
dm40_225.insert("1b_ge4j", {
    "effHad":    [0.00e+00, 1.37e-05, 4.32e-05, 7.29e-05, 7.90e-05, 7.19e-05, 3.19e-05, 2.30e-05, 7.63e-06, 4.04e-06, 4.63e-06],
    "effHadErr": [0.00e+00, 3.91e-06, 6.74e-06, 8.60e-06, 9.00e-06, 8.83e-06, 5.67e-06, 4.69e-06, 2.76e-06, 1.89e-06, 2.10e-06],
    "effHadSum": 0.000351936,
    "effUncRel": 0.247601,
    })


dm80_225 = point(xs=9.9*pb, sumWeightIn=732283, x=225.0, y=145.0,
             label="#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2cc")["text"])  + "(xs = %s pb)"% (9.9*pb),
                                                       "(m_{#tilde{t}}= 225 GeV, m_{#tilde{#chi}^{0}_{1}} = 145 GeV)"))
dm80_225.insert("0b_ge4j", {
    "effHad":    [2.16e-06, 8.63e-05, 2.23e-04, 3.28e-04, 2.32e-04, 1.55e-04, 7.29e-05, 3.34e-05, 1.74e-05, 7.93e-06, 1.11e-05],
    "effHadErr": [1.55e-06, 9.49e-06, 1.76e-05, 1.96e-05, 1.51e-05, 1.22e-05, 8.14e-06, 6.46e-06, 4.23e-06, 2.68e-06, 3.13e-06],
    "effHadSum": 0.00116948,
    "effUncRel": 0.204835,
    })
dm80_225.insert("0b_le3j", {
    "effHad":    [2.45e-03, 1.16e-03, 9.38e-04, 7.62e-04, 2.24e-04, 7.27e-05, 2.81e-05, 1.03e-05, 4.87e-06, 8.46e-07, 6.41e-07],
    "effHadErr": [5.38e-05, 3.64e-05, 3.25e-05, 2.79e-05, 1.53e-05, 8.37e-06, 5.18e-06, 2.99e-06, 2.19e-06, 8.46e-07, 6.41e-07],
    "effHadSum": 0.00565267,
    "effUncRel": 0.125507,
    })
dm80_225.insert("1b_ge4j", {
    "effHad":    [2.62e-06, 5.76e-05, 1.04e-04, 1.57e-04, 1.21e-04, 7.29e-05, 3.37e-05, 1.96e-05, 1.15e-05, 6.38e-06, 8.19e-06],
    "effHadErr": [1.85e-06, 8.11e-06, 1.06e-05, 1.27e-05, 1.08e-05, 8.34e-06, 5.78e-06, 4.29e-06, 3.46e-06, 2.63e-06, 2.69e-06],
    "effHadSum": 0.000594499,
    "effUncRel": 0.198575,
    })

dm10_250 = point(xs = 5.6*pb, sumWeightIn=473154, x=250.0, y=240.0,                 
             label="#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2cc")["text"])  + "(xs = %s pb)"% (5.6*pb),
                                                       "(m_{#tilde{t}}= 250 GeV, m_{#tilde{#chi}^{0}_{1}} = 240 GeV)"))
dm10_250.insert("0b_ge4j", {
    "effHad":    [1.73e-06, 4.85e-05, 1.20e-04, 1.90e-04, 2.15e-04, 1.15e-04, 7.62e-05, 5.74e-05, 2.65e-05, 1.97e-05, 2.04e-05],
    "effHadErr": [1.73e-06, 8.79e-06, 1.39e-05, 1.69e-05, 1.78e-05, 1.29e-05, 1.06e-05, 9.31e-06, 6.35e-06, 5.21e-06, 5.65e-06],
    "effHadSum": 0.000891092,
    "effUncRel": 0.247963,
    })
dm10_250.insert("0b_le3j", {
    "effHad":    [3.73e-03, 2.01e-03, 1.51e-03, 1.52e-03, 7.07e-04, 2.77e-04, 1.42e-04, 3.34e-05, 2.57e-05, 1.42e-05, 7.89e-06],
    "effHadErr": [7.89e-05, 5.67e-05, 5.03e-05, 4.78e-05, 3.27e-05, 2.10e-05, 1.45e-05, 6.84e-06, 6.64e-06, 4.33e-06, 3.65e-06],
    "effHadSum": 0.00998344,
    "effUncRel": 0.201049,
    })
dm10_250.insert("1b_ge4j", {
    "effHad":    [0.00e+00, 7.14e-06, 2.37e-05, 2.19e-05, 2.29e-05, 1.21e-05, 3.77e-06, 1.01e-05, 2.50e-06, 2.86e-06, 2.69e-06],
    "effHadErr": [0.00e+00, 3.59e-06, 5.98e-06, 5.80e-06, 5.47e-06, 3.74e-06, 2.21e-06, 3.92e-06, 1.82e-06, 2.03e-06, 1.92e-06],
    "effHadSum": 0.000109667,
    "effUncRel": 0.241079,
    })
dm10_250.insert("1b_le3j", {
    "effHad":    [2.77e-04, 1.78e-04, 1.13e-04, 1.41e-04, 5.05e-05, 3.50e-05, 1.03e-05, 2.17e-06, 1.34e-06, 0.00e+00, 0.00e+00],
    "effHadErr": [2.27e-05, 1.68e-05, 1.34e-05, 1.47e-05, 8.71e-06, 7.71e-06, 3.59e-06, 2.17e-06, 1.34e-06, 0.00e+00, 0.00e+00],
    "effHadSum": 0.000807689,
    "effUncRel": 0.25
    })


dm40_250 = point(xs=5.6, sumWeightIn=471004, x=250.0, y=210.0,
             label="#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2cc")["text"]) + "(xs = %s pb)"% (5.6*pb),
                                                       "(m_{#tilde{t}}= 250 GeV, m_{#tilde{#chi}^{0}_{1}} = 210 GeV)"))
dm40_250.insert("0b_ge4j", {
    "effHad":    [9.15e-07, 6.79e-05, 1.68e-04, 2.67e-04, 2.86e-04, 1.82e-04, 1.12e-04, 6.63e-05, 3.44e-05, 1.60e-05, 1.22e-05],
    "effHadErr": [9.15e-07, 1.05e-05, 1.62e-05, 2.07e-05, 2.10e-05, 1.81e-05, 1.31e-05, 1.01e-05, 7.07e-06, 4.52e-06, 3.97e-06],
    "effHadSum": 0.00121234,
    "effUncRel": 0.233743,
    })
dm40_250.insert("0b_le3j", {
    "effHad":    [2.04e-03, 1.16e-03, 8.88e-04, 8.69e-04, 3.61e-04, 1.28e-04, 5.57e-05, 2.13e-05, 5.65e-06, 2.80e-06, 3.95e-06],
    "effHadErr": [5.80e-05, 4.31e-05, 3.79e-05, 3.65e-05, 2.30e-05, 1.41e-05, 9.27e-06, 5.70e-06, 2.85e-06, 1.98e-06, 2.28e-06],
    "effHadSum": 0.00553821,
    "effUncRel": 0.177974,
    })
dm40_250.insert("1b_ge4j", {
    "effHad":    [1.50e-06, 2.35e-05, 6.00e-05, 1.00e-04, 1.00e-04, 7.46e-05, 3.30e-05, 1.94e-05, 1.70e-05, 6.73e-06, 1.10e-05],
    "effHadErr": [1.50e-06, 6.06e-06, 9.53e-06, 1.25e-05, 1.23e-05, 1.27e-05, 6.97e-06, 5.28e-06, 5.08e-06, 3.04e-06, 4.20e-06],
    "effHadSum": 0.000447605,
    "effUncRel": 0.242833,
    })


dm80_250 = point(xs = 5.6*pb, sumWeightIn=471804, x=250.0, y=170.0,
             label="#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2cc")["text"]) + "(xs = %s pb)"% (5.6*pb),
                                                       "(m_{#tilde{t}}= 250 GeV, m_{#tilde{#chi}^{0}_{1}} = 170 GeV)"))
dm80_250.insert("0b_ge4j", {
    "effHad":    [1.98e-06, 1.43e-04, 2.57e-04, 4.15e-04, 3.66e-04, 1.91e-04, 9.70e-05, 5.36e-05, 2.43e-05, 8.16e-06, 1.79e-05],
    "effHadErr": [1.98e-06, 1.60e-05, 2.10e-05, 2.60e-05, 2.44e-05, 1.69e-05, 1.28e-05, 1.16e-05, 6.19e-06, 3.20e-06, 5.25e-06],
    "effHadSum": 0.00157364,
    "effUncRel": 0.207536,
    })
dm80_250.insert("0b_le3j", {
    "effHad":    [2.87e-03, 1.49e-03, 1.16e-03, 9.01e-04, 3.20e-04, 1.07e-04, 3.20e-05, 9.01e-06, 4.39e-06, 0.00e+00, 5.63e-06],
    "effHadErr": [7.24e-05, 5.07e-05, 4.48e-05, 3.91e-05, 2.25e-05, 1.29e-05, 6.82e-06, 3.50e-06, 2.55e-06, 0.00e+00, 2.85e-06],
    "effHadSum": 0.00689913,
    "effUncRel": 0.121813,
    })
dm80_250.insert("1b_ge4j", {
    "effHad":    [8.74e-07, 5.61e-05, 1.13e-04, 2.13e-04, 1.79e-04, 1.36e-04, 4.75e-05, 1.95e-05, 9.05e-06, 9.18e-06, 4.76e-06],
    "effHadErr": [8.74e-07, 9.62e-06, 1.37e-05, 1.86e-05, 1.71e-05, 1.50e-05, 8.19e-06, 5.29e-06, 3.56e-06, 3.76e-06, 2.46e-06],
    "effHadSum": 0.000788214,
    "effUncRel": 0.212249,
    })
dm80_250.insert("1b_le3j", {
    "effHad":    [7.86e-04, 4.48e-04, 3.57e-04, 3.20e-04, 8.96e-05, 4.75e-05, 1.02e-05, 0.00e+00, 1.68e-06, 1.76e-06, 0.00e+00],
    "effHadErr": [3.70e-05, 2.77e-05, 2.39e-05, 2.25e-05, 1.15e-05, 8.47e-06, 4.03e-06, 0.00e+00, 1.68e-06, 1.76e-06, 0.00e+00],
    "effHadSum": 0.00206235,
    "effUncRel": 0.144643,
    })

dm80_200 = point(xs = 18.5*pb, sumWeightIn=514714, x=200.0, y=120.0,
             label="#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2cc")["text"]) + "(xs = %s pb)"% (18.5*pb),
                                                       "(m_{#tilde{t}}= 200 GeV, m_{#tilde{#chi}^{0}_{1}} = 120 GeV)"))
dm80_200.insert("0b_ge4j", {
    "effHad":    [4.22e-06, 9.39e-05, 1.77e-04, 2.63e-04, 2.05e-04, 9.72e-05, 4.48e-05, 2.62e-05, 1.58e-05, 6.86e-06, 8.10e-06],
    "effHadErr": [2.45e-06, 1.22e-05, 1.61e-05, 2.06e-05, 1.72e-05, 1.13e-05, 9.01e-06, 5.75e-06, 4.86e-06, 3.11e-06, 3.37e-06],
    "effHadSum": 0.000943068,
    "effUncRel": 0.198166,
    })
dm80_200.insert("0b_le3j", {
    "effHad":    [2.08e-03, 9.28e-04, 7.64e-04, 5.88e-04, 2.05e-04, 4.86e-05, 1.57e-05, 4.31e-06, 4.53e-06, 1.36e-06, 0.00e+00],
    "effHadErr": [5.89e-05, 4.00e-05, 3.44e-05, 3.01e-05, 1.71e-05, 8.44e-06, 4.59e-06, 2.49e-06, 2.62e-06, 1.36e-06, 0.00e+00],
    "effHadSum": 0.00463469,
    "effUncRel": 0.117741,
    })
dm80_200.insert("1b_ge4j", {
    "effHad":    [1.75e-06, 2.86e-05, 8.16e-05, 9.58e-05, 9.18e-05, 3.78e-05, 1.70e-05, 6.62e-06, 3.46e-06, 9.23e-07, 4.06e-06],
    "effHadErr": [1.75e-06, 6.66e-06, 1.13e-05, 1.19e-05, 1.13e-05, 8.40e-06, 4.71e-06, 3.05e-06, 2.04e-06, 9.23e-07, 2.42e-06],
    "effHadSum": 0.00036937,
    "effUncRel": 0.193527,
    })
dm80_200.insert("1b_le3j", {
    "effHad":    [5.42e-04, 2.69e-04, 2.40e-04, 1.90e-04, 5.25e-05, 1.87e-05, 4.92e-06, 1.12e-06, 1.74e-06, 3.17e-06, 0.00e+00],
    "effHadErr": [3.02e-05, 2.03e-05, 1.94e-05, 1.70e-05, 8.55e-06, 4.93e-06, 2.49e-06, 1.12e-06, 1.74e-06, 2.28e-06, 0.00e+00],
    "effHadSum": 0.00132232,
    "effUncRel": 0.107105,
    })


dm10_275 = point(xs=3.28, sumWeightIn=408334, x=275.0, y=265.0,
                  label="#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2cc")["text"])  + "(xs = %s pb)"% (3.28*pb),
                                                            "(m_{#tilde{t}}= 275 GeV, m_{#tilde{#chi}^{0}_{1}} = 265 GeV)"))
dm10_275.insert("0b_ge4j", {
    "effHad":    [1.91e-06, 5.66e-05, 1.13e-04, 2.41e-04, 2.56e-04, 1.47e-04, 1.15e-04, 5.35e-05, 2.73e-05, 9.83e-06, 1.43e-05],
    "effHadErr": [1.91e-06, 9.73e-06, 1.43e-05, 2.05e-05, 2.11e-05, 1.53e-05, 1.42e-05, 9.75e-06, 6.99e-06, 4.06e-06, 4.85e-06],
    "effHadSum": 0.00103485,
    "effUncRel": 0.249004,
    })
dm10_275.insert("0b_le3j", {
    "effHad":    [4.07e-03, 2.40e-03, 1.74e-03, 1.82e-03, 8.56e-04, 3.99e-04, 1.97e-04, 8.14e-05, 3.48e-05, 1.79e-05, 1.65e-05],
    "effHadErr": [8.89e-05, 6.61e-05, 5.59e-05, 5.65e-05, 3.97e-05, 2.78e-05, 1.85e-05, 1.16e-05, 8.07e-06, 5.50e-06, 5.37e-06],
    "effHadSum": 0.0116179,
    "effUncRel": 0.204474,
    })
dm10_275.insert("1b_ge4j", {
    "effHad":    [0.00e+00, 9.84e-06, 1.66e-05, 2.91e-05, 4.30e-05, 2.94e-05, 1.73e-05, 4.95e-06, 8.51e-06, 3.13e-06, 0.00e+00],
    "effHadErr": [0.00e+00, 4.11e-06, 5.45e-06, 7.36e-06, 1.05e-05, 7.20e-06, 5.66e-06, 2.87e-06, 3.87e-06, 2.22e-06, 0.00e+00],
    "effHadSum": 0.000161927,
    "effUncRel": 0.248418,
    })

dm40_275 = point(xs=3.28, sumWeightIn=427572, x=275.0, y=235.0,
                         label="#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2cc")["text"])  + "(xs = %s pb)"% (3.28*pb),
                                                                   "(m_{#tilde{t}}= 275 GeV, m_{#tilde{#chi}^{0}_{1}} = 235 GeV)"))
dm40_275.insert("0b_ge4j", {
    "effHad":    [0.00e+00, 6.52e-05, 1.87e-04, 3.42e-04, 3.46e-04, 2.23e-04, 1.31e-04, 5.31e-05, 4.90e-05, 1.86e-05, 3.30e-05],
    "effHadErr": [0.00e+00, 1.09e-05, 1.86e-05, 2.45e-05, 2.41e-05, 1.94e-05, 1.48e-05, 9.06e-06, 8.97e-06, 5.73e-06, 7.32e-06],
    "effHadSum": 0.00144809,
    "effUncRel": 0.245146,
    })
dm40_275.insert("0b_le3j", {
    "effHad":    [2.27e-03, 1.32e-03, 1.07e-03, 1.08e-03, 3.94e-04, 1.71e-04, 6.90e-05, 2.43e-05, 5.53e-06, 4.52e-06, 2.70e-06],
    "effHadErr": [6.50e-05, 4.96e-05, 4.33e-05, 4.46e-05, 2.67e-05, 1.70e-05, 1.03e-05, 6.29e-06, 3.20e-06, 2.73e-06, 2.00e-06],
    "effHadSum": 0.00641402,
    "effUncRel": 0.182824,
    })
dm40_275.insert("1b_ge4j", {
    "effHad":    [0.00e+00, 2.92e-05, 7.54e-05, 1.06e-04, 1.14e-04, 9.69e-05, 5.50e-05, 1.87e-05, 1.57e-05, 1.30e-05, 1.56e-05],
    "effHadErr": [0.00e+00, 7.57e-06, 1.15e-05, 1.30e-05, 1.36e-05, 1.24e-05, 9.66e-06, 5.39e-06, 5.02e-06, 4.49e-06, 5.29e-06],
    "effHadSum": 0.000539189,
    "effUncRel": 0.250003,
    })


dm80_275 = point(xs=3.28, sumWeightIn=398721, x=275.0, y=195.0,
                  label="#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2cc")["text"])  + "(xs = %s pb)"% (3.28*pb),
                                                            "(m_{#tilde{t}}= 275 GeV, m_{#tilde{#chi}^{0}_{1}} = 195 GeV)"))
dm80_275.insert("0b_ge4j", {
    "effHad":    [0.00e+00, 1.94e-04, 3.17e-04, 4.94e-04, 4.43e-04, 2.91e-04, 1.21e-04, 7.40e-05, 3.33e-05, 3.12e-06, 2.12e-05],
    "effHadErr": [0.00e+00, 2.03e-05, 2.56e-05, 3.09e-05, 3.02e-05, 2.35e-05, 1.56e-05, 1.14e-05, 7.64e-06, 2.22e-06, 5.75e-06],
    "effHadSum": 0.00199123,
    "effUncRel": 0.204577,
    })
dm80_275.insert("0b_le3j", {
    "effHad":    [3.40e-03, 1.59e-03, 1.32e-03, 1.22e-03, 3.99e-04, 1.20e-04, 5.39e-05, 2.50e-05, 1.89e-06, 2.06e-06, 5.16e-06],
    "effHadErr": [8.68e-05, 5.68e-05, 5.12e-05, 4.88e-05, 2.73e-05, 1.45e-05, 9.87e-06, 6.73e-06, 1.89e-06, 2.06e-06, 2.99e-06],
    "effHadSum": 0.00813493,
    "effUncRel": 0.122513,
    })
dm80_275.insert("1b_ge4j", {
    "effHad":    [2.03e-06, 8.94e-05, 1.52e-04, 2.11e-04, 2.37e-04, 1.08e-04, 4.82e-05, 3.80e-05, 1.98e-05, 1.00e-05, 9.97e-06],
    "effHadErr": [2.03e-06, 1.32e-05, 1.73e-05, 1.99e-05, 2.31e-05, 1.39e-05, 8.79e-06, 7.80e-06, 5.67e-06, 4.13e-06, 3.79e-06],
    "effHadSum": 0.000926305,
    "effUncRel": 0.205565,
    })


dm80_350 = point(xs=0.81, sumWeightIn=376322, x=350.0, y=270.0,
             label="#lower[0.25]{#splitline{%s}{%s}}"%("SM + "+pruned(processStamp("T2cc")["text"]) + "(xs = %s pb)"% (0.81*pb),
                                                       "(m_{#tilde{t}}= 350 GeV, m_{#tilde{#chi}^{0}_{1}} = 270 GeV)"))
dm80_350.insert("0b_ge4j", {
    "effHad":    [6.31e-06, 2.09e-04, 5.26e-04, 8.18e-04, 7.35e-04, 4.81e-04, 2.59e-04, 1.69e-04, 7.52e-05, 5.20e-05, 5.44e-05],
    "effHadErr": [3.69e-06, 2.16e-05, 3.62e-05, 4.36e-05, 3.83e-05, 3.02e-05, 2.22e-05, 1.75e-05, 1.18e-05, 1.02e-05, 1.01e-05],
    "effHadSum": 0.0033843,
    "effUncRel": 0.215755,
    })
dm80_350.insert("0b_le3j", {
    "effHad":    [4.44e-03, 2.29e-03, 1.86e-03, 1.46e-03, 5.97e-04, 2.16e-04, 8.80e-05, 3.22e-05, 2.17e-05, 7.79e-06, 3.45e-06],
    "effHadErr": [1.01e-04, 6.99e-05, 6.43e-05, 5.46e-05, 3.40e-05, 2.06e-05, 1.28e-05, 8.34e-06, 6.25e-06, 3.68e-06, 2.47e-06],
    "effHadSum": 0.0110032,
    "effUncRel": 0.125603,
    })
dm80_350.insert("1b_ge4j", {
    "effHad":    [8.26e-06, 1.16e-04, 2.61e-04, 3.45e-04, 3.86e-04, 2.34e-04, 1.23e-04, 7.42e-05, 2.25e-05, 2.12e-05, 3.24e-05],
    "effHadErr": [4.25e-06, 1.56e-05, 2.38e-05, 2.64e-05, 3.03e-05, 2.12e-05, 1.52e-05, 1.49e-05, 5.93e-06, 6.35e-06, 7.97e-06],
    "effHadSum": 0.00162408,
    "effUncRel": 0.210015,
    })
dm80_350.insert("1b_le3j", {
    "effHad":    [1.42e-03, 8.45e-04, 6.96e-04, 5.13e-04, 1.96e-04, 8.04e-05, 2.21e-05, 4.20e-06, 1.92e-06, 3.37e-06, 0.00e+00],
    "effHadErr": [5.88e-05, 4.19e-05, 3.87e-05, 3.15e-05, 2.30e-05, 1.21e-05, 6.44e-06, 2.61e-06, 1.92e-06, 2.42e-06, 0.00e+00],
    "effHadSum": 0.00378025,
    "effUncRel": 0.139954,
    })

bin0 = point(xs = 0.1*pb, sumWeightIn=473154, x=0.0, y=0.0,                 
             label="foo")

bin0.insert("0b_le3j", {
    "effHad":    [0.5] + [0.0]*10,
    #"effHadErr": [0.0] * 11,
    #"effHadSum": 0.5,
    "effUncRel": 0.01,
    })

