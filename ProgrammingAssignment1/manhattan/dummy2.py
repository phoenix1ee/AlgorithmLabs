#from manhattan.merge_sort import merge_sort
import math
from pathlib import Path
from time import time_ns
from merge_sort import merge_sort
from readPoints import readPoints

def Manhattan(P:list,m:int,analysis=False):
    """Calculate the manhattan distance of points in the input list P
    and output a list containing the closet m pairs of points.

	Arguments:
	P -- a list/array containing the points
	m -- no. of closet points needed
    analysis -- boolena to toggle printing of analysis message
	"""
    #find the length of input array
    n = len(P)
    #calculate no. of combinations or pairs
    combination = math.comb(n,2)
    #declare empty array
    Distance = list()
    for i in range(math.floor(math.log2(2000))+1):
        Distance.append(list())
    #initialize counter and keys
    counter = 0
    key = 0
    #calculate manhattan distance for each pairs of coordinates
    while key < n-1:
        for i in range(key+1, n):
            temp = abs(P[key][0]-P[i][0])+abs(P[key][1]-P[i][1])
            Distance[math.floor(math.log2(temp))].append([P[key],P[i],temp])
            counter+=1
            i+=1
        key+=1
    #print intermediate result if applicable
    #This is not part of the algorithm, exist for analysis and trace purpose only
    #called when passed with "True" for "analysis"
    mid_time = time_ns()
    if analysis:
        print(f"pairs of coordinates and manhattan distance: ")
        if counter>10:
            needed = 10
            i=0
            while needed>0:
                for j in range(min(needed, len(Distance[i]))):
                    print(f'{Distance[i][j][0]} , {Distance[i][j][1]} , {Distance[i][j][2]}')
                    needed-=1
                i+=1
            print("only 1st 10 pairs and manhattan distance are printed")
        else:
            for x in Distance:
                for y in x:
                    print(f'{y[0]} , {y[1]} , {y[2]}')
    #call CLRS page 39 merge-sort, modified for the data structure
    Result=list()
    PartitionID = 0
    needed = m
    while needed>0:
        merge_sort(Distance[PartitionID],0)
        #extract the 1st m nos. of pairs and return
        for j in range(min(needed, len(Distance[PartitionID]))):
            Result.append(Distance[PartitionID][j][:2])
            needed-=1
        PartitionID+=1
    return Result


# Testing
if __name__ == "__main__":
    test1=[[1,2],[1,3],[3,1],[4,4]]
    test2=[[1,1],[1,2],[2,1],[2,2],[9,9],[9,10],[10,9],[10,10]]
    infile = Path('datafile/rand6400.txt')
    coo=readPoints(infile)
    result = Manhattan(coo,100,True)
    print(result)
