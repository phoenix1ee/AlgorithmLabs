#Shun Fai Lee 621.83 Programming Assignment3

from sys import setrecursionlimit
setrecursionlimit(1000000)

from pathlib import Path
import argparse
from quicksort.helper import numreader, writeResults
from quicksort.quicksort import quicksort, quicksortMO3

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='use quicksort of different preference to sort numbers')
this_parser.add_argument('-l', action='store_true', help="Optional, for input file is a list of local files")
this_parser.add_argument('n_file', type=str, help="Input data")
this_parser.add_argument('-t', type=str, choices=["q","mo3"], default="q", required=False, action='store', help="Optional choose of sorting strategy, default=original quicksort")
this_parser.add_argument('-o', action='store_true', help="Optional, print the sorted result list to file")
this_parser.add_argument('-a', action='store_true', help="Optional, print to include the analysis details in output")

args = this_parser.parse_args()

# Set the input file path
in_path = Path(args.n_file)

# name for two different quicksort
qsorttype = {"q":"QUICKSORT","mo3":"QUICKSORT-median-of-three partition"}

# set trace output switch
analysis = False
if args.a:
    analysis = not analysis

if in_path.is_file():
    #start if input file exists
    if not args.l:
        #create a storage for performance data
        #performance[number of comparison,number of exchange, [analysis message]]
        performance = [0,0,[]]
        #read the input from file
        data = numreader(in_path)
        #print analysis message if applicable
        if analysis:
            print("input list is:")
            if len(data)>10:
                print(data[:10], end="")
                print("...", end="")
                print("only 1st 10 data are printed")
            else:
                print(data)
            print(f'Total number of data: {len(data)}')
            print(f"Start sorting with {qsorttype[args.t]}.")
        #start sorting with the chosen QUICKSORT or quicksortMO3
        if args.t == "q":
            quicksort(data,0,len(data)-1,performance,True if len(data)<11 else False)
        else:
            quicksortMO3(data,0,len(data)-1,performance,True if len(data)<11 else False)
        #print analysis message if applicable
        if analysis:

            #print status of list on different pass
            if len(performance[2])>0:
                for x in performance[2]:
                    print(x)
            
            print(f'data Sorted: ')
            if len(data)>10:
                for i in range(10):
                    print(f'{data[i]}',end="")
                    if i != 9:
                        print(f',',end="")
                print("...only 1st 10 data are printed")
            else:
                print(f"{data}")
            print("statistics:")
            print("file, data size, sorting, number of comparison, number of exchange")
            print(args.n_file, len(data), qsorttype[args.t], performance[0], performance[1], sep=",")
        #write the sorted list to file if applicable
        if args.o:
            filename = str(in_path.name)
            out_path = str(in_path.absolute())
            out_pathdir = out_path[:len(out_path) - len(filename)]
            out_pathreal = Path(out_pathdir + "output_" + filename)
            writeResults(out_pathreal,data)
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
                    #create a storage for performance data
                    #performance[number of comparison,number of exchange, [analysis message]]
                    performance = [0,0,[]]
                    #read the input from file
                    data = numreader(f_path)
                    #print analysis message if applicable
                    if analysis:
                        print(f"input list from {f_path.name} is:")
                        if len(data)>10:
                            print(data[:10], end="")
                            print("...", end="")
                        else:
                            print(data)
                        print(f'Total number of data: {len(data)}')
                        print(f"Start sorting with {qsorttype[args.t]}.")
                    #start sorting with the chosen QUICKSORT
                    if args.t == "q":
                        quicksort(data,0,len(data)-1,performance)
                    else:
                        quicksortMO3(data,0,len(data)-1,performance)
                    #print analysis message if applicable
                    if analysis:
                        print(f'data Sorted: ')
                        if len(data)>10:
                            for i in range(10):
                                print(f'{data[i]}',end="")
                                if i != 9:
                                    print(f',',end="")
                            print("...only 1st 10 data are printed")
                        else:
                            print(f"{data}")
                        stat_msg.append([f_path.name, len(data), qsorttype[args.t], performance[0], performance[1]])
                        print()
                    #write the sorted list to file if applicable
                    if args.o:
                        childname = "output_"+str(f_path.absolute())[len(str(f_path.absolute().parent))+1:]
                        out_pathreal=f_path.absolute().parent.joinpath(childname)
                        writeResults(out_pathreal,data)
                else:
                    print(f'{f_path.absolute()} in file list supplied do not exist')
            print("statistics:")
            print("file, data size, sorting, number of comparison, number of exchange")
            for x in stat_msg:
                print(x)
            print()
else:
    raise Exception(f'input file in {in_path.absolute()} do not exist')