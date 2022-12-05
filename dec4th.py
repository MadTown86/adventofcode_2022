import dotenv
import os

dv = dotenv.DotEnv(os.getenv('localAdvent2022'))
lp_proj = dv.get("root_local")
fname = lp_proj + "\\" + 'dec4thinput.txt'

def innyoutty(fname):
    with open(fname, 'r') as fp:
        inp = [x[:-1].split(',') for x in fp.readlines()]
        count = 0
        for x, y in inp:
            f, s = x.split('-')
            t, fo = y.split('-')
            terms = lambda f, s, t, fo: [f-t, s-fo]

            if terms:
                count += 1

        return count

if __name__ == "__main__":
    print(innyoutty(fname))