import random
import csv

#read the oprs for each team, maybe use dictionary.

teams = {
    0 : {
        "number" : 612,
        "OPR" : 20.23
    },
    1 : {
        "number" : 614,
        "OPR" : 41.14
    },
    2 : {
        "number" : 686,
        "OPR" : 22.55
    },
    3 : {
        "number" : 888,
        "OPR" : 35.91
    },
    4 : {
        "number" : 1111,
        "OPR" : 33.85
    },
    #5 : {
    #    "number" : 1446,
    #    "OPR" : (32.59+11.94+30.86+15.17)/4
    #},
    #6 : {
    #    "number" : 1629,
    #    "OPR" : (4.87+18.86)/2
    #},
    5 : {
        "number" : 1719,
        "OPR" : 29.29
    },
    6 : {
        "number" : 1727,
        "OPR" : 43.11
    },
    7 : {
        "number" : 2199,
        "OPR" : 38.23
    },
    #10 : {
    #    "number" : 2377,
    #    "OPR" : (10.61+15+16.78)/3
    #},
    8 : {
        "number" : 2534,
        "OPR" : 31.30
    },
    9 : {
        "number" : 2914,
        "OPR" : 15.10
    },
    10 : {
        "number" : 3373,
        "OPR" : 24.25
    },
    #14 : {
    #    "number" : 3389,
    #    "OPR" : (26.38+21.88+22.32)/3
    #},
    #15 : {
    #    "number" : 3714,
    #    "OPR" : (13.39+23.92+27.75)/3
    #},
    #16 : {
    #    "number" : 3748,
    #    "OPR" : (18.97+19.4)/2
    #},
    11 : {
        "number" : 3793,
        "OPR" : 23.55
    },
    #18 : {
    #    "number" : 3941,
    #    "OPR" : (6.93+4.73)/2
    #,
    12 : {
        "number" : 4099,
        "OPR" : 41.80
    },
    13 : {
        "number" : 4456,
        "OPR" : 38.28
    },
    #21 : {
    #    "number" : 4464,
    #    "OPR" : (7.06+9.28)/2
    #},
    14 : {
        "number" : 4505,
        "OPR" : 19.27
    },
    15 : {
        "number" : 4514,
        "OPR" : 27.37
    },
    16 : { #FIRST North Carolina District Event: UNC Pembroke
        "number" : 4541,
        "OPR" : 67.28
    },
    #25 : {
    #    "number" : 4638,
    #    "OPR" : (17.91+18.43)/2
    #},
    17 : {
        "number" : 4821,
        "OPR" : 0.91
    },
    #27 : {
    #    "number" : 4949,
    #    "OPR" : (14.78+14.57)/2
    #},
    #28 : {
    #    "number" : 5587,
    #    "OPR" : (7.69+16.96)/2
    #},
    #29 : {
    #    "number" : 5830,
    #    "OPR" : (16.81+19.71+16.02)/3
    #},
    18 : {
        "number" : 5841,
        "OPR" : 9.71
    },
    #31 : {
    #    "number" : 6239,
    #    "OPR" : (13.96+15.07+18.52)/3
    #},
    #32 : {
    #    "number" : 6326,
    #    "OPR" : (10+17.87+16.54+22.16)/4
    #},
    19 : {
        "number" : 6863,
        "OPR" : 6.87
    },
    20 : {
        "number" : 6893,
        "OPR" : 20.58
    },
    21 : {
        "number" : 7770,
        "OPR" : 23.59
    },
    22 : {
        "number" : 7886,
        "OPR" : 23.11
    },
    23 : {
        "number" : 8197,
        "OPR" : -2.98
    },
    24 : {
        "number" : 8217,
        "OPR" : 16.61
    }
    #39 : {
    #    "number" : 8357,
    #    "OPR" : (9.42+12.24+11.32)/3
    #}
}

#assemble teams into different alliances so that everyone plays (5 times?)

positions = []
n = 0
while n < 10000:
    chantilly = -1
    while chantilly == -1:
        i = 0
        chosen = []
        team1 = []
        team2 = []
        team3 = []
        while i < 8:
            int = random.randint(0,24)
            while int in chosen:
                int = random.randint(0,24)
            chosen.append(int)
            int2 = random.randint(0,24)
            while int2 in chosen:
                int2 = random.randint(0,24)
            chosen.append(int2)
            int3 = random.randint(0,24)
            while int3 in chosen:
                int3 = random.randint(0,24)
            chosen.append(int3)
            team1.append(int)
            team2.append(int2)
            team3.append(int3)
            if int == 0 or int2 == 0 or int3 == 0:
                chantilly = i
            i += 1

    #"fight" against each using combined OPR of teams

    i = 0
    opr = []
    chantillyOPR = 0
    while i < 8:
        opr1 = teams[team1[i]].get("OPR")
        opr2 = teams[team2[i]].get("OPR")
        opr3 = teams[team3[i]].get("OPR")
        opr.append(opr1+opr2+opr3)
        if i == chantilly:
            chantillyOPR = opr1+opr2+opr3
        i += 1

    opr.sort(reverse=True)
    for position, item in enumerate(opr):
        if item == chantillyOPR:
            positions.append(position)
    n += 1

#save rank of knightrix into csv

with open('OwingsMills.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, dialect='excel')
                for position in positions:
                    writer.writerow([position])

#do multiple times then open csv in excel to plot