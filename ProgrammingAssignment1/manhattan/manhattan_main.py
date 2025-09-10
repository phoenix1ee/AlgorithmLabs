#Shun Fai Lee 621.83 Programming Assignment1

from sys import setrecursionlimit
setrecursionlimit(30000)

from pathlib import Path
import argparse
from time import time_ns
import manhattan

def coordinates(in_str:str):
    delimiter=in_str.find(",")
    if in_str[:delimiter].isnumeric and in_str[delimiter+1:].isnumeric:
        return int(in_str[:delimiter]), int(in_str[delimiter+1:])
    else:
        return None


def readPoints(in_path):
    """
    read input file containing lines of coordinates points 
    example line:1,3
    convert and output a list of input data
    :param input_f :a file object which contain some coordinates points
    :return: the list of input data
    """
    points = []
    print(in_path)
    with open(in_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',')  # Change delimiter if needed
        for row in reader:
            if row:
                points.append([int(row[0]),int(row[1])])
    return points

def writeResults(output_f, result):
    """
    obtain an output file and write the result list to the output file
    example line:1,3
    :param output_f :a file object for written to
    :param result : the list containing the output data
    :return: None
    """
    with (output_f.open('w') as file):
        for x in result:
            file.write(str(x))
            file.write("\n")

def writeAnalysis(output_f, result):
    """
    write analysis to output file
    example line:inputfilename, data size, m size, processing time(ns)
    :param output_f :a file object for written to
    :param result : the list containing an entry of analysis data
    :return: None
    """
    pass

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='calculate manhattan distance and return closet m pairs')
this_parser.add_argument('-l', action='store_true', help="Optional, to support batch input by inputing a file containing list of local files")
this_parser.add_argument('n_file', type=str, help="Input File containing the coordinates")
this_parser.add_argument('m', type=int, help="No. of closet pairs needed")
this_parser.add_argument('-o', action='store_true', help="Optional, print the manhattan result list to file")
this_parser.add_argument('-r', action='store_true', help="Optional, repeat manhattan process for accurate analysis")
this_parser.add_argument('-a', action='store_true', help="Optional, print to include the analysis details in output")

args = this_parser.parse_args()

# Set the input and output file path
in_path = Path(args.n_file)

if not args.m.isnumeric():
    raise Exception(f'argument for m, {args.m}, is not valid, expect integer')

if in_path.is_file():
    #read the points from file

    #proceed to start calculation and procesisng if input file exists, and return analysis data if applicable
    
    #write the results to file if necessary
    #start if input file exists
    if not args.l:
        #read the points from file
        coordinate = readPoints(in_path)
        #start calculation and time the process
        start_time = time_ns()
        result = manhattan(coordinate,int(args.m))
        end_time = time_ns()
        #set output file
        if args.o:
            filename = str(in_path.name)
            out_path = str(in_path.absolute())
            out_pathdir = out_path[:len(out_path) - len(filename)]
            out_pathreal = Path(out_pathdir + "output_"+ "_" + filename)
            writeResults(out_pathreal,result)
        if args.a:
            print("processing statistics:")
            print("file, data size, m size, processing time(ns)")
            print(args.n_file, len(coordinate), args.m, "%.2f" % (end_time - start_time), sep=",")
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
                if f_path.is_file():
                    #read the points from file
                    coordinate = readPoints(f_path)
                    #start calculation and time the process
                    start_time = time_ns()
                    result = manhattan(coordinate,int(args.m))
                    end_time = time_ns()
                    #set output file
                    with (f_path.open('r') as in_file2):
                        start_time = time_ns()
                        num_list, compare, exchange  = sortthisway(in_file2,args.t,f_path.absolute())
                        filename = str(f_path.name)
                        if args.o:
                            out_path = str(f_path.absolute())
                            out_pathdir = out_path[:len(out_path) - len(filename)]
                            out_pathreal = Path(out_pathdir + "output_" + args.t + "_"  + filename)
                            writeResults(out_pathreal,result)
                        if args.a:
                            print(args.n_file, len(coordinate), args.m, "%.2f" % (end_time - start_time), sep=",")
                else:
                    print(f'{f_path.absolute()} in file list supplied do not exist')
else:
    raise Exception(f'input file in {in_path.absolute()} do not exist')