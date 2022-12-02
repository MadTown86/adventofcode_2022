import dotenv
import os

dotenv.load_dotenv(os.getenv('advent2002env'))
lp_proj = dotenv.get_key(os.getenv('advent2002env'), "p_proj")
fname = 'dec1st_1_input.txt'

def inputreader(file):
    binser = []
    count = 0
    with open(lp_proj + file, 'r') as lp:
        count = 0
        for line in lp:
            if line:
                count += line
            else:
                binser.append(count)


def nourishedelves(*args):
    well = []
    for line in args:
        if line:
