from data import data
import utils

def common1(x) :
    x._lumi =  	{
        "mumu"  : 1.139e+04,
        "muon"  : 1.139e+04,
        "mcPhot": 1.157e+04,
        "phot"  : 1.157e+04,
        "mcHad" : 1.166e+04,
        "had"   : 1.166e+04,
        "mcMuon": 1.139e+04,
        "mcMumu": 1.139e+04,
	}

    x._triggerEfficiencies = {
        "hadBulk":       (1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000),
        "muon":          (0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880, 0.880),
        "phot":          (1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000),
        "mumu":          (0.950, 0.960, 0.960, 0.970, 0.970, 0.970, 0.980, 0.980),
        }

    x._htBinLowerEdges = (275.0, 325.0, 375.0, 475.0, 575.0, 675.0, 775.0, 875.0)
    x._htMaxForPlot    = 975.0
    x._htMeans         = (298.0, 348.0, 416.0, 517.0, 617.0, 719.0, 819.0, 1044.)

    x._observations["nPhot"] = tuple([None, None]+list(x._observations["nPhot"][2:]))

def common(x) :
    common1(x)

    #systBins = tuple([0]*4+[1]*2+[2]*2)
    systBins = tuple([0,1]+[2]*2+[3]*2+[4]*2)
    name = x.__class__.__name__

    if "ge2j" in name :
        systMagnitudes = (0.10, 0.10, 0.20, 0.20, 0.30)
        #x._observations["nHadBulk"] = (630453600, 286166200, 209611400, 69777150, 26101500, 20182300, 4745175, 4776350)
        x._triggerEfficiencies["had"] = (0.870, 0.986, 0.994, 1.000, 1.000, 1.000, 1.000, 1.000)
    elif "le3j" in name :
        #systMagnitudes = (0.10, 0.20, 0.20)
        systMagnitudes = (0.10, 0.10, 0.20, 0.20, 0.20)
        x._triggerEfficiencies["had"] = (0.891, 0.987, 0.990, 1.000, 1.000, 1.000, 1.000, 1.000)
        x._observations["nHadBulk"] = (487992800, 202369400, 134976100, 36965375, 12292400,  8301900, 1925125, 1768325)
    elif "ge4j" in name :
        #systMagnitudes = (0.10, 0.20, 0.30)
        systMagnitudes = (0.10, 0.10, 0.20, 0.20, 0.30)
        x._triggerEfficiencies["had"] = (0.837, 0.982, 0.997, 1.000, 1.000, 1.000, 1.000, 1.000)
        x._observations["nHadBulk"] = (142460800,  83796800,  74635300, 32811775, 13809100, 11880400, 2820050, 3008025)

    if "ge4b" in name :
        x._mergeBins = (0, 1, 2, 2, 2, 2, 2, 2)
        systMagnitudes = (0.25,)
        systBins = (0, 0, 0)
    else :
        x._mergeBins = None

    x._systBins = {
        "sigmaPhotZ": systBins,
        "sigmaMuonW": systBins,
        "sigmaMumuZ": systBins,
        }

    x._fixedParameters = {
        "sigmaPhotZ": systMagnitudes,
        "sigmaMuonW": systMagnitudes,
        "sigmaMumuZ": systMagnitudes,
        "k_qcd_nom":2.96e-2,
        "k_qcd_unc_inp":utils.quadSum([0.61e-2, 0.463e-2])
        }

class data_0b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 295.8, 220.5, 117.1, 54.79, 27.14, 18.89, ) ,
		"mcHad"              :   ( 1906.0, 693.6, 528.6, 311.1, 138.6, 61.3, 26.94, 22.27, ) ,
		"mcTtw"              :   ( 1360.0, 480.8, 373.3, 205.7, 85.18, 37.34, 15.14, 13.7, ) ,
		"mcMuon"             :   ( 1795.0, 806.9, 893.2, 691.9, 373.5, 197.6, 104.8, 144.1, ) ,
		"mcZinv"             :   ( 546.0, 212.8, 155.3, 105.5, 53.38, 23.96, 11.8, 8.565, ) ,
		"mcMumu"             :   ( 131.7, 63.66, 63.79, 53.25, 32.88, 18.47, 10.4, 15.3, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 75.35, 12.38, 21.26, 9.722, 7.11, 5.2, 3.826, 4.712, ) ,
		"mcMumuErr"          :   ( 3.974, 2.957, 1.479, 1.095, 0.8693, 0.6727, 0.4905, 0.5866, ) ,
		"mcHadErr"           :   ( 68.46, 20.79, 8.399, 6.006, 4.009, 2.61, 1.664, 1.601, ) ,
		"mcZinvErr"          :   ( 7.92, 4.709, 3.554, 2.653, 1.887, 1.224, 0.8757, 0.7091, ) ,
		"mcTtwErr"           :   ( 68.0, 20.25, 7.61, 5.388, 3.538, 2.305, 1.415, 1.435, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 15.68, 13.72, 9.7, 6.78, 4.587, 3.509, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 308.0, 213.0, 99.0, 50.0, 24.0, 17.0, ) ,
		"nHad"               :   ( 1.236e+04, 3535.0, 1158.0, 355.0, 128.0, 66.0, 17.0, 27.0, ) ,
		"nMuon"              :   ( 1388.0, 645.0, 638.0, 446.0, 260.0, 147.0, 59.0, 88.0, ) ,
		"nMumu"              :   ( 126.0, 46.0, 55.0, 56.0, 32.0, 11.0, 7.0, 8.0, ) ,
	}

        common(self)


