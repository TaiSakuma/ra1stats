from inputData import syst
from data import data,scaled

# TypeI PF MET

def common(x, systMode = 1240) :
    x._htBinLowerEdges = (275.0, 325.0, 375.0, 475.0, 575.0, 675.0, 775.0, 875.0)
    x._htMaxForPlot = 975.0
    x._htMeans = ( 297.96, 347.558, 415.942, 516.723, 617.19, 718.153, 818.612, 1044.56 )

    x._mergeBins = None
    x._constantMcRatioAfterHere = (    0,     0,     0,     0,     0,     0,     0,     1)
    x._lumi =  	{
		"mumu"               :   3.676e+03 ,
		"muon"               :   3.676e+03 ,
		"mcPhot"             :   3.889e+03 ,
		"phot"               :   3.889e+03 ,
		"mcHad"              :   3.871e+03 ,
		"had"                :   3.871e+03 ,
		"mcMuon"             :   3.676e+03 ,
		"mcMumu"             :   3.676e+03 ,
	}
    x._triggerEfficiencies = {
        "hadBulk":       (     1.000,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000),
        "had":           (     0.900,     0.990,     0.990,     0.990,     1.000,     1.000,     1.000,     1.000),
        "muon":          (     0.880,     0.880,     0.880,     0.880,     0.880,     0.880,     0.880,     0.880),
        "phot":          (     1.000,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000),
        "mumu":          (     0.950,     0.960,     0.960,     0.970,     0.970,     0.970,     0.980,     0.980),
        }
    x._purities = {
        "phot":          (     1.000,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000,     1.000),
        }
    x._mcExpectationsBeforeTrigger["mcGjets"] =  x._mcExpectationsBeforeTrigger["mcPhot"]
    x._mcExtraBeforeTrigger = {}
    x._observations["nHadBulk"] = (231496000, 103615000, 76347400, 25456300, 9467480, 3855680, 1729150, 1750550)
    syst.load(x, mode = systMode)

class data_0b(data) :
# with alphaT
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
                "mcPhot"             :   ( None, None, 1.212e+03, 460.3, 174.7, 68.14, 30.28, 24.91, ) ,
                "mcHad"              :   ( 3.241e+03, 1.206e+03, 902.9, 330.2, 123.5, 48.45, 20.3, 15.81, ) ,
                "mcTtw"              :   ( 1.766e+03, 551.1, 427.8, 155.3, 55.72, 21.06, 9.005, 7.308, ) ,
                "mcMuon"             :   ( 1.02e+03, 417.8, 307.4, 112.5, 44.82, 17.86, 7.27, 4.516, ) ,
                "mcZinv"             :   ( 1.475e+03, 654.8, 475.1, 174.9, 67.79, 27.39, 11.3, 8.505, ) ,
                "mcMumu"             :   ( 121.5, 55.12, 46.8, 19.51, 8.137, 2.094, 0.35, 0.1185, ) ,
            }

        self._mcStatError =  	{
                "mcMuonErr"          :   ( 72.54, 28.82, 4.96, 2.694, 1.662, 1.024, 0.6568, 0.4861, ) ,
                "mcMumuErr"          :   ( 7.912, 5.353, 4.936, 3.107, 2.016, 1.024, 0.0, 0.05745, ) ,
                "mcHadErr"           :   ( 142.6, 31.67, 30.37, 3.685, 2.164, 1.41, 0.8632, 0.766, ) ,
                "mcZinvErr"          :   ( 7.619, 4.906, 3.62, 1.971, 1.218, 0.7717, 0.4919, 0.4238, ) ,
                "mcTtwErr"           :   ( 142.4, 31.29, 30.15, 3.114, 1.788, 1.18, 0.7094, 0.6381, ) ,
                "mcPhotErr"          :   ( None, None, 19.61, 11.49, 7.044, 4.367, 2.898, 2.618, ) ,
            }

        self._observations =  	{
                "nPhot"              :   ( None, None, 1.052e+03, 360.0, 140.0, 49.0, 14.0, 12.0, ) ,
                "nHad"               :   ( 2.461e+03, 1.124e+03, 755.0, 290.0, 85.0, 41.0, 8.0, 22.0, ) ,
                "nMuon"              :   ( 694.0, 294.0, 247.0, 69.0, 25.0, 5.0, 5.0, 1.0, ) ,
                "nMumu"              :   ( 103.0, 52.0, 31.0, 15.0, 2.0, 2.0, 2.0, 0.0, ) ,
            }
        common(self)

