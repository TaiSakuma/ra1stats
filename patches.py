import collections

def cmssmCut(iX, x, iY, y, iZ, z) :
    def yMin(x) :
        return 450.0 - (300.0)*(x-500.0)/(1200.0-500.0)

    def yMax(x) :
        return 750.0 - (250.0)*(x-500.0)/(1200.0-500.0)

    if 0.0 <= x <=  500.0 :
        return  500.0 <= y <= 700.0

    if  500.0 <= x <= 1200.0 :
        return yMin(x) <= y <= yMax(x)

    if 1200.0 <= x <= 1500.0:
        return 200.0 <= y <= 450.0

    if 1500.0 <= x:
        return 200.0 <= y <= 400.0

def cutFunc() :
    return {"T1":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>299.9),
            "T2":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>299.9),
            "T2tt":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>299.9),
            "T2bb":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>299.9),
            "T5zz":lambda iX,x,iY,y,iZ,z:(y<(x-200.1) and iZ==1 and x>399.9),
            "T1bbbb":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>299.9),
            "T1tttt":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>299.9),
            "T1tttt_2012":lambda iX,x,iY,y,iZ,z:(y<(x-150.1) and iZ==1 and x>299.9),
            "tanBeta10":cmssmCut,
            }

def curves() :
    return {"tanBeta10":{
            ("ExpectedUpperLimit",          "default"): [( 160, 590), ( 240, 590), ( 320, 587), ( 400, 580), ( 480, 567),
                                                         ( 560, 550), ( 640, 530), ( 720, 500), ( 800, 465), ( 880, 423),
                                                         ( 960, 370), (1040, 342), (1120, 325), (1200, 310), (1280, 300),
                                                         (1360, 295), (1440, 293), (1520, 290), (1600, 287), (1680, 285),
                                                         (1760, 283), (1840, 280), (1920, 275), (2000, 269), (2080, 265),
                                                         (2160, 262), (2240, 260), (2320, 260), (2400, 260), (2480, 260),
                                                         (2560, 260), (2640, 265), (2720, 273), (2800, 282), (2880, 290),
                                                         (2960, 300),],
            ("ExpectedUpperLimit_-1_Sigma", "default"): [( 160, 630), ( 240, 635), ( 320, 635), ( 400, 630), ( 480, 620),
                                                         ( 560, 608), ( 640, 590), ( 720, 565), ( 800, 535), ( 880, 500),
                                                         ( 960, 440), (1040, 380), (1120, 365), (1200, 360), (1280, 350),
                                                         (1360, 340), (1440, 330), (1520, 328), (1600, 325), (1680, 322),
                                                         (1760, 321), (1840, 319), (1920, 315), (2000, 310), (2080, 305),
                                                         (2160, 300), (2240, 295), (2320, 292), (2400, 290), (2480, 290),
                                                         (2560, 290), (2640, 294), (2720, 300), (2800, 305), (2880, 310),
                                                         (2960, 315),],
            ("ExpectedUpperLimit_+1_Sigma", "default"): [( 160, 570), ( 240, 570), ( 320, 565), ( 400, 550), ( 480, 530),
                                                         ( 560, 505), ( 640, 475), ( 720, 430), ( 800, 390), ( 880, 360),
                                                         ( 960, 336), (1040, 320), (1120, 300), (1200, 280), (1280, 265),
                                                         (1360, 260), (1440, 254), (1520, 250), (1600, 250), (1680, 250),
                                                         (1760, 250), (1840, 250), (1920, 250), (2000, 249), (2080, 247),
                                                         (2160, 244), (2240, 240), (2320, 237), (2400, 235), (2480, 235),
                                                         (2560, 237), (2640, 250), (2720, 265), (2800, 275), (2880, 285),
                                                         (2960, 295),],
            ("UpperLimit",                  "default"): [( 160, 630), ( 240, 630), ( 320, 625), ( 400, 610), ( 480, 590),
                                                         ( 560, 570), ( 640, 545), ( 720, 520), ( 800, 490), ( 880, 448),
                                                         ( 960, 392), (1040, 355), (1120, 338), (1200, 328), (1280, 319),
                                                         (1360, 309), (1440, 300), (1520, 295), (1600, 292), (1680, 290),
                                                         (1760, 290), (1840, 289), (1920, 287), (2000, 286), (2080, 283),
                                                         (2160, 280), (2240, 280), (2320, 280), (2400, 280), (2480, 280),
                                                         (2560, 280), (2640, 280), (2720, 283), (2800, 285), (2880, 290),
                                                         (2960, 300),],
            ("UpperLimit",                  "up"     ): [( 160, 630), ( 240, 630), ( 320, 630), ( 400, 623), ( 480, 610),
                                                         ( 560, 590), ( 640, 570), ( 720, 545), ( 800, 515), ( 880, 480),
                                                         ( 960, 435), (1040, 395), (1120, 355), (1200, 340), (1280, 330),
                                                         (1360, 320), (1440, 315), (1520, 308), (1600, 306), (1680, 303),
                                                         (1760, 300), (1840, 297), (1920, 295), (2000, 295), (2080, 293),
                                                         (2160, 290), (2240, 289), (2320, 288), (2400, 287), (2480, 286),
                                                         (2560, 287), (2640, 290), (2720, 293), (2800, 298), (2880, 303),
                                                         (2960, 310),],
            ("UpperLimit",                  "down"   ): [( 160, 610), ( 240, 630), ( 320, 600), ( 400, 580),
                                                                      ( 640, 550), ( 720, 500), ( 800, 450), ( 880, 440),
                                                         ( 960, 340), (1040, 360), (1120, 360), (1200, 330), (1280, 310),
                                                         (1360, 300), (1440, 290), (1520, 300), (1600, 290), (1680, 290),
                                                         (1760, 280), (1840, 290),              (2000, 280), (2080, 260),
                                                         (2160, 260), (2240, 250), (2320, 290), (2400, 290), (2480, 280),
                                                                      (2640, 260), (2720, 270), (2800, 310), (2880, 290),
                                                         (2960, 300),],
            }
            }

