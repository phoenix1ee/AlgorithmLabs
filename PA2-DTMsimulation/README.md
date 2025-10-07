# Shun Fai Lee Programming Assignment 2

This python package is developed on and expected to be run in CLI with python interpreter 3.12 or above.

It accepted user input in the form of a text file containing lines of coordinates, or a file containing a list of full file path
and output statistics to console and/or outputing result list, to the same directory as the input file, by passing optional arguments. Statistics information includes file names, data size, m size, processing time(ns). The module also support to repeat for multiple times optionally for better accuracy of statistics, with the appropriate argument passed. 

## How to download and run:

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m manhattan -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m manhattan <input_file> <m>`

   a. IE: `python -m manhattan file/coordinates.txt 30 -o`

In the above example, output of the calculated and desired result will be written to a file named output_coordinates.txt at directory `file/`.

### Instruction to Run:

```commandline
usage: __main__.py [-h] [-l] [-o] [-a] [-r [REPEAT]] n_file m

calculate manhattan distance and return closet m pairs

positional arguments:
  n_file                Input File containing the coordinates
  m                     No. of closet pairs needed

options:
  -h, --help            show this help message and exit
  -l                    Optional, to support batch input by inputing a file containing list of local files
  -o                    Optional, print the manhattan result list to file
  -a                    Optional, print to include the analysis details in output
  -r, --repeat          Optional, repeat manhattan process for certain times for accurate analysis

```

Usage statements:

| Symbol | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [h]    | variable h is optional. It display the helper message                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [l]    | variable l is optional. It will tell program that input file is a list of files                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [m]    | variable m is compulsory. It is the number of pairs of coordinates you want.                                                                                                                                                                                                                                                                                                                                                                              |
| [a]    | variable a is optional. It will ask the program to print out input, output and intermediate statistics of the algorithm for user's reference                                                                                                                                                                                                                                                                                                                                                                                                     |
| [o]    | variable o is optional. It will ask the program to write the result list of closet pairs to output file  |
                                                
## File list

This project have a single module in a single package.
Here is huffman package explained.

* [ProgrammingAssignment1/](.): The parent package folder.
    * [README.md](README):
      The guide for using this manhattan distance module
    * [manhattan](manhattan): 
      This is the *module* in this *package*.
      * [`__init__.py`](ProgrammingAssignment1/__init__.py) xxx
      * [`__main__.py`](ProgrammingAssignment1/__main__.py) 
        This file is the entrypoint to the manhattan module when ran as a program. It handles the command line arguments and do all functions calling and output.
      * `manhattan.py` 
        This is the core algorithm for the manhattan distance operations.
      * `readPoints.py` 
        This is the method to read input file.
      * `merge_sort.py` 
        This is the CLRS page 39 merge-sort.
      * `writeResults.py` 
        This is the method to write calculated manhattan distance results to output file.
      * `manhattan_improvement.py` 
        This is the improved core algorithm for the manhattan distance operations. It is not included in the main program but is for standalone execution for testing purpose.

## Example input and output

>An example of manhattan printout, with the -a paramenter
> 
>python3 -m manhattan data.txt 3 -a
>
>From Input file : `line1:1,2 , line2: 3,1 , line3: 3,1 , line4: 4,4`
> 
>In Output console:
> 
> `input list is:`
>
> `[[1, 2], [1, 3], [3, 1], [4, 4]]`
>
> `Total number of points: 4`
>
> `Start manhattan calculation.`
>
> `pairs of coordinates and manhattan distance: `
>
> `[1, 2] , [1, 3] , 1`
>
> `[1, 2] , [3, 1] , 3`
>
> `[1, 2] , [4, 4] , 5`
>
> `[1, 3] , [3, 1] , 4`
>
> `[1, 3] , [4, 4] , 4`
>
> `[3, 1] , [4, 4] , 4`
>
> `manhattan algorithm for the input list executed for 1 time.`
>
> `average execution time =58777.00ns`
>
> `Result of closet 3 pairs: `
>
> `[1, 2] , [1, 3]`
>
> `[1, 2] , [3, 1]`
>
> `[1, 3] , [3, 1]`
>
> `statistics:`
>
> `file, data size, m size, part1 processing time(ns), part2 processing time(ns)`
>
> `data.txt,4,3,12216.00,46561.00`