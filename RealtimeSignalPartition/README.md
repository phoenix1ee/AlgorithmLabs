# Shun Fai Lee Programming Assignment 4

This python package is developed on and expected to be run in CLI with python interpreter 3.12 or above.

This is a real time partition algorithm for partitioning two interweaving signals from 1 signal stream and identified the noise, and correct assignment of bits to two distinct signals. It is a linear time algorithm, which is real time and simple.
It accepted user input in the form of a text file containing lines of values. Each line is one set of problem.
and output processing statistics to console, print the assignment if needed, by passing optional arguments. Statistics information includes input identifier, data size, number of push operations and number of pop operations.  

## How to download and run:

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m signalpartition -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m signalpartition <input_file> -a`

   a. IE: `python -m signalpartition file/data.txt -a`

In the above example, the input file will be read and the module will output analysis statistics to shell, with the assignment of bits.

### Instruction to Run:

```commandline
usage: __main__.py [-h] [-a] n_file

real time signal partitioning

positional arguments:
  n_file      Input data

options:
  -h, --help  show this help message and exit
  -a          Optional, print to include the analysis details in output
```

Usage statements:

| Symbol | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [h]    | variable h is optional. It display the helper message                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [a]    | variable a is optional. It will ask the program to print out the complete assigment of signal index for user's reference.                                                                                                                                                                                                                                                                                                                                                                                                     |
                                                
## File list

This project have a single module in a single package.
Here is huffman package explained.

* [RealtimeSignalPartition/](.): The parent package folder.
    * [README.md](README):
      The guide for using this signalpartition module
    * [signalpartition](signalpartition): 
      This is the *module* in this *package*.
      * [`__init__.py`](signalpartition/__init__.py)
      * [`__main__.py`](signalpartition/__main__.py) 
        This file is the entrypoint to the PA4-signalpartition module when ran as a program. It handles the command line arguments and do all functions calling and output.
      * `signalpartition.py` 
        This is the core algorithm for the signal partitioning operations.
      * `generate.py` 
        This includes a generator of example test cases.

## Example input and output

>An example of signalpartition printout, with the -a paramenter
> 
>python3 -m signalpartition data.txt -a
>
>From Input file : `BB15,010100111001001,101,010`
> 
>In Output console:
>

> `test case identifier:BB15`

> `signal stream:`

> `010100111001001`

> `x: 101`

> `y: 010`

> `index of signal x: [[4, 5, 7], [9, 11, 12]]`

> `index of signal y: [[1, 2, 3], [6, 8, 10]]`

> `index of noise: [[], [13, 14, 15]]`

> `the test case BB15 is an interweaving of ship x and y signals`

> `statistics:`

> `case identifier, data size, number of push, number of pop`

> `BB15,15,32,28`
