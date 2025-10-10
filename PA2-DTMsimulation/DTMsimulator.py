from sys import setrecursionlimit
setrecursionlimit(30000)

from pathlib import Path
import argparse
import csv

def readDTM(in_path):
    """
    read input file containing DTM table 
    example header:state,symbol,nstate,nsymbol,move
    example line:q0,0,q0,0,1
    convert and output a dict input data
    :param in_path :a file object which contain DTM table
    :return: the dict of input data
    """
    DTM = dict()
    with open(in_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')  # Change delimiter if needed
        #print(reader.fieldnames)
        #x=1
        for row in reader:
            if row['state'] in DTM:
                # add the transition content to DTM dict
                #print(f'row {x}  {row['nstate']},{row['nsymbol']},{row['move']}')
                DTM[row['state']].update({row['symbol']:(row['nstate'],row['nsymbol'],row['move'])})
                #print(DTM[row['state']])
            else:
                # update the key for state 1st
                #print(f'row {x}  {row['nstate']},{row['nsymbol']},{row['move']}')
                DTM.update({row['state']:{row['symbol']:(row['nstate'],row['nsymbol'],row['move'])}})
                #print(DTM[row['state']])
            #x+=1
    return DTM

def replace(in_str,index,char):
    return in_str[:index]+char+in_str[index+1:]

def DTMsimulate(DTM,in_str)->bool:
    tape = in_str[:]
    currentstate="q0"
    currentindex = 0
    round = 1
    while currentstate not in ("qY","qN"):
        currentsymbol = tape[currentindex]
        tape = replace(tape, currentindex, DTM[currentstate][currentsymbol][1])
        currentindex = currentindex + int(DTM[currentstate][currentsymbol][2])
        currentstate = DTM[currentstate][currentsymbol][0]
        print(f"round{round}: tape: {tape}, next tape position: {currentindex+1}")
        round+=1
    return True if currentstate == "qY" else False


# Testing
if __name__ == "__main__":
    # use the Argument parser to define compulsory and optional arguments
    this_parser = argparse.ArgumentParser(description ='calculate manhattan distance and return closet m pairs')
    this_parser.add_argument('n_file', type=str, help="Input File containing the coordinates")
    this_parser.add_argument('-o', action='store_true', help="Optional, print the manhattan result list to file")

    args = this_parser.parse_args()

    # Set the input file path
    in_path = Path(args.n_file)

    if in_path.is_file():
        DTM = readDTM(in_path)
    else:
        raise Exception(f'input file in {in_path.absolute()} do not exist')
    test = "000b"
    print(DTMsimulate(DTM,test))
    print(test)