from pathlib import Path
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

# Testing
if __name__ == "__main__":
    inpath = Path('datafile\DTMtable.csv')
    temp = readDTM(inpath)
    print(temp['q0']['1'][1])