def nEventsIn() :
    return {""         :(1,     None),
            "T5zz"     :(5.0e3, None),
            "tanBeta10":(9.0e3, 11.0e3),
            }

def overwriteInput() :
    return collections.defaultdict(list)

def overwriteOutput() :
    out = collections.defaultdict(list)
    out.update({"T2": [(9,2,1)],
                "T2bb": [
                (16, 9, 1), (18, 2, 1), (20, 3, 1), (20, 14, 1), (21, 1, 1),
                (22, 5, 1), (22, 15, 1), (23, 12, 1), (25, 17, 1), (26, 14, 1),
                (27, 13, 1), (28, 13, 1), (28, 19, 1), (29, 7, 1), (29, 9, 1),
                (29, 18, 1), (30, 4, 1), (31, 4, 1), (31, 6, 1), (31, 20, 1),
                (31, 23, 1), (33, 4, 1), (33, 5, 1), (33, 16, 1), (33, 20, 1),
                (33, 21, 1), (33, 22, 1), (33, 25, 1), (33, 26, 1), (35, 17, 1),
                (36, 13, 1), (36, 26, 1), (39, 9, 1), (39, 32, 1), (40, 5, 1),
                (40, 34, 1), (41, 11, 1), (41, 16, 1), (41, 20, 1), (41, 23, 1),
                (41, 27, 1), (42, 21, 1), (42, 29, 1), (42, 31, 1), (42, 33, 1),
                (43, 13, 1), (44, 6, 1), (44, 9, 1), (44, 17, 1), (44, 26, 1),
                (44, 31, 1), (44, 33, 1), (20, 12, 1), (31,2,1)
                ],
                "T1bbbb": [ (36, 29, 1) ],
                "T1tttt": [
                (37, 2, 1), (37, 3, 1), (37, 4, 1), (37, 5, 1), (37, 6, 1),
                (37, 7, 1), (29, 13, 1), (40, 24, 1), (44, 28, 1),
                (27, 11, 1)
                ],
                })
    return out

