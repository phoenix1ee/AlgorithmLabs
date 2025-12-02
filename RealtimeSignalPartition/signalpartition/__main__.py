#Shun Fai Lee 621.83 Programming Assignment4

from sys import setrecursionlimit
setrecursionlimit(1000000)

import csv
from pathlib import Path
import argparse
from signalpartition.signalpartition import SignalMonitor


# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='real time signal partitioning')
this_parser.add_argument('n_file', type=str, help="Input data")
this_parser.add_argument('-a', action='store_true', help="Optional, print to include the analysis details in output")

args = this_parser.parse_args()

# Set the input file path
in_path = Path(args.n_file)

# set trace output switch
analysis = False
if args.a:
    analysis = not analysis

if in_path.is_file():
    #start if input file exists
    #read the input from file
    data = list()
    with open(in_path, mode="r") as file:
        reader = csv.reader(file, delimiter=",")
        for line in reader:
            data.append([i for i in line])
    for i in data:
        print(f"test case identifier:{i[0]}\nsignal stream: ")
        if len(i[1])>35:
            print(i[1][:35], end="")
            print("...")
        else:
            print(i[1])
        print(f"x: {i[2]}")
        print(f"y: {i[3]}")
        #process the signal
        sgm = SignalMonitor(i[2],i[3])
        for j in range(len(i[1])):
            sgm.push(i[1][j])
        noise,x,y,push,pop = sgm.output()
        #print final assignment if necessary
        if analysis:
            print(f"index of signal x: {x}")
            print(f"index of signal y: {y}")
            print(f"index of noise: {noise}")
        if len(x)>0 or len(y)>0:
            print(f"the test case {i[0]} is an interweaving of ship x and y signals")
        print("statistics:")
        print("case identifier, data size, number of push, number of pop")
        print(i[0], len(i[1]), push, pop, sep=",")
else:
    raise Exception(f'input file in {in_path.absolute()} do not exist')