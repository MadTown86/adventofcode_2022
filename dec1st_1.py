import dotenv
import os

dv = dotenv.DotEnv(os.getenv('localAdvent2022'))
lp_proj = dv.get("root_local")
fname = lp_proj + "\\" + 'dec1st_1_input.txt'

def inputreader(file):
    highest = 0
    second = 0
    third = 0
    count = 0
    with open(file, 'r') as lp:
        for line in lp:
            if len(line) > 1:
                count += int(line)

            elif len(line) == 1:

                if highest == 0:
                    highest = count
                elif highest > count > second > third:
                    third = second
                    second = count
                elif second > count > third:
                    third = count
                elif highest < count:
                    third = second
                    second = highest
                    highest = count
                elif second < count < highest:
                    third = second
                    second = count
                elif third < count < second:
                    third = count
                count = 0

    return highest + second + third



if __name__ == "__main__":
    print(inputreader(fname))
