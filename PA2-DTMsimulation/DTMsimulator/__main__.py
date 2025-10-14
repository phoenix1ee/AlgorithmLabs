#Shun Fai Lee 621.83 Programming Assignment2

from sys import setrecursionlimit
setrecursionlimit(30000)

from pathlib import Path
import argparse

from DTMsimulator.readDTM import readDTM
from DTMsimulator.tape import tape
from DTMsimulator.DTMsimulate import printDTM , DTMsimulate

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='Simulate a DTM with input: csv file represeting DTM and test string')
this_parser.add_argument('n_file', type=str, help="Input File containing the DTM description")
this_parser.add_argument('inputstring', type=str, help="The input string")

args = this_parser.parse_args()

# Set the input file path
in_path = Path(args.n_file)

if in_path.is_file():
    print(f'read DTM specification from {in_path}')
    DTM = readDTM(in_path)
    printDTM(DTM)
    print(f'start operations:\ninput string is {args.inputstring}')
    testtape = tape(args.inputstring)
    Result , transition = DTMsimulate(DTM,testtape)
    print(f'Processing:{"Success" if Result else "Failed"}')
    if len(transition)>30:
        filename = str(in_path.name)
        out_path = str(in_path.absolute())
        out_pathdir = out_path[:len(out_path) - len(filename)]
        out_pathreal = Path(out_pathdir + "output.txt")
        with (out_pathreal.open('w') as file):
            for x in transition:
                file.write(str(x))
                file.write("\n")
else:
    raise Exception(f'input file in {in_path.absolute()} do not exist')