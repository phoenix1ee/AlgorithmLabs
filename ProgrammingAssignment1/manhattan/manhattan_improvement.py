from merge_sort import merge_sort
import math
from pathlib import Path
from time import time_ns
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
            for partition in Distance:
                for pair in partition:
                    print(f'{pair[0]} , {pair[1]} , {pair[2]}')
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
    return Result,mid_time


# Testing
if __name__ == "__main__":
    infile = Path('datafile/rand6400.txt')
    coordinates=readPoints(infile)
    m = 8000
    start_time = time_ns()
    result,mid_time = Manhattan(coordinates,m,True)
    end_time = time_ns()
    part1_time = mid_time - start_time
    part2_time = end_time - mid_time
    print("statistics:")
    print("file, data size, m size, part1 processing time(ns), part2 processing time(ns)")
    print(infile, len(coordinates), m, "%.2f" % part1_time, "%.2f" % part2_time, sep=",")