class data_0b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 2655.0, 914.9, 309.9, 125.3, 42.91, 34.15, ) ,
		"mcHad"              :   ( 8797.0, 3619.0, 2450.0, 713.0, 239.8, 81.28, 31.63, 23.23, ) ,
		"mcTtw"              :   ( 4995.0, 1934.0, 1299.0, 350.5, 107.5, 34.63, 13.81, 8.94, ) ,
		"mcMuon"             :   ( 1.222e+04, 6497.0, 6191.0, 2569.0, 1096.0, 512.4, 263.1, 330.5, ) ,
		"mcZinv"             :   ( 3802.0, 1686.0, 1152.0, 362.5, 132.3, 46.64, 17.82, 14.29, ) ,
		"mcMumu"             :   ( 1273.0, 715.1, 706.8, 311.2, 135.7, 66.46, 34.77, 44.1, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 143.6, 45.22, 35.99, 28.38, 14.26, 9.919, 7.029, 7.989, ) ,
		"mcMumuErr"          :   ( 10.28, 6.589, 5.028, 2.64, 1.728, 1.197, 0.8748, 0.9875, ) ,
		"mcHadErr"           :   ( 133.3, 36.33, 18.94, 9.504, 5.531, 3.178, 1.914, 1.562, ) ,
		"mcZinvErr"          :   ( 20.44, 13.25, 9.654, 5.017, 3.057, 1.78, 1.109, 0.9864, ) ,
		"mcTtwErr"           :   ( 131.7, 33.83, 16.29, 8.072, 4.609, 2.632, 1.56, 1.211, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 49.18, 27.28, 16.38, 10.57, 5.683, 5.249, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 2599.0, 851.0, 252.0, 93.0, 35.0, 21.0, ) ,
		"nHad"               :   ( 2.234e+04, 7211.0, 3182.0, 622.0, 193.0, 62.0, 19.0, 26.0, ) ,
		"nMuon"              :   ( 9728.0, 5051.0, 4669.0, 1811.0, 779.0, 297.0, 150.0, 194.0, ) ,
		"nMumu"              :   ( 1340.0, 711.0, 624.0, 205.0, 120.0, 44.0, 21.0, 26.0, ) ,
	}

        common(self)


class data_1b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 49.31, 33.35, 16.31, 10.85, 5.501, 3.333, ) ,
		"mcHad"              :   ( 1182.0, 475.5, 368.1, 181.2, 66.73, 26.29, 11.0, 9.345, ) ,
		"mcTtw"              :   ( 1096.0, 440.4, 340.9, 163.6, 59.22, 21.69, 8.417, 7.647, ) ,
		"mcMuon"             :   ( 1600.0, 830.7, 892.8, 652.1, 334.6, 163.9, 82.97, 95.36, ) ,
		"mcZinv"             :   ( 86.35, 35.16, 27.14, 17.64, 7.511, 4.608, 2.579, 1.698, ) ,
		"mcMumu"             :   ( 33.36, 15.79, 18.15, 15.37, 9.099, 5.074, 2.347, 3.702, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 13.38, 7.418, 8.008, 6.484, 4.589, 3.226, 2.268, 2.347, ) ,
		"mcMumuErr"          :   ( 1.183, 0.7751, 0.7845, 0.6868, 0.5162, 0.4199, 0.2289, 0.3321, ) ,
		"mcHadErr"           :   ( 11.9, 6.039, 4.905, 3.271, 1.929, 1.117, 0.7169, 0.716, ) ,
		"mcZinvErr"          :   ( 1.504, 0.9078, 0.7161, 0.5146, 0.3137, 0.2537, 0.1943, 0.1504, ) ,
		"mcTtwErr"           :   ( 11.8, 5.971, 4.853, 3.231, 1.904, 1.088, 0.6901, 0.7001, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 2.944, 2.248, 1.47, 1.419, 0.9396, 0.6125, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 57.0, 45.0, 16.0, 12.0, 10.0, 3.0, ) ,
		"nHad"               :   ( 2744.0, 959.0, 501.0, 157.0, 65.0, 19.0, 15.0, 7.0, ) ,
		"nMuon"              :   ( 1375.0, 613.0, 594.0, 444.0, 204.0, 109.0, 55.0, 48.0, ) ,
		"nMumu"              :   ( 31.0, 14.0, 21.0, 15.0, 11.0, 3.0, 2.0, 4.0, ) ,
	}

        common(self)