class data_0b_no_aT(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
                "mcPhot"             :   ( None, None, 1.212e+03, 460.3, 174.7, 68.14, 30.28, 24.91, ) ,
                "mcHad"              :   ( 3.241e+03, 1.206e+03, 902.9, 330.2, 123.5, 48.45, 20.3, 15.81, ) ,
                "mcTtw"              :   ( 1.766e+03, 551.1, 427.8, 155.3, 55.72, 21.06, 9.005, 7.308, ) ,
                "mcMuon"             :   ( 5.103e+03, 2.463e+03, 2.267e+03, 1.078e+03, 482.6, 233.2, 115.0, 147.7, ) ,
                "mcZinv"             :   ( 1.475e+03, 654.8, 475.1, 174.9, 67.79, 27.39, 11.3, 8.505, ) ,
                "mcMumu"             :   ( 520.2, 285.0, 265.4, 113.2, 62.55, 34.34, 13.69, 12.49, ) ,
            }

        self._mcStatError =  	{
                "mcMuonErr"          :   ( 163.3, 65.06, 13.98, 28.99, 5.607, 3.921, 2.709, 5.389, ) ,
                "mcMumuErr"          :   ( 16.54, 12.22, 11.75, 7.511, 5.658, 4.191, 2.639, 2.442, ) ,
                "mcHadErr"           :   ( 142.6, 31.67, 30.37, 3.685, 2.164, 1.41, 0.8632, 0.766, ) ,
                "mcZinvErr"          :   ( 7.619, 4.906, 3.62, 1.971, 1.218, 0.7717, 0.4919, 0.4238, ) ,
                "mcTtwErr"           :   ( 142.4, 31.29, 30.15, 3.114, 1.788, 1.18, 0.7094, 0.6381, ) ,
                "mcPhotErr"          :   ( None, None, 19.61, 11.49, 7.044, 4.367, 2.898, 2.618, ) ,
            }

        self._observations =  	{
                "nPhot"              :   ( None, None, 1.052e+03, 360.0, 140.0, 49.0, 14.0, 12.0, ) ,
                "nHad"               :   ( 2.461e+03, 1.124e+03, 755.0, 290.0, 85.0, 41.0, 8.0, 22.0, ) ,
                "nMuon"              :   ( 3.582e+03, 1.878e+03, 1.784e+03, 731.0, 324.0, 130.0, 86.0, 97.0, ) ,
                "nMumu"              :   ( 465.0, 222.0, 195.0, 85.0, 59.0, 20.0, 11.0, 6.0, ) ,
            }
        common(self)

class data_1b(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
                "mcPhot"             :   ( None, None, 113.3, 44.98, 18.69, 8.22, 4.038, 3.295, ) ,
                "mcHad"              :   ( 660.4, 261.6, 206.4, 74.38, 30.76, 11.14, 5.087, 3.79, ) ,
                "mcTtw"              :   ( 518.8, 199.6, 158.5, 55.58, 23.15, 7.911, 3.606, 2.551, ) ,
                "mcMuon"             :   ( 1.504e+03, 824.8, 767.9, 410.1, 180.2, 83.22, 43.4, 60.51, ) ,
                "mcZinv"             :   ( 141.6, 61.99, 47.92, 18.8, 7.61, 3.226, 1.481, 1.239, ) ,
                "mcMumu"             :   ( 73.4, 45.87, 40.93, 22.99, 11.28, 5.598, 2.097, 2.887, ) ,
            }

        self._mcStatError =  	{
                "mcMuonErr"          :   ( 38.92, 20.6, 16.72, 10.76, 7.456, 5.151, 4.087, 11.55, ) ,
                "mcMumuErr"          :   ( 3.789, 3.118, 2.582, 1.616, 1.133, 1.011, 0.3862, 0.3364, ) ,
                "mcHadErr"           :   ( 60.58, 17.98, 6.952, 4.36, 2.957, 1.602, 1.192, 0.7677, ) ,
                "mcZinvErr"          :   ( 1.664, 1.002, 0.7681, 0.4337, 0.2803, 0.151, 0.09339, 0.1148, ) ,
                "mcTtwErr"           :   ( 60.56, 17.96, 6.91, 4.338, 2.944, 1.595, 1.188, 0.7591, ) ,
                "mcPhotErr"          :   ( None, None, 3.453, 2.037, 0.9642, 0.8281, 0.55, 0.3467, ) ,
            }

        self._observations =  	{
                "nPhot"              :   ( None, None, 143.0, 57.0, 15.0, 11.0, 4.0, 1.0, ) ,
                "nHad"               :   ( 556.0, 219.0, 178.0, 60.0, 19.0, 7.0, 2.0, 3.0, ) ,
                "nMuon"              :   ( 1.339e+03, 655.0, 601.0, 274.0, 128.0, 59.0, 29.0, 16.0, ) ,
                "nMumu"              :   ( 64.0, 34.0, 33.0, 20.0, 6.0, 2.0, 3.0, 1.0, ) ,
            }
        common(self)

