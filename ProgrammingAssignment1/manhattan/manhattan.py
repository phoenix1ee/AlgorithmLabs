#from manhattan.merge_sort import merge_sort
import math
from manhattan.merge_sort import merge_sort

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
    #initialize counter and keys
    counter = 0
    key = 0
    #calculate manhattan distance for each pairs of coordinates
    while key < n-1:
        for i in range(key+1, n):
            temp = abs(P[key][0]-P[i][0])+abs(P[key][1]-P[i][1])
            Distance.append([P[key],P[i],temp])
            counter+=1
            i+=1
        key+=1
    #print intermediate result if applicable
    #This is not part of the algorithm, exist for analysis and trace purpose only
    #called when passed with "True" for "analysis"
    if analysis:
        print(f"pairs of coordinates and manhattan distance: ")
        if len(Distance)>10:
            for i in range(10):
                print(f'{Distance[i][0]} , {Distance[i][1]} , {Distance[i][2]}')
            print("only 1st 10 pairs and manhattan distance are printed")
        else:
            for x in Distance:
                print(f'{x[0]} , {x[1]} , {x[2]}')
    #call CLRS page 39 merge-sort, modified for the data structure
    merge_sort(Distance,0)
    #extract the 1st m nos. of pairs and return
    Result = [item[:2] for item in Distance[:m]]
    return Result


# Testing
if __name__ == "__main__":
    test1=[[1,2],[1,3],[3,1],[4,4]]
    print(Manhattan(test1,4))