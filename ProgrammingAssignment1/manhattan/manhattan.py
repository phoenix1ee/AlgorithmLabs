#from manhattan.merge_sort import merge_sort
import math
from manhattan.merge_sort import merge_sort

def Manhattan(P:list,m:int):
    """Calculate the manhattan distance of points in the input list P
    and output a list containing the closet m pairs of points.

	Arguments:
	P -- a list/array containing the points
	m -- no. of closet points needed
	"""
    n = len(P)
    combination = math.comb(n,2)
    Distance = list()
    counter = 0
    key = 0
    while key < n-1:
        for i in range(key+1, n):
            temp = abs(P[key][0]-P[i][0])+abs(P[key][1]-P[i][1])
            Distance.append([P[key],P[i],temp])
            counter+=1
            i+=1
        key+=1
    merge_sort(Distance,0)
    Result = [item[:2] for item in Distance[:m]]
    return Result


# Testing
if __name__ == "__main__":
    test1=[[1,2],[1,3],[3,1],[4,4]]
    print(Manhattan(test1,4))