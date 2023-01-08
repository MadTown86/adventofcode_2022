import dotenv, os

lp_proj = dotenv.get_key(os.getenv('adventofcode2022'), 'root_local')
fname = lp_proj + "\\" + 'dec8thinput.txt'

with open(fname, 'r') as f:
    lines = f.read().splitlines()

totl = len(lines)
count = 0
res_list = []

step_x = lambda x: lines[x][y]
step_y = lambda y: lines[x][y]
nrange = lambda x: list(range(x - 1, -1, -1))
srange = lambda x: list(range(x + 1, totl, 1))
erange = lambda y: list(range(y + 1, totl, 1))
wrange = lambda y: list(range(y - 1, -1, -1))

for x in range(totl):
    for y in range(totl):

        if x == 0 or y == 0 or x == totl - 1 or y == totl - 1:
            count += 1
            continue

        pos = lines[x][y]

        flag = True
        for xn in nrange(x):
            if pos <= step_x(xn):
                break
            if xn == 0:
                if pos > step_x(xn):
                    count += 1
                    res_list.append(([x, y], pos, count))
                    flag = False
                    break
        if flag:
            for xs in srange(x):
                if pos <= step_x(xs):
                    break
                if xs == totl-1:
                    if pos > step_x(xs):
                        count += 1
                        res_list.append(([x, y], pos, count))
                        flag = False
                        break
        if flag:
            for ye in erange(y):
                if pos <= step_y(ye):
                    break
                if ye == totl-1:
                    if pos > step_y(ye):
                        count += 1
                        res_list.append(([x, y], pos, count))
                        flag = False
                        break
        if flag:
            for yw in wrange(y):
                if pos <= step_y(yw):
                    break
                if yw == 0:
                    if pos > step_y(yw):
                        count += 1
                        res_list.append(([x, y], pos, count))
                        flag = False
                        break

print(res_list)
print(f' ANS1: {count}')


res_list2 = []
highest_rank = [0, 0], 0
rank = 0
for x in range(totl):
    for y in range(totl):
        ncount, scount, ecount, wcount = 0, 0, 0, 0
        pos = lines[x][y]

        if x != 0:
            for xn in nrange(x):
                if pos > step_x(xn):
                    ncount += 1
                if pos <= step_x(xn):
                    ncount += 1
                    break
        if x != totl:
            for xs in srange(x):
                if pos > step_x(xs):
                    scount += 1
                if pos <= step_x(xs):
                    scount += 1
                    break

        if y != 0:
            for ye in erange(y):
                if pos > step_y(ye):
                    ecount += 1
                if pos <= step_y(ye):
                    ecount += 1
                    break

        if y != totl:
            for yw in wrange(y):
                if pos > step_y(yw):
                    wcount += 1
                if pos <= step_y(yw):
                    wcount += 1
                    break

        rank = ncount * scount * ecount * wcount

        print(f'RANK: {rank}')

        res_list2.append(([x, y], [ncount, scount, ecount, wcount], pos, rank))

        if rank > highest_rank[1]:
            highest_rank = ([x, y], rank)

for item in res_list2:
    print(item)
print(f'Ans2: {highest_rank}')




