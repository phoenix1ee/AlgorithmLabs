from sys import setrecursionlimit
setrecursionlimit(30000)

from pathlib import Path
from DTMsimulator.tape import tape
from DTMsimulator.readDTM import readDTM

def DTMsimulate(DTM,in_tape:tape):
    currentstate="q0"
    round = 0
    tapestate = list()
    while currentstate not in ("qY","qN"):
        #read tape
        currentsymbol = in_tape.now.v
        #write to tape
        in_tape.write(DTM[currentstate][currentsymbol][1])
        #print current tape state
        tapestate.append("transition "+str(round)+": tape: "+in_tape.print())
        if round <31:
            print(f"transition {round}: tape: {in_tape.print()}")
        round+=1
        #move and update state
        in_tape.move(int(DTM[currentstate][currentsymbol][2]))
        currentstate = DTM[currentstate][currentsymbol][0]
    if round >30:
        print(f"...skip...\nonly the 1st 30 transition are printed")
    print(f"final tape: {in_tape.print()}")
    if currentstate == "qY":
        return True , tapestate
    else:
        return False,tapestate

def printDTM(DTM):
    print("DTM is defined as follows:")
    Q = list(DTM)
    Gamma = list(DTM[Q[0]].keys())
    s = list({DTM[x][y][2] for x in Q for y in Gamma})
    Sigma = [x for x in Gamma if x !='b']
    b = ["b"]
    print(f'6-tuple M = \n Gamma: {Gamma} \n Q: {Q} \n s: {s}')
    # print transition table with alignment
    print(f" transition table:")
    transition = list()
    transition.append([" "]+Gamma)
    for q in Q:
        transition.append([q]+list(DTM[q][y] for y in Gamma))
    # transform row and columns of 2-D list
    transitioncols = list(zip(*transition))
    # find max length of each row elements
    widths = [max(len(str(item)) for item in col) for col in transitioncols]
    for row in transition:
        print(" ","  ".join(f"{str(item):<{widths[i]}}" for i, item in enumerate(row)))
    print(f' Sigma: {Sigma} \n b: {b}')

# Testing
if __name__ == "__main__":
    # Set the input file path
    in_path = Path('datafile\DTMtable2.csv')
    if in_path.is_file():
        print(f'read DTM specification from {in_path}')
        DTM = readDTM(in_path)
        printDTM(DTM)
        teststring="111000"
        print(f'test string is {teststring}')
        testtape = tape(teststring)
        print(DTMsimulate(DTM,testtape))
    else:
        raise Exception(f'input file in {in_path.absolute()} do not exist')