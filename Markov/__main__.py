#Shun Fai Lee 621.83 Programming Assignment2

from sys import setrecursionlimit
setrecursionlimit(30000)

from pathlib import Path
import argparse
from Markov.helperFunc import readMatrix
from Markov.matrixClass import matrix

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='Simulate a DTM with input: csv file represeting DTM and test string')
this_parser.add_argument('n_file', type=str, help="Input File containing the DTM description")

args = this_parser.parse_args()

# Set the input file path
in_path = Path(args.n_file)

if in_path.is_file():
    print(f'read Matrix specification from {in_path}')
    in_matrix = matrix(readMatrix(in_path))
    in_matrix.mprint()
    filename = str(in_path.name)
    out_path = str(in_path.absolute())
    out_pathdir = out_path[:len(out_path) - len(filename)]
    out_pathreal = Path(out_pathdir + "output.txt")
    #result of markov chain process
    # set as input matrix for now
    output = in_matrix.matrix
    with (out_pathreal.open('w') as file):
        for x in output:
            file.write(str(x))
            file.write("\n")
else:
    raise Exception(f'input file in {in_path.absolute()} do not exist')