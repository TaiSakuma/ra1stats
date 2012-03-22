#!/usr/bin/env python

import plottingGrid as pg

pg.makeTopologyXsLimitPlots(logZ = True,
                            names = ["UpperLimit","upperLimit95"],
                            #simpleExcl = True,
                            #drawGraphs = False,
                            #mDeltaFuncs = {"mDeltaMin":0.0, "mDeltaMax":400.0, "nSteps":4, "mGMax":1250.},
                            #printXs = True,
                            )
