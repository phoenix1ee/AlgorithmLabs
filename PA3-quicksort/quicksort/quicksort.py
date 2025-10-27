#Shun Fai Lee 621.83 Programming Assignment3

#partition with reference to CLRS P184
def partition(A: list, p, r, performance: list=None):
    """
    the partition function that return a pivot for use by quicksort function
    :param A: the list to be sorted
    :param p: the starting index of partitioning
    :param r: the end index of partitioning
    :param performance: the array[comparison, exchange, [analysis message]] to store key metrics including no. of comparisons and exchanges
    :return: the index of pivot, analysis data including no. of comparisons and exchanges are made in place in Array performance

    A[r] is chosen as the pivot.

    """
    #A[r] is chosen as the pivot.
    x = A[r]  # select the last element as the pivot

    i = p - 1  # highest index into the low side
    for j in range(p, r):  # process each element other than the pivot
        # add 1 comparison
        performance[0]+=1
        if A[j] <= x:  # does this element belong on the low side?
            i += 1  # index of a new slot in the low side
            A[i], A[j] = A[j], A[i]  # put this element there
            #add 1 exchange
            performance[1]+=1

    A[i + 1], A[r] = A[r], A[i + 1]  # the pivot does just to the right of the low side
    #add 1 exchange
    performance[1]+=1
    return i + 1  # return the new index of the pivot


#modified partition that use median-of-three partitioning
def partitionMO3(A: list, p, r, performance: list=None):
    """
    the partition function that return a pivot for use by quicksort function
    :param A: the list to be sorted
    :param p: the starting index of partitioning
    :param r: the end index of partitioning
    :param performance: the array[comparison, exchange, [analysis message]] to store key metrics including no. of comparisons and exchanges
    :return: the index of pivot, analysis data including no. of comparisons and exchanges are made in place in Array performance

    """
    #calculate the median index
    m = (p+r)//2
    #use a simple insertion sort like logic
    if A[p]>A[r]:
        #exchange A[p] and A[r]
        A[p], A[r] = A[r], A[p]
        #add 1 comparison and exchange
        performance[0]+=1
        performance[1]+=1
    if A[p]>A[m]:
        #exchange A[p] and A[m]
        A[p], A[m] = A[m], A[p]
        #add 1 comparison and exchange
        performance[0]+=1
        performance[1]+=1
    if A[r]>A[m]:
        #exchange A[r] and A[m]
        A[r], A[m] = A[m], A[r]
        #add 1 comparison and exchange
        performance[0]+=1
        performance[1]+=1

    x = A[r]  # select the last element as the pivot

    i = p - 1  # highest index into the low side
    for j in range(p, r):  # process each element other than the pivot
        # add 1 comparison
        performance[0]+=1
        if A[j] <= x:  # does this element belong on the low side?
            i += 1  # index of a new slot in the low side
            A[i], A[j] = A[j], A[i]  # put this element there
            #add 1 exchange
            performance[1]+=1
            
    A[i + 1], A[r] = A[r], A[i + 1]  # the pivot does just to the right of the low side
    #add 1 exchange
    performance[1]+=1
    return i + 1  # return the new index of the pivot

#quicksort with reference to CLRS P184
def quicksort(A, p=0, r=None, performance:list=None, analyze = False):
    """
    sort the input list with quicksort using last element as pivot
    :param A: the list to be sorted
    :param p: the starting index of sorting
    :param r: the end index of sorting
    :param performance: the array[comparison, exchange, [analysis message]] to store key metrics including no. of comparisons and exchanges
    :return: None, analysis data including no. of comparisons and exchanges are made in place in Array performance
    """
    if r is None:
        r = len(A) - 1
    if p < r:
        # using original partition scheme
        q = partition(A, p, r,performance)
        if analyze:
            performance[2].append(f"list after partition run between index {p} and {r}")
            performance[2].append([x for x in A])
            performance[2].append(f"Pivot now at {q}")
        quicksort(A, p, q-1,performance)  # recursively sort the low side
        quicksort(A, q+1, r,performance)  # recursively sort the high side

#quicksort with reference to CLRS P184, using median-of-three partition
def quicksortMO3(A, p=0, r=None, performance:list=None,analyze = False):
    """
    sort the input list with quicksort using last element as pivot
    :param A: the list to be sorted
    :param p: the starting index of sorting
    :param r: the end index of sorting
    :param performance: the array[comparison, exchange, [analysis message]] to store key metrics including no. of comparisons and exchanges
    :return: None, analysis data including no. of comparisons and exchanges are made in place in Array performance
    """
    if r is None:
        r = len(A) - 1
    if p < r:
        # using original partition scheme
        q = partitionMO3(A, p, r,performance)
        if analyze:
            performance[2].append(f"list after partition run between index {p} and {r}")
            performance[2].append([x for x in A])
            performance[2].append(f"Pivot now at {q}")
        quicksortMO3(A, p, q-1,performance)  # recursively sort the low side
        quicksortMO3(A, q+1, r,performance)  # recursively sort the high side


# Testing
if __name__ == "__main__":
    test = [5,4,3,2,1]
    test2 = test[:]
    temp = [0,0]
    i=0
    print(f"test input={test}")
    print(f"testing partition scheme: partition")
    print(f"pivot={partition(test,0,len(test)-1,temp)}")
    print(f"input after partition: {test}")
    print(f"no. of comparison:{temp[0]}, no. of exchange:{temp[1]}")
    temp2 = [0,0]
    print(f"testing partition scheme: partitionMO3")
    print(f"pivot={partitionMO3(test2,0,len(test2)-1,temp2)}")
    print(f"input after partition: {test2}")
    print(f"no. of comparison:{temp2[0]}, no. of exchange:{temp2[1]}")
    