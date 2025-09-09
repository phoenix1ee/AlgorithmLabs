#Shun Fai Lee 621.83 Programming Assignment1

from sys import setrecursionlimit
setrecursionlimit(30000)

from pathlib import Path
import argparse
from time import time_ns


def coordinates(in_str:str):
    delimiter=in_str.find(",")
    if in_str[:delimiter].isnumeric and in_str[delimiter+1:].isnumeric:
        return int(in_str[:delimiter]), int(in_str[delimiter+1:])
    else:
        return None


def readPoints(input_f):
    """
    read input file containing lines of coordinates points 
    example line:1,3
    convert and output a list of input data
    :param input_f :a file object which contain some coordinates points
    :return: the list of input data
    """
    points = []
    error = []
    line = 0
    for l in input_f:
        line += 1
        in_c = l.strip().replace(" ", "")
        if in_c and in_c.isnumeric():
            pass
        else:
            if len(in_c) == 0:
                error.append((line, "empty line"))
            else:
                error.append((line, "invalid line"))
    return points, error

def writeResults(output_f, result):
    """
    obtain an output file and write the result list to the output file
    example line:1,3
    :param output_f :a file object for written to
    :param result : the list containing the output data
    :return: None
    """
    pass

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='calculate manhattan distance and return closet m pairs')
this_parser.add_argument('-l', action='store_true', help="Optional, to support batch input by inputing a file containing list of local files")
this_parser.add_argument('n_file', type=str, help="Input File containing the coordinates")
this_parser.add_argument('m', type=int, help="No. of closet pairs needed")
this_parser.add_argument('-a', action='store_true', help="Optional, print to include the analysis details in output")
args = this_parser.parse_args()

# Set the input and output file path
in_path = Path(args.n_file)

if in_path.is_file():
    #proceed to start calculation and procesisng if input file exists, and return analysis data if applicable
    with (in_path.open('r') as in_file):
        if not args.l:
            filename = str(in_path.name)
            out_path = str(in_path.absolute())
            out_pathdir = out_path[:len(out_path) - len(filename)]
            out_pathreal = Path(out_pathdir + "output_"+ "_" + filename)
            output_file = out_pathreal.open('w')

            start_time = time_ns()
            num_list, compare, exchange = sortthisway(in_file,args.t,in_path.absolute())
            printout(num_list, compare, exchange, output_file, in_path.absolute())
            end_time = time_ns()
            if args.a:
                print("processing statistics:")
                print("file, sort type, no. of comparison, no. of exchange, processing time(ns)")
                print(args.n_file, args.t, compare, exchange, "%.2f" % (end_time - start_time), sep=",")
        else:
            filelist=[]
            for line in in_file:
                line_s = line.strip().replace(" ", "")
                if line_s:
                    filelist.append(line_s)
            if args.a:
                print("processing statistics:")
                print("file, sort type, no. of comparison, no. of exchange, processing time(ns)")
            for f_name in filelist:
                f_path = Path(f_name)
                if f_path.is_file():
                    with (f_path.open('r') as in_file2):
                        start_time = time_ns()
                        num_list, compare, exchange  = sortthisway(in_file2,args.t,f_path.absolute())
                        filename = str(f_path.name)
                        out_path = str(f_path.absolute())
                        out_pathdir = out_path[:len(out_path) - len(filename)]
                        out_pathreal = Path(out_pathdir + "output_" + args.t + "_"  + filename)
                        output_file = out_pathreal.open('w')
                        printout(num_list,compare, exchange, output_file,f_path.absolute())
                        end_time = time_ns()
                        if args.a:
                            print(f_name,args.t,compare,exchange,"%.2f" % (end_time - start_time),sep=",")
                else:
                    print(f'{f_path.absolute()} in file list supplied do not exist')
else:
    raise Exception(f'input file in {in_path.absolute()} do not exist')