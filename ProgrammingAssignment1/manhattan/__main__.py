#Shun Fai Lee 621.83 Programming Assignment1

from sys import setrecursionlimit
setrecursionlimit(30000)

from pathlib import Path
import argparse
from time import time_ns
from manhattan.readPoints import readPoints
from manhattan.writeResults import writeResults
from manhattan.manhattan import Manhattan
from manhattan.writeAnalysis import writeAnalysis

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='calculate manhattan distance and return closet m pairs')
this_parser.add_argument('-l', action='store_true', help="Optional, to support batch input by inputing a file containing list of local files")
this_parser.add_argument('n_file', type=str, help="Input File containing the coordinates")
this_parser.add_argument('m', type=int, help="No. of closet pairs needed")
this_parser.add_argument('-o', action='store_true', help="Optional, print the manhattan result list to file")
this_parser.add_argument('-a', action='store_true', help="Optional, print to include the analysis details in output")
this_parser.add_argument('-r','--repeat',type=int,nargs='?',const=1,default=1, help="Optional, repeat manhattan process for certain times for accurate analysis")

args = this_parser.parse_args()

# Set the input and output file path
in_path = Path(args.n_file)

if not int(args.m):
    raise Exception(f'argument for m, {args.m}, is not valid, expect integer')

if in_path.is_file():
    #start if input file exists
    if not args.l:
        #read the points from file
        coordinate = readPoints(in_path)
        #start calculation and time the process
        t_time = 0
        for i in range(args.repeat):
            start_time = time_ns()
            result = Manhattan(coordinate,int(args.m))
            end_time = time_ns()
            print("%.2f" % (end_time - start_time))
            t_time += end_time - start_time
        t_time = t_time//args.repeat
        #write the result list to file
        if args.o:
            filename = str(in_path.name)
            out_path = str(in_path.absolute())
            out_pathdir = out_path[:len(out_path) - len(filename)]
            out_pathreal = Path(out_pathdir + "output_" + filename)
            writeResults(out_pathreal,result)
        #return analysis data if applicable
        if args.a:
            print("processing statistics:")
            print("file, data size, m size, processing time(ns)")
            print(args.n_file, len(coordinate), args.m, "%.2f" % t_time, sep=",")
    else:
        filelist=[]
        with (in_path.open('r') as in_file):
            for line in in_file:
                line_s = line.strip().replace(" ", "")
                if line_s:
                    filelist.append(line_s)
            if args.a:
                print("processing statistics:")
                print("file, data size, m size, processing time(ns)")
            for f_name in filelist:
                f_path = Path(f_name)
                print(f_path.absolute())
                if f_path.is_file():
                    #read the points from file
                    coordinate = readPoints(f_path)
                    #start calculation and time the process
                    t_time = 0
                    for i in range(args.repeat):
                        start_time = time_ns()
                        result = Manhattan(coordinate,int(args.m))
                        end_time = time_ns()
                        print("%.2f" % (end_time - start_time))
                        t_time += end_time - start_time
                    t_time = t_time//args.repeat
                    #write the result list to file
                    if args.o:
                        childname = f_name[len(str(f_path.absolute().parent))+1:]
                        out_pathreal = Path(str(f_path.absolute().parent)+"\\" + "output_" + childname)
                        writeResults(out_pathreal,result)
                    if args.a:
                        print(childname, len(coordinate), args.m, "%.2f" % t_time, sep=",")
                else:
                    print(f'{f_path.absolute()} in file list supplied do not exist')
else:
    raise Exception(f'input file in {in_path.absolute()} do not exist')