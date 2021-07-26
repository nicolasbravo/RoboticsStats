import random
import csv

#read the oprs for each team, maybe use dictionary.

teams = {
    0 : {
        "number" : 116,
        "OPR" : (2.89+8.46)/2
    },
    1 : {
        "number" : 339,
        "OPR" : (12.7+15.2+30.59)/3
    },
    2 : {
        "number" : 539,
        "OPR" : (20.15+26.93+22.15)/3
    },
    3 : {
        "number" : 611,
        "OPR" : (13.75+19.19)/2
    },
    4 : {
        "number" : 612,
        "OPR" : (25.9+24.81+20.13)/3
    },
    5 : {
        "number" : 614,
        "OPR" : (32.59+11.94+30.86+15.17)/4
    },
    6 : {
        "number" : 620,
        "OPR" : (4.87+18.86)/2
    },
    7 : {
        "number" : 623,
        "OPR" : (10.5+14.7)/2
    },
    8 : {
        "number" : 686,
        "OPR" : (18.79+23.84+17.37)/3
    },
    9 : {
        "number" : 836,
        "OPR" : (26.64+25.51+30.71+19.43)/4
    },
    10 : {
        "number" : 1111,
        "OPR" : (10.61+15+16.78)/3
    },
    11 : {
        "number" : 1123,
        "OPR" : (6.7+17.32+12.71)/3
    },
    12 : {
        "number" : 1418,
        "OPR" : (22.22+27.96+30.31+29.2)/4
    },
    13 : {
        "number" : 1719,
        "OPR" : (17.53+24.71+19.51)/3
    },
    14 : {
        "number" : 1727,
        "OPR" : (26.38+21.88+22.32)/3
    },
    15 : {
        "number" : 1731,
        "OPR" : (13.39+23.92+27.75)/3
    },
    16 : {
        "number" : 1895,
        "OPR" : (18.97+19.4)/2
    },
    17 : {
        "number" : 1915,
        "OPR" : (6.05+2.99)/2
    },
    18 : {
        "number" : 2186,
        "OPR" : (6.93+4.73)/2
    },
    19 : {
        "number" : 2199,
        "OPR" : (17.83+29.42+25.87)/3
    },
    20 : {
        "number" : 2363,
        "OPR" : (19.74+15.66+22.42)/3
    },
    21 : {
        "number" : 2421,
        "OPR" : (7.06+9.28)/2
    },
    22 : {
        "number" : 2819,
        "OPR" : (2.89+14.24)/2
    },
    23 : {
        "number" : 2849,
        "OPR" : (11.46+16.26+24.41)/3
    },
    24 : {
        "number" : 2900,
        "OPR" : (5.1+11.39)/2
    },
    25 : {
        "number" : 2988,
        "OPR" : (17.91+18.43)/2
    },
    26 : {
        "number" : 3274,
        "OPR" : (4.45+11.16+10.41)/3
    },
    27 : {
        "number" : 3373,
        "OPR" : (14.78+14.57)/2
    },
    28 : {
        "number" : 3650,
        "OPR" : (7.69+16.96)/2
    },
    29 : {
        "number" : 4099,
        "OPR" : (16.81+19.71+16.02)/3
    },
    30 : {
        "number" : 4472,
        "OPR" : (22.33+19.44+20.89+32.56)/4
    },
    31 : {
        "number" : 4505,
        "OPR" : (13.96+15.07+18.52)/3
    },
    32 : {
        "number" : 5243,
        "OPR" : (10+17.87+16.54+22.16)/4
    },
    33 : {
        "number" : 5546,
        "OPR" : (13.29+16.95+21.14)/3
    },
    34 : {
        "number" : 6504,
        "OPR" : (11.22+7.4)/2
    },
    35 : {
        "number" : 6882,
        "OPR" : (9.42+12.24+11.32)/3
    }
}

#assemble teams into different alliances so that everyone plays (5 times?)

positions = []
n = 0
while n < 10000:
    i = 0
    chosen = []
    team1 = []
    team2 = []
    team3 = []
    chantilly = 0
    while i < 12:
        int = random.randint(0,35)
        while int in chosen:
            int = random.randint(0,35)
        chosen.append(int)
        int2 = random.randint(0,35)
        while int2 in chosen:
            int2 = random.randint(0,35)
        chosen.append(int2)
        int3 = random.randint(0,35)
        while int3 in chosen:
            int3 = random.randint(0,35)
        chosen.append(int3)
        team1.append(int)
        team2.append(int2)
        team3.append(int3)
        if int == 4 or int2 == 4 or int3 == 4:
            chantilly = i
        i += 1

    #"fight" against each using combined OPR of teams

    i = 0
    opr = []
    chantillyOPR = 0
    while i < 12:
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

with open('Haymarket.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, dialect='excel')
                for position in positions:
                    writer.writerow([position])

#do multiple times then open csv in excel to plot