class data_1b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 265.6, 86.33, 25.9, 14.57, 6.166, 4.106, ) ,
		"mcHad"              :   ( 1715.0, 743.3, 493.4, 114.6, 30.2, 11.9, 4.519, 2.769, ) ,
		"mcTtw"              :   ( 1330.0, 564.6, 369.1, 77.16, 18.47, 6.38, 2.177, 1.181, ) ,
		"mcMuon"             :   ( 2943.0, 1696.0, 1536.0, 558.4, 211.1, 89.59, 41.77, 46.45, ) ,
		"mcZinv"             :   ( 384.7, 178.6, 124.3, 37.42, 11.73, 5.522, 2.342, 1.588, ) ,
		"mcMumu"             :   ( 174.9, 102.0, 96.22, 40.92, 16.37, 7.773, 3.616, 4.61, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 17.41, 11.03, 10.15, 6.129, 3.504, 2.178, 1.499, 1.491, ) ,
		"mcMumuErr"          :   ( 2.446, 1.834, 1.569, 0.8624, 0.5042, 0.3105, 0.2242, 0.2503, ) ,
		"mcHadErr"           :   ( 14.54, 7.023, 5.254, 2.278, 1.09, 0.6572, 0.348, 0.2198, ) ,
		"mcZinvErr"          :   ( 3.042, 2.034, 1.459, 0.7029, 0.3874, 0.251, 0.195, 0.1184, ) ,
		"mcTtwErr"           :   ( 14.22, 6.722, 5.047, 2.167, 1.019, 0.6074, 0.2882, 0.1852, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 6.681, 3.368, 1.817, 1.527, 0.9717, 0.737, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 307.0, 101.0, 27.0, 9.0, 5.0, 3.0, ) ,
		"nHad"               :   ( 4003.0, 1315.0, 605.0, 114.0, 27.0, 9.0, 4.0, 1.0, ) ,
		"nMuon"              :   ( 2664.0, 1441.0, 1227.0, 413.0, 155.0, 51.0, 27.0, 26.0, ) ,
		"nMumu"              :   ( 184.0, 99.0, 102.0, 43.0, 18.0, 6.0, 2.0, 5.0, ) ,
	}

        common(self)


class data_2b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 6.837, 3.41, 2.371, 1.112, 0.4486, 0.2378, ) ,
		"mcHad"              :   ( 515.2, 211.0, 161.6, 82.63, 30.49, 9.813, 3.524, 3.5, ) ,
		"mcTtw"              :   ( 502.2, 206.0, 157.7, 80.29, 29.7, 9.245, 3.259, 3.335, ) ,
		"mcMuon"             :   ( 1033.0, 536.8, 561.6, 396.4, 203.1, 94.31, 46.11, 50.56, ) ,
		"mcZinv"             :   ( 12.99, 5.016, 3.922, 2.332, 0.7925, 0.5678, 0.2644, 0.1646, ) ,
		"mcMumu"             :   ( 13.27, 5.132, 7.242, 5.412, 2.893, 1.609, 0.4087, 0.8141, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 7.173, 5.188, 5.35, 4.433, 3.093, 2.102, 1.385, 1.393, ) ,
		"mcMumuErr"          :   ( 0.8512, 0.4472, 0.5623, 0.4564, 0.3051, 0.2682, 0.0874, 0.1424, ) ,
		"mcHadErr"           :   ( 4.682, 3.094, 2.684, 1.892, 1.127, 0.588, 0.3535, 0.3369, ) ,
		"mcZinvErr"          :   ( 0.6434, 0.3706, 0.2822, 0.1886, 0.1069, 0.08629, 0.03151, 0.02475, ) ,
		"mcTtwErr"           :   ( 4.637, 3.071, 2.669, 1.883, 1.122, 0.5817, 0.3521, 0.336, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 1.275, 0.8011, 0.6469, 0.3224, 0.07996, 0.04545, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 14.0, 13.0, 5.0, 1.0, 2.0, 2.0, ) ,
		"nHad"               :   ( 616.0, 276.0, 161.0, 73.0, 30.0, 6.0, 1.0, 2.0, ) ,
		"nMuon"              :   ( 825.0, 417.0, 388.0, 272.0, 147.0, 66.0, 25.0, 17.0, ) ,
		"nMumu"              :   ( 9.0, 7.0, 4.0, 7.0, 3.0, 1.0, 0.0, 2.0, ) ,
	}

        common(self)


