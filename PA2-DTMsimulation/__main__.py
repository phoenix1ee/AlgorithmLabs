#Shun Fai Lee 621.83 Programming Assignment2

from sys import setrecursionlimit
setrecursionlimit(30000)

from pathlib import Path
import argparse

from readDTM import readDTM
from tape import tape
from DTMsimulator import DTMsimulate

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='calculate manhattan distance and return closet m pairs')
this_parser.add_argument('n_file', type=str, help="Input File containing the coordinates")
this_parser.add_argument('-o', action='store_true', help="Optional, print the manhattan result list to file")

args = this_parser.parse_args()

# Set the input file path
in_path = Path(args.n_file)

if in_path.is_file():
    DTM = readDTM(in_path)
    test = "111000b"
    print(DTMsimulate(DTM,test))
    print(test)
else:
    raise Exception(f'input file in {in_path.absolute()} do not exist')