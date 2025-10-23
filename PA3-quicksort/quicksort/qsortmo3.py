#Shun Fai Lee Lab4
from sorter.qsort_helper import partitiion

def qsortmo3(target: list, low, high):
    """
    sort the input list with quicksort using median of 3 element as pivot
    :param target: the list to be sorted
    :param low: the starting index of sorting
    :param high: the end index of sorting
    :return: the list, no. of comparisons and exchange make
    """
    temp = target
    cpsum = 0
    exsum = 0
    if low >= high:
        return temp, cpsum, exsum
    elif high - low == 1:
        cpsum += 1
        if temp[low] < temp[high]:
            return temp, cpsum, exsum
        else:
            tempn = temp[low]
            temp[low] = temp[high]
            temp[high] = tempn
            exsum+=1
            return temp, cpsum, exsum
    else:
        new, temp_cp, temp_ex = partitiion(target, low, high, "mo3")
        cpsum += temp_cp
        exsum += temp_ex
        temp, temp_cp2, temp_ex2 = qsortmo3(temp, low, new)
        cpsum += temp_cp2
        exsum += temp_ex2
        temp, temp_cp3, temp_ex3 = qsortmo3(target, new + 1, high)
        cpsum += temp_cp3
        exsum += temp_ex3
        return temp, cpsum, exsum