# Turing Machine Simulation

This python package is developed on and expected to be run in CLI with python interpreter 3.12 or above.

It accepted user input of a Deterministic Turing Machine defined in the form of a transition table and a input string
and output the result to terminal and or file. 

## How to download and run:

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m DTMsimulator -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m DTMsimulator <input_file> <inputstring>`

   a. IE: `python -m DTMsimulator file/DTMaddition.csv 110add11`

In the above example, tape status will be printed on Shell and if there are more than 30 transition, all transitions will be output to an output.txt file at directory `file/`.

### Instruction to Run:

```commandline
usage: __main__.py [-h] n_file inputstring

Simulate a DTM with input: csv file represeting DTM and test string

positional arguments:
  n_file       Input File containing the DTM description
  inputstring  The input string

options:
  -h, --help   show this help message and exit

```

## File list

This project have a single module in a single package.
Here is huffman package explained.

* [PA2-DTMsimulation/](.): The parent package folder.
    * [README.md](README):
      The guide for using this DTMsimulator module
    * [DTMsimulator](DTMsimulator): 
      This is the *module* in this *package*.
      * [`__init__.py`](DTMsimulator/__init__.py)
      * [`__main__.py`](DTMsimulator/__main__.py) 
        This file is the entrypoint to the DTMsimulator module when ran as a program. It handles the command line arguments and do all functions calling and output.
      * `DTMsimulate.py` 
        This is the core algorithm for the DTM operations.
      * `readDTM.py` 
        This is the method to read input DTM definition file.
      * `tape.py` 
        This is the class to simulate a tape.

## Included DTM
This project include the following DTM definition files:
1. DTMexample.csv
2. Binaryaddition.csv
3. BinarySub.csv
4. BinaryMul.csv