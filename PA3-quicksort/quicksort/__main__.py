#Shun Fai Lee Lab4
from pathlib import Path
import argparse
from time import time_ns

from sorter.sorterhelper import sortthisway
from sorter.sorterhelper import printout

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='use quicksort of different preference to sort numbers')
this_parser.add_argument('-l', action='store_true', help="Optional, for input file is a list of local files")
this_parser.add_argument('n_file', type=str, help="Input File Pathname containing the numbers to be sorted")
this_parser.add_argument('-t', type=str, choices=["q1","q10","q50","q100","mo3","mg","nmgl"], default="mo3", required=False, action='store', help="Optional choose of sorting strategy, default=mo3")
this_parser.add_argument('-a', action='store_true', help="Optional, include the analysis details in output")
args = this_parser.parse_args()

# Set the input and output file path
in_path = Path(args.n_file)

if in_path.is_file():
    #proceed the frequency table file if it exists, build and print to file
    with (in_path.open('r') as in_file):
        compare = 0
        exchange = 0
        if not args.l:
            filename = str(in_path.name)
            out_path = str(in_path.absolute())
            out_pathdir = out_path[:len(out_path) - len(filename)]
            out_pathreal = Path(out_pathdir + "output_"+ args.t + "_" + filename)
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