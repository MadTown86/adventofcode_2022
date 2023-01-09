import math
import os
import dotenv

# With refactoring help Muumi

dotenv.load_dotenv()
input_dir = os.getenv('adventofcode2022', '.')
fname = os.path.join(input_dir, 'dec8thinput.txt')

with open(fname, 'r') as f:
    lines = f.read().splitlines()

num_rows = len(lines)
num_cols = len(lines[0])
count = 0

for x in range(num_rows):
    for y in range(num_cols):
        nrange = range(x - 1, -1, -1)
        srange = range(x + 1, num_rows, 1)
        erange = range(y + 1, num_cols, 1)
        wrange = range(y - 1, -1, -1)

        pos = lines[x][y]

        count += any((
            x == 0, y == 0, x == num_rows - 1, y == num_cols - 1,
            all(lines[xx][y] < pos for xx in nrange),
            all(lines[xx][y] < pos for xx in srange),
            all(lines[x][yy] < pos for yy in erange),
            all(lines[x][yy] < pos for yy in wrange)
        ))

print(f'ANS1: {count}')


highest_rank = [0, 0], 0
rank = 0
for x in range(num_rows):
    for y in range(num_cols):
        ncount, scount, ecount, wcount = 0, 0, 0, 0
        pos = lines[x][y]

        nrange = range(x - 1, -1, -1)
        srange = range(x + 1, num_rows, 1)
        erange = range(y + 1, num_cols, 1)
        wrange = range(y - 1, -1, -1)

        scores = []
        for xrange in (nrange, srange):
            visibility = 0
            for xx in xrange:
                visibility += 1
                if pos <= lines[xx][y]:
                    break
            scores.append(visibility)

        for yrange in (erange, wrange):
            visibility = 0
            for yy in yrange:
                visibility += 1
                if pos <= lines[x][yy]:
                    break
            scores.append(visibility)

        rank = math.prod(scores)

        if rank > highest_rank[1]:
            highest_rank = ([x, y], rank)

print(f'ANS2: {highest_rank}')