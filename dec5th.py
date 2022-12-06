import dotenv
import os
from collections import defaultdict

dv = dotenv.DotEnv(os.getenv('localAdvent2022'))
lp_proj = dv.get("root_local")
fname = lp_proj + "\\" + 'dec5thinput.txt'

def stackitgood(fname):
    with open(fname, 'r') as fp:
        lines = [x[:-1] for x in fp.readlines()]
        d = defaultdict(list)
        # build stacks
        for line in lines:
            for ind in range(len(line)-1):
                if line[ind].isalpha() and line[ind].isupper():
                    d[ind] += line[ind]

        stack = {}
        numbbin = sorted([x for x in range(1, 10)], reverse=True)
        for x, y in sorted(d.items()):
            stack[numbbin.pop()] = [x for x in reversed(y)]
        print(stack)



if __name__ == "__main__":
    print(stackitgood(fname))