def graphBlackLists() :
    out = {}
    keys  = [ "UpperLimit", "ExpectedUpperLimit" ]
    keys += [ "ExpectedUpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    keys += [ "UpperLimit_%+d_Sigma" % i for i in [-1,1] ]
    for key in keys :
        out[key] = collections.defaultdict(list)

    out["UpperLimit"].update({"T1" : [ (1000,125), (1000,175) ]})
    out["UpperLimit_-1_Sigma"].update({"T1":[ (950, 350) ]})
    out["UpperLimit_+1_Sigma"].update({"T1":[ (1050,50), (1025, 375),
        (1025, 400), (1000,425) ]})

    out["UpperLimit"].update({"T2" : [ (800,200) ]})
    out["UpperLimit_-1_Sigma"].update({"T2":[ (750, 200), (675,300),
        (525,300) ]})
    out["UpperLimit_+1_Sigma"].update({"T2":[ (575,400), (725,325), (700,300),
        (750,250), (775,200), (825,275), (800,250), (850,225), (850,75),
        (875,75), (725,250)]})
    out["ExpectedUpperLimit_-1_Sigma"].update({"T2" : [ (875,150) ]})

    out["UpperLimit"].update({"T2bb" : [ (500,100), (500,250),
        (575,125), (500, 150), (525,200), (500,200) ]})

    out["UpperLimit_-1_Sigma"].update({"T2bb" : [ (525,150), (475, 200)]})
    out["UpperLimit_+1_Sigma"].update({"T2bb" : [ (575,125), (500, 250), (550, 200), (575, 200), (500,150), (525,200)]})

    out["ExpectedUpperLimit_-1_Sigma"].update({"T2bb" : [ (500,250),
        (525,225), (525,100), (525,200)]})
    out["ExpectedUpperLimit_+1_Sigma"].update({"T2bb" : [ (475, 75), ]})

    out["UpperLimit"].update({"T2tt" : [ (550,100), (525,150), (450,50), (475,100) ]})
    out["UpperLimit_-1_Sigma"].update({"T2tt":[ (550, 100) ]})
    out["UpperLimit_+1_Sigma"].update({"T2tt":[ (550, 100), (575,125),
        (525,150), (475,125) ]})
    out["ExpectedUpperLimit_-1_Sigma"].update({"T2tt" : [ (450,50), (375,50)]})

    out["UpperLimit"].update({"T1bbbb" : [ (1050,200), (1050,250),
        (1075,650), (1050,400), (1025,475), (975,650), (1050,450), (950,625),
        (975,550), (1000,525), (1025,525), (1050,475), (1000,575), (1000,625),
        (1025,625), (1050,600)]})
    out["UpperLimit_-1_Sigma"].update({"T1bbbb" : [ (950,600), (975,600),
        (1025,600), (1025,575), (875,550), (925,525), (950,500), (975,500),
        (900,575) ]})
    out["UpperLimit_+1_Sigma"].update({"T1bbbb" : [ (875,625), (1025,475),
        (1025,525), (1075,650), (1075,625), (1075,100), (1075,150), (1075,350),
        (1125,375), (1075,400), (1075,450), (1075,500) ]})

    out["ExpectedUpperLimit_-1_Sigma"].update({"T1bbbb" :
        [(1050,75), (1100,200), (975,625), (875, 625), (925,575), (900,575),
        (875,575), (850,575), (825,575), (1025,575), (1050,450) ]})
    out["ExpectedUpperLimit"].update({"T1bbbb" : [ (1025,475),
        (1025,450) ]})

    out["UpperLimit"].update({"T1tttt" : [ (550,150), (800,350),
        (750,300), (800,300), (800,250), (825,200), (825,250), (875,300) ]})
    out["UpperLimit_-1_Sigma"].update({"T1tttt" : [ (550,150), (600,100),
        (600,150), (725,200), (750,200), (875,175), (775,275), (825,250) ]})
    out["UpperLimit_+1_Sigma"].update({"T1tttt" : [ (550,150), (825,200),
        (825,250), (875,350), (900,350), (925,300), (900,300)]})

    out["ExpectedUpperLimit"].update({"T1tttt" : [(825,175)] })
    out["ExpectedUpperLimit_+1_Sigma"].update({"T1tttt" :
        [(675,175), (750, 125) ]})
    out["ExpectedUpperLimit_-1_Sigma"].update({"T1tttt" :
        [(875,350), (900,150), (900,200), (1000,225), (925,225), (950,275),
        (950,300), (900,325), (850,325)]})

    out["UpperLimit"].update({"T1tttt_2012" : [ (850,200) ]})
    out["UpperLimit_-1_Sigma"].update({"T1tttt_2012" : [ (450,50) ]})

    return out
