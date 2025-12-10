#Shun Fai Lee 621.83 Programming Assignment1

from sys import setrecursionlimit
setrecursionlimit(30000)

from pathlib import Path
import argparse
from time import time_ns
from manhattan.readPoints import readPoints
from manhattan.writeResults import writeResults
from manhattan.manhattan import Manhattan
from manhattan.manhattan_improvement import AcceleratedManhattan

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='calculate manhattan distance and return closet m pairs')
this_parser.add_argument('-l', action='store_true', help="Optional, to support batch input by inputing a file containing list of local files")
this_parser.add_argument('n_file', type=str, help="Input File containing the coordinates")
this_parser.add_argument('m', type=int, help="No. of closet pairs needed")
this_parser.add_argument('-o', action='store_true', help="Optional, print the manhattan result list to file")
this_parser.add_argument('-a', action='store_true', help="Optional, print to include the analysis details in output")
this_parser.add_argument('-r','--repeat',type=int,nargs='?',const=1,default=1, help="Optional, repeat manhattan process for certain times for accurate analysis")

args = this_parser.parse_args()

# Set the input file path
in_path = Path(args.n_file)

# check for valid m value
if not int(args.m):
    raise Exception(f'argument for m, {args.m}, is not valid, expect integer')

# set trace output switch
analysis = False
if args.a:
    analysis = not analysis

if in_path.is_file():
    #start if input file exists
    if not args.l:
        #read the points from file
        coordinate = readPoints(in_path)
        #print analysis message if applicable
        if analysis:
            print("input list is:")
            if len(coordinate)>10:
                print(coordinate[:10])
                print("only 1st 10 points are printed")
            else:
                print(coordinate)
            print(f'Total number of points: {len(coordinate)}')
            print("Start manhattan calculation.")
        #start manhattan distance calculation and record the time consumed
        part1_time = 0
        part2_time = 0
        for i in range(args.repeat):
            start_time = time_ns()
            result, mid_time = AcceleratedManhattan(coordinate,int(args.m),(analysis if i==0 else False))
            end_time = time_ns()
            part1_time += mid_time - start_time
            part2_time += end_time - mid_time
        part1_time = part1_time//args.repeat
        part2_time = part2_time//args.repeat
        t_time = part1_time+part2_time
        #print analysis dmessage if applicable
        if analysis:
            print(f'manhattan algorithm for the input list executed for {args.repeat} time.')
            print(f'average execution time ={"%.2f" % t_time}ns')
            print(f'Result of closet {args.m} pairs: ')
            if len(result)>10:
                for i in range(10):
                    print(f'{result[i][0]} , {result[i][1]}')
                print("only 1st 10 pairs are printed")
            else:
                for x in result:
                    print(f'{x[0]} , {x[1]}')
            print("statistics:")
            print("file, data size, m size, part1 processing time(ns), part2 processing time(ns)")
            print(args.n_file, len(coordinate), args.m, "%.2f" % part1_time, "%.2f" % part2_time, sep=",")
        #write the result list to file if applicable
        if args.o:
            filename = str(in_path.name)
            out_path = str(in_path.absolute())
            out_pathdir = out_path[:len(out_path) - len(filename)]
            out_pathreal = Path(out_pathdir + "output_" + filename)
            writeResults(out_pathreal,result)
    else:
        filelist=[]
        with (in_path.open('r') as in_file):
            for line in in_file:
                line_s = line.strip().replace(" ", "")
                if line_s:
                    filelist.append(line_s)
            stat_msg = list()
            for f_name in filelist:
                f_path = Path(f_name)
                if f_path.is_file():
                    #read the points from file
                    coordinate = readPoints(f_path)
                    #print analysis message if applicable
                    if analysis:
                        print("input list is:")
                        if len(coordinate)>10:
                            print(coordinate[:10])
                            print("only 1st 10 points are printed")
                        else:
                            print(coordinate)
                        print(f'Total number of points: {len(coordinate)}')
                        print("Start manhattan calculation.")
                    #start calculation and time the process
                    part1_time = 0
                    part2_time = 0
                    for i in range(args.repeat):
                        start_time = time_ns()
                        result, mid_time = AcceleratedManhattan(coordinate,int(args.m),(analysis if i==0 else False))
                        end_time = time_ns()
                        part1_time += mid_time - start_time
                        part2_time += end_time - mid_time
                    part1_time = part1_time//args.repeat
                    part2_time = part2_time//args.repeat
                    t_time = part1_time+part2_time
                    #print analysis message if applicable
                    if analysis:
                        print(f'manhattan algorithm for the input list executed for {args.repeat} time.')
                        print(f'average execution time ={"%.2f" % t_time}ns')
                        print(f'Result of closet {args.m} pairs: ')
                        if len(result)>10:
                            for i in range(10):
                                print(f'{result[i][0]} , {result[i][1]}')
                            print("only 1st 10 pairs are printed")
                        else:
                            for x in result:
                                print(f'{x[0]} , {x[1]}')
                        stat_msg.append([f_name,len(coordinate),args.m,"%.2f" % part1_time,"%.2f" % part2_time])
                        print()
                    #write the result list to file
                    if args.o:
                        childname = "output_"+str(f_path.absolute())[len(str(f_path.absolute().parent))+1:]
                        out_pathreal=f_path.absolute().parent.joinpath(childname)
                        #out_pathreal = Path(str(f_path.absolute().parent)+"\\" + "output_" + childname)
                        writeResults(out_pathreal,result)
                else:
                    print(f'{f_path.absolute()} in file list supplied do not exist')
            print("statistics:")
            print("file, data size, m size, part1 processing time(ns), part2 processing time(ns)")
            for x in stat_msg:
                print(x)
            print()
else:
    raise Exception(f'input file in {in_path.absolute()} do not exist')