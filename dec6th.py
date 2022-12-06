import dotenv
import os

dv = dotenv.DotEnv(os.getenv('localAdvent2022'))
lp_proj = dv.get("root_local")
fname = lp_proj + "\\" + 'dec6thinput.txt'

def signal(fname):
    with open(fname) as fp:
        i = fp.read()
        j = 3
        test = True if i[j] != i[j - 1] and i[j] != i[j - 2] and i[j] != i[j - 3] and i[j - 2] != i[j - 3] else False
        t1 = True if i[j] != i[j-1] else False
        t2 = True if i[j] != i[j-2] else False
        t3 = True if i[j] != i[j-3])
        print(i[j-2] != i[j-3])


        top = len(i)
        while j < top:
            print(i[j] != i[j - 1])
            print(i[j] != i[j - 2])
            print(i[j] != i[j - 3])
            print(i[j - 2] != i[j - 3])
            print(test, j, i[j-3], i[j-2], i[j-1], i[j])
            if test:
                return j
            else:
                j += 1

if __name__ == "__main__":
    print(signal(fname))

