import dotenv
import os

dv = dotenv.DotEnv(os.getenv('localAdvent2022'))
lp_proj = dv.get("root_local")
fname = lp_proj + "\\" + 'dec3rd_input.txt'

"""
Learning recap - I didn't need to do all of the garbage trying to 'slice' off the newline characters, they aren't being
considered at least they don't matter for the second part of the 3rd days question.
"""

def rucksackdecode(fname):
    with open(fname, 'r') as fp:
        tot = 0
        tolistorg = fp.readlines()
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
        i = 0
        j = 1
        k = 2
        tot = 0
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
            i += 3
            j += 3
            k += 3

        return tot

if __name__ == "__main__":
    print(badgeofhonor(fname))
