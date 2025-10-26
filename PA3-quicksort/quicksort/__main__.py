#Shun Fai Lee 621.83 Programming Assignment3

from sys import setrecursionlimit
setrecursionlimit(30000)

from pathlib import Path
import argparse
from quicksort.helper import numreader, printout
from quicksort.quicksort import quicksort, quicksortMO3

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='use quicksort of different preference to sort numbers')
this_parser.add_argument('-l', action='store_true', help="Optional, for input file is a list of local files")
this_parser.add_argument('n_file', type=str, help="Input data")
this_parser.add_argument('-t', type=str, choices=["q","mo3"], default="q", required=False, action='store', help="Optional choose of sorting strategy, default=mo3")
this_parser.add_argument('-o', action='store_true', help="Optional, print the manhattan result list to file")
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
    if not args.l:
        #create a storage for performance data
        performance = [0,0]
        #read the input from file
        data = numreader(in_path)
        #print analysis message if applicable
        if analysis:
            print("input list is:")
            if len(data)>10:
                print(data[:10])
                print("only 1st 10 points are printed")
            else:
                print(data)
            print(f'Total number of points: {len(data)}')
            print("Start manhattan calculation.")
        #start manhattan distance calculation and record the time consumed
        part1_time = 0
        part2_time = 0
        for i in range(args.repeat):
            start_time = time_ns()
            result, mid_time = Manhattan(data,int(args.m),(analysis if i==0 else False))
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
            print(args.n_file, len(data), args.m, "%.2f" % part1_time, "%.2f" % part2_time, sep=",")
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
                    data = readPoints(f_path)
                    #print analysis message if applicable
                    if analysis:
                        print("input list is:")
                        if len(data)>10:
                            print(data[:10])
                            print("only 1st 10 points are printed")
                        else:
                            print(data)
                        print(f'Total number of points: {len(data)}')
                        print("Start manhattan calculation.")
                    #start calculation and time the process
                    part1_time = 0
                    part2_time = 0
                    for i in range(args.repeat):
                        start_time = time_ns()
                        result, mid_time = Manhattan(data,int(args.m),(analysis if i==0 else False))
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
                        stat_msg.append([f_name,len(data),args.m,"%.2f" % part1_time,"%.2f" % part2_time])
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