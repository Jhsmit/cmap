__license__ = "MIT"
__source__ = "https://github.com/matplotlib/cmocean"


# Used to reconstruct the colormap in pycam02ucs.cm.viscm
# parameters = {'xp': [19.702560107644928, 44.755497326581946, 19.328635671541406, -17.315959066605274, -9.0896214723274511],
#               'yp': [10.453858877923182, 16.062725419476237, 25.410836322064682, 38.124267149584966, 28.402231810892971],
#               'min_Jp': 15.1269035533,
#               'max_Jp': 97.1573604061}

oxy = [
    [0.25032177, 0.02046237, 0.01966892],
    [0.25556485, 0.02111591, 0.02090008],
    [0.26080155, 0.02176437, 0.02215967],
    [0.26604463, 0.02238304, 0.02344016],
    [0.27128867, 0.02298149, 0.02474302],
    [0.27653264, 0.02356134, 0.02606762],
    [0.28178616, 0.02410204, 0.02740685],
    [0.2870368, 0.02462864, 0.02876669],
    [0.29229647, 0.02511521, 0.03013811],
    [0.29755977, 0.02557236, 0.03152275],
    [0.30282213, 0.02600981, 0.03292221],
    [0.30809895, 0.02639179, 0.03432345],
    [0.31337668, 0.02674829, 0.03573423],
    [0.31865532, 0.02707913, 0.03715281],
    [0.32394949, 0.02734825, 0.03856493],
    [0.32924566, 0.0275874, 0.03997916],
    [0.33454443, 0.02779483, 0.04137064],
    [0.33985476, 0.02794706, 0.04271748],
    [0.34517249, 0.02805369, 0.04402858],
    [0.35049427, 0.02812284, 0.04530589],
    [0.35582068, 0.02815263, 0.04654771],
    [0.36115912, 0.02812226, 0.04774545],
    [0.36650539, 0.02804229, 0.04890135],
    [0.37185718, 0.02791864, 0.05001584],
    [0.37721491, 0.02774988, 0.05108646],
    [0.38257895, 0.02753472, 0.05211053],
    [0.38794955, 0.02727216, 0.0530851],
    [0.39332999, 0.02695212, 0.05400333],
    [0.39871727, 0.02658339, 0.05486495],
    [0.4041101, 0.02617015, 0.05566751],
    [0.40950809, 0.02571398, 0.05640694],
    [0.41491066, 0.02521742, 0.05707881],
    [0.42031692, 0.02468426, 0.05767829],
    [0.42572564, 0.02411983, 0.05820017],
    [0.43113554, 0.02353014, 0.05863828],
    [0.43654919, 0.02290868, 0.05897909],
    [0.44195989, 0.02228071, 0.05922146],
    [0.44736413, 0.02166211, 0.05935828],
    [0.45275755, 0.02107282, 0.05938213],
    [0.45814185, 0.02051271, 0.05927134],
    [0.46350709, 0.02002405, 0.05902266],
    [0.46884497, 0.01964556, 0.05862776],
    [0.47415166, 0.01940234, 0.05806381],
    [0.47941183, 0.01936335, 0.05733102],
    [0.48461318, 0.01958983, 0.05642063],
    [0.48974345, 0.02014613, 0.05532002],
    [0.49478242, 0.02112808, 0.05404462],
    [0.49971373, 0.0226195, 0.05260679],
    [0.50452218, 0.02470022, 0.05103037],
    [0.50919629, 0.02743498, 0.04934859],
    [0.51373016, 0.03086488, 0.04759931],
    [0.51812392, 0.03500463, 0.04582043],
    [0.52238301, 0.03984501, 0.04404711],
    [0.52651678, 0.04511655, 0.04230179],
    [0.53053614, 0.05056764, 0.0405991],
    [0.53445216, 0.0561323, 0.03893708],
    [0.53827673, 0.0617482, 0.03738225],
    [0.54201853, 0.06738178, 0.03591446],
    [0.54568722, 0.07300021, 0.03454024],
    [0.54928963, 0.0785877, 0.03324672],
    [0.55283335, 0.08412806, 0.03203531],
    [0.55632188, 0.08962115, 0.03088638],
    [0.55976329, 0.09505189, 0.02981373],
    [0.56315905, 0.10042718, 0.02879664],
    [0.56651252, 0.10574699, 0.02783021],
    [0.56982815, 0.11100806, 0.02691693],
    [0.57310894, 0.11621126, 0.02605384],
    [0.57635575, 0.12136236, 0.02523129],
    [0.57957073, 0.12646316, 0.02444688],
    [0.58275576, 0.1315157, 0.02369841],
    [0.5859125, 0.13652212, 0.02298378],
    [0.58904242, 0.14148465, 0.0223011],
    [0.592147, 0.14640517, 0.02164915],
    [0.5952277, 0.15128527, 0.02102731],
    [0.59828484, 0.15612864, 0.02043163],
    [0.60131931, 0.16093734, 0.01986079],
    [0.60433195, 0.16571333, 0.01931361],
    [0.60732351, 0.17045851, 0.01878899],
    [0.61029466, 0.17517467, 0.01828593],
    [0.61324599, 0.17986355, 0.01780353],
    [0.61617893, 0.18452532, 0.01734338],
    [0.61909328, 0.18916277, 0.01690272],
    [0.6219895, 0.19377738, 0.01648082],
    [0.62486798, 0.1983706, 0.01607703],
    [0.62772912, 0.20294375, 0.01569076],
    [0.63057325, 0.20749811, 0.0153215],
    [0.63340069, 0.21203487, 0.01496877],
    [0.63621174, 0.21655515, 0.01463216],
    [0.63900669, 0.22106003, 0.01431132],
    [0.64178639, 0.22554964, 0.01400751],
    [0.64455206, 0.23002362, 0.01372295],
    [0.6473024, 0.23448507, 0.01345343],
    [0.65003764, 0.23893485, 0.01319875],
    [0.65275796, 0.24337375, 0.01295875],
    [0.65546356, 0.24780256, 0.01273331],
    [0.65815552, 0.25222081, 0.01252464],
    [0.6608348, 0.25662825, 0.01233463],
    [0.66349987, 0.26102774, 0.01215897],
    [0.66615089, 0.2654199, 0.01199767],
    [0.66878801, 0.2698053, 0.01185078],
    [0.67141252, 0.27418313, 0.01172117],
    [0.67402504, 0.27855337, 0.01161017],
    [0.67662404, 0.28291857, 0.01151371],
    [0.67920965, 0.28727919, 0.01143195],
    [0.681782, 0.29163567, 0.01136508],
    [0.68434402, 0.2959853, 0.01132014],
    [0.686893, 0.30033171, 0.01129044],
    [0.68942903, 0.30467536, 0.01127608],
    [0.69195221, 0.3090166, 0.01127734],
    [0.69446517, 0.31335309, 0.01130065],
    [0.69696575, 0.31768766, 0.01134076],
    [0.69945374, 0.32202097, 0.01139719],
    [0.70192928, 0.3263533, 0.01147037],
    [0.70439517, 0.33068214, 0.0115673],
    [0.70684868, 0.33501077, 0.01168139],
    [0.70928991, 0.33933943, 0.01181309],
    [0.71171981, 0.34366752, 0.01196487],
    [0.71413942, 0.34799439, 0.0121395],
    [0.71654695, 0.35232217, 0.01233279],
    [0.71894251, 0.35665105, 0.01254529],
    [0.72132803, 0.36097949, 0.01278202],
    [0.72370232, 0.36530896, 0.01304031],
    [0.72606481, 0.36964029, 0.01331909],
    [0.72841623, 0.37397307, 0.01362047],
    [0.73075769, 0.37830656, 0.01394753],
    [0.7330875, 0.3826426, 0.01429651],
    [0.73540578, 0.3869813, 0.0146681],
    [0.73771444, 0.39132123, 0.01506735],
    [0.74001188, 0.39566404, 0.0154908],
    [0.74229795, 0.40001012, 0.0159385],
    [0.74457375, 0.40435871, 0.01641363],
    [0.7468391, 0.40871021, 0.01691622],
    [0.74909321, 0.41306552, 0.01744482],
    [0.75133661, 0.41742436, 0.01800127],
    [0.75357007, 0.42178631, 0.01858798],
    [0.75579243, 0.42615255, 0.01920263],
    [0.75800383, 0.43052314, 0.01984613],
    [0.76020558, 0.43489718, 0.02052233],
    [0.76239635, 0.43927596, 0.02122851],
    [0.76457628, 0.44365952, 0.02196563],
    [0.76674624, 0.44804735, 0.02273648],
    [0.76890556, 0.45244015, 0.02354003],
    [0.77105415, 0.45683815, 0.02437675],
    [0.77319254, 0.46124109, 0.02524862],
    [0.77532049, 0.46564932, 0.02615572],
    [0.77743783, 0.47006311, 0.02709835],
    [0.77954483, 0.47448241, 0.02807794],
    [0.78164146, 0.4789074, 0.0290951],
    [0.78372758, 0.4833383, 0.03015029],
    [0.78580334, 0.48777515, 0.03124464],
    [0.78786865, 0.49221815, 0.03237872],
    [0.78992356, 0.4966674, 0.03355346],
    [0.79196818, 0.50112295, 0.03476996],
    [0.79400213, 0.50558518, 0.03602816],
    [0.79602577, 0.51005397, 0.03732978],
    [0.79803924, 0.51452935, 0.03867607],
    [0.80004182, 0.51901194, 0.04006614],
    [0.80203408, 0.52350144, 0.04147691],
    [0.80401624, 0.52799783, 0.04289943],
    [0.80598747, 0.53250179, 0.04433686],
    [0.8079482, 0.53701313, 0.04579001],
    [0.80989886, 0.54153165, 0.0472597],
    [0.81183872, 0.54605798, 0.04874406],
    [0.81376767, 0.55059227, 0.05024275],
    [0.81568657, 0.55513405, 0.05175753],
    [0.81759499, 0.55968372, 0.05328731],
    [0.81949185, 0.56424207, 0.05482979],
    [0.82137865, 0.56880822, 0.05638803],
    [0.82325551, 0.57338218, 0.05796215],
    [0.8251199, 0.57796567, 0.05954713],
    [0.82697416, 0.58255729, 0.0611476],
    [0.82881842, 0.58715704, 0.06276375],
    [0.83065077, 0.59176621, 0.06439206],
    [0.83247193, 0.59638442, 0.06603397],
    [0.83428298, 0.60101108, 0.06769149],
    [0.83608314, 0.60564678, 0.06936327],
    [0.83787054, 0.61029272, 0.07104627],
    [0.83964766, 0.61494746, 0.07274493],
    [0.84141458, 0.61961104, 0.07445946],
    [0.84316828, 0.62428535, 0.07618511],
    [0.8449106, 0.62896934, 0.07792519],
    [0.84664248, 0.63366253, 0.07968136],
    [0.84836317, 0.63836545, 0.08145269],
    [0.85006967, 0.64307988, 0.08323499],
    [0.8517654, 0.64780392, 0.08503379],
    [0.85345037, 0.65253762, 0.08684936],
    [0.85512241, 0.65728228, 0.08867898],
    [0.85678071, 0.66203842, 0.09052203],
    [0.85842781, 0.66680464, 0.09238251],
    [0.86006366, 0.67158104, 0.09426077],
    [0.86168545, 0.67636924, 0.0961536],
    [0.86329311, 0.6811693, 0.09806161],
    [0.86488895, 0.68598001, 0.09998839],
    [0.86647286, 0.69080147, 0.10193437],
    [0.86804282, 0.69563482, 0.10389775],
    [0.86959676, 0.7004812, 0.10587693],
    [0.87113804, 0.70533885, 0.10787672],
    [0.87266647, 0.71020788, 0.10989772],
    [0.87418187, 0.71508846, 0.11194054],
    [0.87567959, 0.71998302, 0.11400111],
    [0.87716225, 0.72489021, 0.11608345],
    [0.87863089, 0.72980951, 0.11818975],
    [0.88008521, 0.73474108, 0.12032085],
    [0.88152491, 0.73968512, 0.12247764],
    [0.88294684, 0.74464321, 0.12465844],
    [0.88435056, 0.74961555, 0.1268644],
    [0.88573838, 0.75460097, 0.12909932],
    [0.88710988, 0.75959969, 0.13136443],
    [0.88846459, 0.76461192, 0.13366106],
    [0.88980202, 0.76963789, 0.13599066],
    [0.89112162, 0.77467784, 0.1383548],
    [0.89242043, 0.77973314, 0.14075338],
    [0.89369837, 0.78480379, 0.14318884],
    [0.89495679, 0.78988908, 0.14566486],
    [0.89619502, 0.79498925, 0.14818373],
    [0.89741236, 0.80010458, 0.15074796],
    [0.89860807, 0.80523531, 0.15336033],
    [0.89978135, 0.81038173, 0.15602391],
    [0.90093137, 0.8155441, 0.15874211],
    [0.90205726, 0.82072269, 0.16151872],
    [0.90315814, 0.82591775, 0.16435797],
    [0.90423307, 0.83112953, 0.16726459],
    [0.90528113, 0.83635827, 0.17024392],
    [0.90630138, 0.84160414, 0.17330195],
    [0.90729292, 0.84686732, 0.17644545],
    [0.9082549, 0.8521479, 0.17968212],
    [0.90918541, 0.85744638, 0.18302038],
    [0.9100752, 0.86276633, 0.18646838],
    [0.9109312, 0.86810433, 0.19004033],
    [0.91175302, 0.87346008, 0.1937498],
    [0.91254071, 0.87883301, 0.19761251],
    [0.91327552, 0.88423014, 0.20164647],
    [0.91397111, 0.88964499, 0.20587612],
    [0.91462416, 0.89507797, 0.21032894],
    [0.91521971, 0.9005338, 0.2150418],
    [0.91576919, 0.90600639, 0.22005714],
    [0.9162675, 0.91149583, 0.22543188],
    [0.91670208, 0.91700434, 0.23124674],
    [0.91708955, 0.92252213, 0.23759656],
    [0.9174401, 0.92804079, 0.24461551],
    [0.91778416, 0.93354269, 0.25248],
    [0.91818209, 0.93899707, 0.26142023],
    [0.91880144, 0.94433427, 0.27160124],
    [0.91988874, 0.94946138, 0.28299331],
    [0.92170201, 0.95429517, 0.29515795],
    [0.92432629, 0.95882577, 0.30744836],
    [0.92765151, 0.96310918, 0.31947504],
    [0.9315219, 0.9672116, 0.33105536],
    [0.93580128, 0.97118464, 0.34221253],
    [0.94039225, 0.97506515, 0.35296587],
    [0.94522476, 0.97887874, 0.3633572],
    [0.95025594, 0.9826387, 0.37347976],
    [0.95544153, 0.98636342, 0.38330209],
    [0.96076275, 0.99005723, 0.39290859],
    [0.96620066, 0.99372665, 0.40232518],
    [0.97173864, 0.99737776, 0.41156586],
]