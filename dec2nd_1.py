import dotenv
import os

dv = dotenv.DotEnv(os.getenv('localAdvent2022'))
lp_proj = dv.get("root_local")
fname = lp_proj + "\\" + 'dec2nd_1_input.txt'

# A, X - Rock (1)
# B, Y - Paper (2)
# C, Z - Scissors (3)
# 0, 3, 6 (loss, draw, win)
def elfoncrackthecode(fname):
    score = 0
    wins = {'A Y': [2, 6], 'B Z': [3, 6], 'C X': [1, 6]}
    loss = {'A Z': [3, 0], 'B X': [1, 0], 'C Y': [2, 0]}
    draw = {'A X': [1, 3], 'B Y': [2, 3], 'C Z': [3, 3]}
    with open(fname, 'r') as fp:
        tolist = fp.readlines()
        tolist = [x[:3] for x in tolist]
        for line in tolist:
            if line in wins.keys():
                score += wins[line][0] + wins[line][1]
            elif line in loss.keys():
                score += loss[line][0] + loss[line][1]
            else:
                score += draw[line][0] + draw[line][1]

    return score
# X - LOSE, Y - DRAW, Z - WIN
def elfoncrackthecode2(fname):
    score = 0
    wins = {'A Y': [1, 3], 'B Z': [3, 6], 'C X': [2, 0]}
    loss = {'A Z': [2, 6], 'B X': [1, 0], 'C Y': [3, 3]}
    draw = {'A X': [3, 0], 'B Y': [2, 3], 'C Z': [1, 6]}
    with open(fname, 'r') as fp:
        tolist = fp.readlines()
        tolist = [x[:3] for x in tolist]
        for line in tolist:
            if line in wins.keys():
                score += wins[line][0] + wins[line][1]
            elif line in loss.keys():
                score += loss[line][0] + loss[line][1]
            else:
                score += draw[line][0] + draw[line][1]

    return score

if __name__ == "__main__":
    print(elfoncrackthecode2(fname))