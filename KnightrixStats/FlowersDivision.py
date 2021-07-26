import random
import csv

#read the oprs for each team, maybe use dictionary.

teams = {
    0 : {
        "number" : 3749,
        "OPR" : 37.5
    },
    1 : {
        "number" : 4592,
        "OPR" : 19
    },
    2 : {
        "number" : 4969,
        "OPR" : 38.1
    },
    3 : {
        "number" : 5904,
        "OPR" : 10.5
    },
    4 : {
        "number" : 6700,
        "OPR" : 37.2
    },
    5 : {
        "number" : 6931,
        "OPR" : 54.4
    },
    6 : {
        "number" : 7080,
        "OPR" : 37.9
    },
    7 : {
        "number" : 7182,
        "OPR" : 44.8
    },
    8 : {
        "number" : 7278,
        "OPR" : 23.2
    },
    9 : {
        "number" : 8221,
        "OPR" : 73.1
    },
    10 : {
        "number" : 8297,
        "OPR" : 58
    },
    11 : {
        "number" : 8619,
        "OPR" : 14.8
    },
    12 : {
        "number" : 8788,
        "OPR" : 41.5
    },
    13 : {
        "number" : 9073,
        "OPR" : 32.6
    },
    14 : {
        "number" : 9794,
        "OPR" : 48
    },
    15 : {
        "number" : 11112,
        "OPR" : 56.8
    },
    16 : {
        "number" : 12096,
        "OPR" : 56
    },
    17 : {
        "number" : 12838,
        "OPR" : 6.8
    },
    18 : {
        "number" : 13599,
        "OPR" : 21.9
    },
    19 : {
        "number" : 13804,
        "OPR" : 28.4
    },
    20 : {
        "number" : 14616,
        "OPR" : 5.2
    },
    21 : {
        "number" : 15304,
        "OPR" : 52.4
    },
    22 : {
        "number" : 15317,
        "OPR" : 7.4
    },
    23 : {
        "number" : 15325,
        "OPR" : 51.4
    },
    24 : {
        "number" : 15360,
        "OPR" : 30.5
    },
    25 : {
        "number" : 16312,
        "OPR" : 12.8
    },
    26 : {
        "number" : 16809,
        "OPR" : 12
    },
    27 : {
        "number" : 17160,
        "OPR" : 21.7
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
    knightrix = 0
    while i < 14:
        int = random.randint(0,27)
        while int in chosen:
            int = random.randint(0,27)
        chosen.append(int)
        int2 = random.randint(0,27)
        while int2 in chosen:
            int2 = random.randint(0,27)
        chosen.append(int2)
        team1.append(int)
        team2.append(int2)
        if int == 13 or int2 == 13:
            knightrix = i
        i += 1

    #"fight" against each using combined OPR of teams

    i = 0
    opr = []
    knightrixOPR = 0
    while i < 14:
        opr1 = teams[team1[i]].get("OPR")
        opr2 = teams[team2[i]].get("OPR")
        opr.append(opr1+opr2)
        if i == knightrix:
            knightrixOPR = opr1+opr2
        i += 1

    opr.sort(reverse=True)
    for position, item in enumerate(opr):
        if item == knightrixOPR:
            positions.append(position+1)
    n += 1

#save rank of knightrix into csv

with open('flowers.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, dialect='excel')
                for position in positions:
                    writer.writerow([position])

#do multiple times then open csv in excel to plot