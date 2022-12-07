import dotenv
import os

dv = dotenv.DotEnv(os.getenv('localAdvent2022'))
lp_proj = dv.get("root_local")
fname = lp_proj + "\\" + 'dec6thinput.txt'

def signal(fname):
    with open(fname) as fp:
        i = fp.read()
        j = 3
        top = len(i)
        while j < top:
            t1 = True if i[j] != i[j-1] else False
            t2 = True if i[j] != i[j-2] else False
            t3 = True if i[j] != i[j-3] else False
            t4 = True if i[j-2] != i[j-3] else False
            t5 = True if i[j-1] != i[j-2] else False
            t6 = True if i[j-1] != i[j-3] else False
            if t1 and t2 and t3 and t4 and t5 and t6:
                return j + 1, i[j], i[j-1], i[j-2], i[j-3]
            else:
                j += 1

def signal2(fname):
    with open(fname) as fp:
        i, p, b = fp.read(), 0, []
        while len(b) < 14:
            if i[p] not in b:
                b.append(i[p])
                p += 1
            else:
                fallback = len(b) - b.index(i[p]) - 1
                b = []
                p -= fallback
        return p

if __name__ == "__main__":
    print(signal2(fname))

