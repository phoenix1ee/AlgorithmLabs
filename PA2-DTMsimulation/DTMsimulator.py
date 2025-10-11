from sys import setrecursionlimit
setrecursionlimit(30000)

from readDTM import readDTM
from pathlib import Path
import argparse
from tape import tape

def DTMsimulate(DTM,in_tape:tape)->bool:
    currentstate="q0"
    round = 1
    while currentstate not in ("qY","qN"):
        currentsymbol = in_tape.now.v
        in_tape.write(DTM[currentstate][currentsymbol][1])
        in_tape.move(int(DTM[currentstate][currentsymbol][2]))
        currentstate = DTM[currentstate][currentsymbol][0]
        print(f"round{round}: tape: {in_tape.print()}")
        round+=1
    print(f"final state: {in_tape.print()}")
    return True if currentstate == "qY" else False


# Testing
if __name__ == "__main__":
    # use the Argument parser to define compulsory and optional arguments
    this_parser = argparse.ArgumentParser(description ='calculate manhattan distance and return closet m pairs')
    this_parser.add_argument('n_file', type=str, help="Input File containing the coordinates")
    this_parser.add_argument('-o', action='store_true', help="Optional, print the manhattan result list to file")

    args = this_parser.parse_args()

    # Set the input file path
    in_path = Path(args.n_file)

    if in_path.is_file():
        DTM = readDTM(in_path)
    else:
        raise Exception(f'input file in {in_path.absolute()} do not exist')
    test = tape("111000")
    print(DTMsimulate(DTM,test))