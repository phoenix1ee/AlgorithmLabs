# Shun Fai Lee Programming Assignment 3

This python package is developed on and expected to be run in CLI with python interpreter 3.12 or above.

It accepted user input in the form of a text file containing lines of values, or a file containing a list of full file path
and output statistics to console and outputing sorted list if needed, to the same directory as the module, by passing optional arguments. Statistics information includes file names, data size, sorting type, number of comparison, number of exchange.  

## How to download and run:

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m quicksort -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m quicksort -t mo3 <input_file> -a`

   a. IE: `python -m quicksort -t mo3 file/data.txt -a`

In the above example, the input file will be read and the module will output analysis statistics to shell, but not outputing the sorted file.

### Instruction to Run:

```commandline
usage: __main__.py [-h] [-l] [-t {q,mo3}] [-o] [-a] n_file

use quicksort of different preference to sort numbers

positional arguments:
  n_file      Input data

options:
  -h, --help  show this help message and exit
  -l          Optional, for input file is a list of local files
  -t {q,mo3}  Optional choose of sorting strategy, default=original quicksort
  -o          Optional, print the sorted result to file
  -a          Optional, print to include the analysis details in output

```

Usage statements:

| Symbol | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [h]    | variable h is optional. It display the helper message                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [l]    | variable l is optional. It will tell program that input file is a list of files                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [t]    | variable t is optional. It is the type of quicksort to be used. want.                                                                                                                                                                                                                                                                                                                                                                              |
| [a]    | variable a is optional. It will ask the program to print out input, output and intermediate statistics of the algorithm for user's reference.                                                                                                                                                                                                                                                                                                                                                                                                     |
| [o]    | variable o is optional. It will ask the program to write the result list to output file  |
                                                
## File list

This project have a single module in a single package.
Here is huffman package explained.

* [PA3-quicksort/](.): The parent package folder.
    * [README.md](README):
      The guide for using this quicksort module
    * [quicksort](quicksort): 
      This is the *module* in this *package*.
      * [`__init__.py`](quicksort/__init__.py)
      * [`__main__.py`](quicksort/__main__.py) 
        This file is the entrypoint to the PA3-quicksort module when ran as a program. It handles the command line arguments and do all functions calling and output.
      * `quicksort.py` 
        This is the core algorithm for the quicksort operations.
      * `helper.py` 
        This includes some helper methods to read input file and write results.

## Example input and output

>An example of quicksort printout, with the -a paramenter
> 
>python3 -m quicksort data.txt -a
>
>From Input file : `4
7
9
3
1
6
8
2
5
0`
> 
>In Output console:
> 
> `input list is:`

> `[4, 7, 9, 3, 1, 6, 8, 2, 5, 0]`

> `Total number of data: 10`

> `Start sorting with QUICKSORT.`

> `list after partition run between index 0 and 9`

> `[0, 7, 9, 3, 1, 6, 8, 2, 5, 4]`

> `Pivot now at 0`

> `data Sorted: `

> `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`

> `statistics:`

> `file, data size, sorting, number of comparison, number of exchange`

> `.\datafile\PA3whiteBox_rand.txt,10,QUICKSORT,29,16`
