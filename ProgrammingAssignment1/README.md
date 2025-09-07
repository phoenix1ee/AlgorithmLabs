# Shun Fai Lee Programming Assignment 1

This python package is developed with Python and to be run with python interpreter 3.13.

It accepted user input in the form of a text file containing numbers, or a file containing a list of files in the same executing directory
and output to the same directory as the input file.

It can also perform optional actions, including printing information of sort type, no. of comparison, no. of exchange, processing time(ns), with the appropriate argument input. 

## How to download and run:

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m sorter -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m sorter <input_file> -`
   a. IE: `python -m sorter file/number.txt`

Output of the sorted numbers, with statistics will be written to an output file with name echoing the input file after processing the input file.

### Intruction to Run:

```commandline
usage: __main__.py [-h] [-l] [-t {q1,q10,q50,q100,mo3,mg,nmgl}] [-a] n_file

use quicksort of different preference to sort numbers

positional arguments:
  n_file                Input File Pathname containing the numbers to be sorted

options:
  -h, --help            show this help message and exit
  -l                    Optional, for input file is a list of local files
  -t {q1,q10,q50,q100,mo3,mg,nmgl}
                        Optional choose of sorting strategy, default=mo3
  -a                    Optional, include the analysis details in output

```

Usage statements:

| Symbol | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [h]    | variable h is optional. It display the helper message                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [l]    | variable l is optional. It will tell program that input file is a list of files to be sorted                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [t]    | variable t is optional. It will allow user to choose the preferred sorting algorithm, default is using quicksort with median of 3 as pivot                                                                                                                                                                                                                                                                                                                                                                              |
| [a]    | variable a is optional. It will ask the program to print out statistics of sorting on terminal for user's reference                                                                                                                                                                                                                                                                                                                                                                                                     |
|        | Available options are:<br/> q1->quicksort with 1st element as pivot<br/>q10->quicksort with 1st element as pivot, switch to insertion sort when partition size is 10 or less<br/>q50->quicksort with 1st element as pivot, switch to insertion sort when partition size is 50 or less<br/>q100->quicksort with 1st element as pivot, switch to insertion sort when partition size is 100 or less<br/>mo3->quicksort using median of 3 as pivot<br/>mg->generic mergesort<br/>nmgl->natural merge sort with linked list  |
| n_file | This is the path for frequency table input txt file. Required Positional argument                                                                                                                                                                                                                                                            
## File list

This project have a single module in a single package.
Here is huffman package explained.

* [PA1/](.): The parent package folder.
    * [README.md](README):
      The guide for using this converter
    * [sorter](sorter): 
      This is the *module* in this *package*.
      * [`__init__.py`](PA1/__init__.py) xxx
      * [`__main__.py`](PA1/__main__.py) 
        This file is the entrypoint to the sorter when ran as a program. It handles the command line arguments and do all functions calling and output.
      * `insertionsort.py` 
        This the function to do an insertion sort on an input array and output it.

## Input and Output format:

For this sorter function to function properly, user must supply a legitimate file path as argument,and by default, without specifying optional [-l] [-t] [-a] arguments.
The file is a txt file containing the numbers to be sorted. The program will output the results to a text file at the same directory as the input file.

User can also [-l] argument to indicated that input file is in fact a lists of files containing numbers to be sorted, the program will then process all files one by one.

Without the [-l] argument, the input file should be itself a txt file containing numbers.

With the [-l] argument, the input file should be itself a list of txt file containing numbers, with each line corresponding to a single file e.g. "set1.txt" .

Each number txt file should be in a line by line format, with each line corresponding to a single number e.g. "9999" .

Any space/ tabs/ character inside the input file or number file will be trimmed. Each empty line will be recorded and printed on output for user reference
There is no limitation on number of files or quantity of numbers to be sorted, but input should contain only numbers.

The module will then print the output statistics or information to an output txt file at the same directory as the input number file.
It will only print sorted numbers to output file if the input number file is with size 50 or less

### Example input and output

>An example of sorter printout, with the default quicksort median of 3 sorting algorithm
> 
>From Input file : `line1:3 , line2: 1, , line3: 2`
> 
>In Output file:
> 
>`From /xxx/number.txt:`
> 
>`The sorted elements are:`
> 
>`1 2 3`
> 
> `Total no. of sorted elements: 3`
> 
> `Total no. of comparison/exchanges make is 6 and 2`

