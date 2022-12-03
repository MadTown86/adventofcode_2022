import dotenv
import os

dv = dotenv.DotEnv(os.getenv('localAdvent2022'))
lp_proj = dv.get("root_local")
fname = lp_proj + "\\" + 'dec3rd_input.txt'


def rucksackdecode(fname):
    with open(fname, 'r') as fp:
        tot = 0
        tolistorg = fp.readlines()
        print(len(tolistorg))
        tolist = [[x[:(len(x[:-1]) // 2)], x[:-1][len(x[:-1]) // 2:]] for x in tolistorg if x != tolistorg[-1]]
        tolist.append([tolistorg[-1][:(len(tolistorg[-1]) // 2)], tolistorg[-1][len(tolistorg[-1]) // 2:]])
        for x, y in tolist:
            flag = False
            for dig in x:
                if not flag:
                    if dig in y:
                        flag = True
                        if dig.isupper():
                            calc = (ord(dig) - ord('A')) + 27
                            tot += calc
                        else:
                            calc = (ord(dig) - ord('a')) + 1
                            tot += calc
        return tot

def badgeofhonor(fname):
    with open(fname, 'r') as fp:
        tolistorg = fp.readlines()
        tlo = [x for x in tolistorg]
        print(tlo)
        i = 0
        j = 1
        k = 2
        tot = 0
        testbin = {}
        while k < len(tlo):
            flag = False
            for dig in tlo[i]:
                if not flag:
                    if dig in tlo[j] and dig in tlo[k]:
                        flag = True
                        if dig.isupper():
                            calc = (ord(dig) - ord('A')) + 27
                            tot += calc
                        else:
                            calc = (ord(dig) - ord('a')) + 1
                            tot += calc

                        testbin[i] = (dig, calc)

            i += 3
            j += 3
            k += 3

        return tot, testbin






if __name__ == "__main__":
    print(badgeofhonor(fname))