class data_2b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 18.92, 3.965, 1.45, 0.803, 0.448, 0.1645, ) ,
		"mcHad"              :   ( 339.8, 153.2, 99.27, 20.94, 4.765, 1.429, 0.394, 0.1819, ) ,
		"mcTtw"              :   ( 305.7, 137.2, 89.69, 18.12, 4.026, 1.063, 0.2725, 0.1036, ) ,
		"mcMuon"             :   ( 987.3, 568.1, 503.8, 161.7, 56.95, 21.58, 8.336, 7.623, ) ,
		"mcZinv"             :   ( 34.08, 16.05, 9.576, 2.824, 0.7386, 0.3661, 0.1215, 0.07824, ) ,
		"mcMumu"             :   ( 40.8, 18.44, 16.23, 5.662, 2.186, 0.6733, 0.2947, 0.3306, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 7.434, 5.687, 5.397, 3.036, 1.766, 1.041, 0.6275, 0.5518, ) ,
		"mcMumuErr"          :   ( 1.467, 0.8982, 0.8014, 0.44, 0.2601, 0.08812, 0.08256, 0.08428, ) ,
		"mcHadErr"           :   ( 3.914, 2.661, 2.183, 0.9825, 0.4749, 0.2638, 0.1193, 0.05513, ) ,
		"mcZinvErr"          :   ( 1.071, 0.7059, 0.4469, 0.2167, 0.1094, 0.06524, 0.02287, 0.01904, ) ,
		"mcTtwErr"           :   ( 3.765, 2.566, 2.137, 0.9583, 0.4622, 0.2556, 0.117, 0.05174, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 2.39, 0.7291, 0.579, 0.3246, 0.1906, 0.04243, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 33.0, 7.0, 1.0, 2.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 619.0, 241.0, 111.0, 21.0, 7.0, 1.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 878.0, 451.0, 403.0, 120.0, 32.0, 7.0, 3.0, 4.0, ) ,
		"nMumu"              :   ( 45.0, 26.0, 15.0, 3.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_3b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.343, 0.172, 0.1054, 0.05307, 0.01883, 0.008872, ) ,
		"mcHad"              :   ( 53.62, 22.04, 17.09, 10.26, 4.218, 1.302, 0.4624, 0.5682, ) ,
		"mcTtw"              :   ( 52.95, 21.8, 16.87, 10.14, 4.184, 1.259, 0.449, 0.5595, ) ,
		"mcMuon"             :   ( 120.2, 61.9, 64.91, 49.46, 28.39, 13.59, 6.745, 8.271, ) ,
		"mcZinv"             :   ( 0.6719, 0.245, 0.2285, 0.1208, 0.03413, 0.04236, 0.01347, 0.008759, ) ,
		"mcMumu"             :   ( 0.9859, 0.3267, 0.4421, 0.3625, 0.1896, 0.1114, 0.02424, 0.0529, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.9693, 0.7089, 0.7408, 0.6626, 0.5376, 0.3621, 0.2448, 0.2794, ) ,
		"mcMumuErr"          :   ( 0.206, 0.03953, 0.03841, 0.035, 0.0239, 0.02274, 0.006787, 0.01173, ) ,
		"mcHadErr"           :   ( 0.588, 0.3948, 0.3459, 0.2919, 0.1922, 0.09802, 0.06072, 0.07124, ) ,
		"mcZinvErr"          :   ( 0.05486, 0.02379, 0.03394, 0.01373, 0.006687, 0.012, 0.00256, 0.002321, ) ,
		"mcTtwErr"           :   ( 0.5854, 0.3941, 0.3442, 0.2916, 0.192, 0.09728, 0.06067, 0.07121, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.08627, 0.0657, 0.03594, 0.02419, 0.003743, 0.002012, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 59.0, 28.0, 9.0, 6.0, 5.0, 4.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 84.0, 48.0, 49.0, 32.0, 18.0, 11.0, 6.0, 2.0, ) ,
		"nMumu"              :   ( 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_3b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.3331, 0.06088, 0.02547, 0.00464, 0.01154, 0.002196, ) ,
		"mcHad"              :   ( 15.52, 7.002, 4.521, 0.9465, 0.2005, 0.0557, 0.01267, 0.001995, ) ,
		"mcTtw"              :   ( 14.61, 6.687, 4.311, 0.8989, 0.19, 0.04785, 0.01093, 0.001127, ) ,
		"mcMuon"             :   ( 49.38, 28.01, 24.44, 7.546, 2.649, 1.018, 0.3322, 0.3155, ) ,
		"mcZinv"             :   ( 0.9114, 0.315, 0.2103, 0.04765, 0.01045, 0.007853, 0.001744, 0.0008677, ) ,
		"mcMumu"             :   ( 1.033, 0.3779, 0.4602, 0.139, 0.05165, 0.01415, 0.006248, 0.006573, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.4693, 0.3558, 0.3451, 0.2035, 0.0996, 0.07658, 0.03236, 0.0303, ) ,
		"mcMumuErr"          :   ( 0.104, 0.02463, 0.06408, 0.01533, 0.007963, 0.002781, 0.002556, 0.002581, ) ,
		"mcHadErr"           :   ( 0.2471, 0.1566, 0.1275, 0.05916, 0.02666, 0.01521, 0.006819, 0.0005161, ) ,
		"mcZinvErr"          :   ( 0.104, 0.03508, 0.02554, 0.005934, 0.00245, 0.002373, 0.0006704, 0.000276, ) ,
		"mcTtwErr"           :   ( 0.2241, 0.1526, 0.1249, 0.05886, 0.02654, 0.01502, 0.006786, 0.0004362, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.07253, 0.02179, 0.01601, 0.0005229, 0.008196, 0.0007704, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 18.0, 9.0, 8.0, 0.0, 1.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 48.0, 29.0, 20.0, 9.0, 3.0, 0.0, 1.0, 0.0, ) ,
		"nMumu"              :   ( 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_ge4b_ge4j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.005339, 0.003724, 0.001403, 0.0009959, 0.0004395, 0.0001909, ) ,
		"mcHad"              :   ( 1.708, 0.6888, 0.5832, 0.4796, 0.2413, 0.07831, 0.02834, 0.04678, ) ,
		"mcTtw"              :   ( 1.697, 0.685, 0.567, 0.4773, 0.2408, 0.07709, 0.02803, 0.04652, ) ,
		"mcMuon"             :   ( 4.138, 2.089, 2.296, 2.224, 1.555, 0.8153, 0.4252, 0.6235, ) ,
		"mcZinv"             :   ( 0.01058, 0.003742, 0.0162, 0.002318, 0.0005451, 0.001215, 0.0003103, 0.0002559, ) ,
		"mcMumu"             :   ( 0.0188, 0.005824, 0.007753, 0.007623, 0.004232, 0.002816, 0.0005713, 0.001375, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.03959, 0.03089, 0.03277, 0.04035, 0.04068, 0.02694, 0.01928, 0.0278, ) ,
		"mcMumuErr"          :   ( 0.005969, 0.001012, 0.0007531, 0.0008565, 0.0006649, 0.0007891, 0.0001885, 0.000383, ) ,
		"mcHadErr"           :   ( 0.0224, 0.01493, 0.01941, 0.01817, 0.01359, 0.007597, 0.004612, 0.007631, ) ,
		"mcZinvErr"          :   ( 0.001327, 0.0004054, 0.01289, 0.0003464, 0.0001389, 0.0004446, 6.955e-05, 0.0001049, ) ,
		"mcTtwErr"           :   ( 0.02237, 0.01493, 0.01452, 0.01816, 0.01359, 0.007584, 0.004611, 0.007631, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.001474, 0.00188, 0.0005025, 0.0004849, 0.0001102, 6.225e-05, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 4.0, 0.0, 2.0, 1.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 1.0, 1.0, 0.0, 1.0, 2.0, 0.0, 0.0, 0.0, ) ,
		"nMumu"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)


class data_ge4b_le3j(data) :
    def _fill(self) :
        self._mcExpectationsBeforeTrigger =  	{
		"mcPhot"             :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcHad"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcTtw"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcMuon"             :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcZinv"             :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcMumu"             :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        self._mcStatError =  	{
		"mcMuonErr"          :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcMumuErr"          :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcHadErr"           :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcZinvErr"          :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcTtwErr"           :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"mcPhotErr"          :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        self._observations =  	{
		"nPhot"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nHad"               :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMuon"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
		"nMumu"              :   ( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ) ,
	}

        common(self)
