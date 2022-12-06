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
            a, b = terms(int(f), int(s), int(t), int(fo))
            conditions = True if a <= 0 <= b or a >= 0 >= b else False
            if conditions:
                count += 1
        return count

def overlappy(fname):
    with open(fname, 'r') as fp:
        count = 0
        inp = [x[:-1].split(',') for x in fp.readlines()]
        for x, y in inp:
            f, s = x.split('-')
            t, fo = y.split('-')
            cond1 = True if int(f) < int(t) > int(s) or int(f) > int(fo) < int(s) else False

            if cond1:
                continue
            else:
                count += 1

        return count

if __name__ == "__main__":
    print(overlappy(fname))