import dotenv
import os
from collections import defaultdict

dv = dotenv.DotEnv(os.getenv('localAdvent2022'))
lp_proj = dv.get("root_local")
fname = lp_proj + "\\" + 'dec5thinput.txt'

def stackitgood(fname):
    with open(fname, 'r') as fp:
        org_list = [x for x in fp.readlines()]

        # List of clean lines
        lines = [x[:-1] for x in org_list[:-1]]
        lines.append(org_list[-1])

        # Getting break point for moves and assembling clean moves
        ind = 0
        while len(lines[ind]) != 0:
            ind += 1
            continue
        splitpos = ind
        moves = lines[splitpos:]
        clean_moves = []
        for move in moves:
            if len(move) == 0:
                continue
            else:
                temp_list = move.split(" ")
                temp_overwrite = []
                for item in temp_list:
                    if item.isnumeric():
                        temp_overwrite.append(int(item))
                clean_moves.append(temp_overwrite)

        # Building stacks w/ list, reversed so pop == pop and append = push
        d = defaultdict(list)
        for line in lines:
            for ind in range(len(line)-1):
                if line[ind].isalpha() and line[ind].isupper():
                    d[ind] += line[ind]

        stack = {}
        numbbin = sorted([x for x in range(1, 10)], reverse=True)
        for x, y in sorted(d.items()):
            stack[numbbin.pop()] = [x for x in reversed(y)]


        def craneops_1(a, b, c):
            temp_container = []
            while a > 0:
                temp_container.append(stack[b].pop())
                stack[c].append(temp_container.pop())
                a -= 1
        def craneops_2(a, b, c):
            temp_container = []
            while a > 0:
                temp_container.append(stack[b].pop())
                a -= 1

            while len(temp_container) > 0:
                stack[c].append(temp_container.pop())

        for move in clean_moves:
            craneops_2(*move)
            for x, y in stack.items():
                print(y)
            print('\n')

if __name__ == "__main__":
    print(stackitgood(fname))