class data_2b(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
                "mcPhot"             :   ( None, None, 9.043, 3.413, 2.15, 0.6642, 0.2998, 0.1748, ) ,
                "mcHad"              :   ( 150.2, 60.5, 52.87, 18.8, 9.281, 2.608, 1.524, 0.7981, ) ,
                "mcTtw"              :   ( 135.3, 54.55, 48.44, 16.93, 8.552, 2.306, 1.383, 0.695, ) ,
                "mcMuon"             :   ( 573.5, 339.8, 307.0, 170.9, 81.08, 32.85, 19.62, 18.22, ) ,
                "mcZinv"             :   ( 14.85, 5.944, 4.438, 1.87, 0.7284, 0.302, 0.1406, 0.1031, ) ,
                "mcMumu"             :   ( 18.13, 11.81, 8.624, 5.407, 2.484, 0.6533, 0.1875, 0.549, ) ,
            }

        self._mcStatError =  	{
                "mcMuonErr"          :   ( 19.9, 10.94, 7.933, 7.035, 2.925, 1.82, 1.397, 1.444, ) ,
                "mcMumuErr"          :   ( 1.878, 1.728, 1.503, 1.19, 0.762, 0.2355, 0.1368, 0.2882, ) ,
                "mcHadErr"           :   ( 7.321, 2.319, 4.632, 1.249, 1.001, 0.4372, 0.3432, 0.2351, ) ,
                "mcZinvErr"          :   ( 0.5969, 0.3685, 0.2652, 0.1551, 0.1004, 0.05995, 0.04133, 0.02742, ) ,
                "mcTtwErr"           :   ( 7.296, 2.289, 4.624, 1.239, 0.9956, 0.4331, 0.3407, 0.2335, ) ,
                "mcPhotErr"          :   ( None, None, 1.323, 0.743, 0.6585, 0.3259, 0.1368, 0.05159, ) ,
            }

        self._observations =  	{
                "nPhot"              :   ( None, None, 15.0, 6.0, 1.0, 1.0, 0.0, 1.0, ) ,
                "nHad"               :   ( 155.0, 67.0, 45.0, 27.0, 8.0, 1.0, 0.0, 2.0, ) ,
                "nMuon"              :   ( 568.0, 267.0, 276.0, 137.0, 53.0, 24.0, 12.0, 8.0, ) ,
                "nMumu"              :   ( 9.0, 9.0, 11.0, 4.0, 0.0, 1.0, 0.0, 2.0, ) ,
            }
        common(self)

class data_ge3b(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
                "mcPhot"             :   ( None,  None, 0.232, 0.09742, 0.06791, 0.02015, 0.004676, 0.0004666, ) ,
                "mcHad"              :   ( 8.726, 3.443, 3.626, 1.719, 1.167, 0.3545, 0.2667, 0.1249, ) ,
                "mcTtw"              :   ( 8.397, 3.309, 3.514, 1.666, 1.144, 0.3435, 0.2617, 0.1215, ) ,
                "mcMuon"             :   ( 25.65, 16.73, 17.81, 16.83, 8.317, 3.654, 2.817, 3.107, ) ,
                "mcZinv"             :   ( 0.3286, 0.1338, 0.1113, 0.05369, 0.02355, 0.01104, 0.005043, 0.00338, ) ,
                "mcMumu"             :   ( 0.567, 0.3986, 0.3588, 0.3062, 0.1956, 0.05237, 0.01772, 0.03229, ) ,
            }

        self._mcStatError =  	{
                "mcMuonErr"          :   ( 0.5692, 0.4087, 0.2478, 0.4355, 0.1995, 0.1253, 0.1223, 0.1108, ) ,
                "mcMumuErr"          :   ( 0.0561, 0.05526, 0.05517, 0.05287, 0.05164, 0.01272, 0.009897, 0.01565, ) ,
                "mcHadErr"           :   ( 0.3065, 0.1022, 0.1994, 0.07798, 0.08018, 0.03694, 0.03227, 0.02384, ) ,
                "mcZinvErr"          :   ( 0.01409, 0.008894, 0.007336, 0.004767, 0.003321, 0.00225, 0.001666, 0.001035, ) ,
                "mcTtwErr"           :   ( 0.3062, 0.1019, 0.1993, 0.07784, 0.08012, 0.03687, 0.03223, 0.02382, ) ,
                "mcPhotErr"          :   ( None,   None, 0.03721, 0.02333, 0.02141, 0.011, 0.003834, 0.0, ) ,
            }

        self._observations =  	{
                "nPhot"              :   ( None, None, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, ) ,
                "nHad"               :   ( 14.0, 1.0, 2.0, 2.0, 0.0, 1.0, 0.0, 0.0, ) ,
                "nMuon"              :   ( 35.0, 24.0, 26.0, 13.0, 7.0, 2.0, 1.0, 2.0, ) ,
                "nMumu"              :   ( 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
            }
        common(self)
