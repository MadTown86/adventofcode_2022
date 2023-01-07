import dotenv, os

lp_proj = dotenv.get_key(os.getenv('adventofcode2022'), 'root_local')
fname = lp_proj + "\\" + 'dec8thexample.txt'

with open(fname, 'r') as f:
    lines = f.read().splitlines()

x, y, count = 0, 0, 0

print(len(lines))
print(len(lines[0]))

for x in range(len(lines)):
    for y in range(len(lines[0])):
        if x == 0 or x == len(lines)-1:
            count += 1
        if y == 0 or y == len(lines[0])-1:
            count += 1

    if 0 < x < 99 and 0 < y < 99:
        pos = lines[x][y]
        n = lines[x-1][y]
        s = lines[x+1][y]
        e = lines[x][y+1]
        w = lines[x][y-1]
        if lines[x-1][y] < pos:
            for ind in range(x, 0, -1):
                if lines[ind][y] > pos:
                    break
                if ind == 0:
                    count += 1
        # if lines[x+1][y] < pos:
        #     for ind in range(x, 99, 1):
        #         if lines[ind][y] > pos:
        #             break
        #         if ind == 99:
        #             count += 1
        # if lines[x][y+1] < pos:
        #     for ind in range(y, 99, 1):
        #         if lines[x][ind] > pos:
        #             break
        #         if ind == 99:
        #             count += 1
        # if lines[x][y-1] < pos:
        #     for ind in range(y, 0, -1):
        #         if lines[x][ind] > pos:
        #             break
        #         if ind == 0:

print(count)













# loop through each position
# at each position check its n, s, e, w positions to see shorter/taller
# continue in each direction that is smaller until you reach an edge or a taller tree
# maintain count of trees viewable from exterior
# Count exterior trees
