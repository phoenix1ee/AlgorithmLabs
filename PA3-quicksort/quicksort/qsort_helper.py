#Shun Fai Lee Lab4
def median(a,b,c):
    """
    find the median of three values
    :param a: the 1st object
    :param b: the 2nd object
    :param c: the 3rd object
    :return: the median of 3
    """
    temp = [a]
    if b>a:
        temp.append(b)
    else:
        temp.insert(0,b)
    if c > a and c > b :
        return temp[1]
    elif c < a and c < b :
        return temp[0]
    else:
        return c

def priority(a, b, mode = "d") -> bool:
    """
    determine if the 1st object has higher priority then 2nd object, leave flexibility to accommodation multiple modes
    equal will priority to "a"
    default: mode = "d" check priority according to default mode
    alternative: mode = "leave blank for future"
    :param a: the 1st object
    :param b: the 2nd object
    :param mode: the logic for determining priority
    :return: boolean value, True if 1st object has priority > 2nd object, otherwise false
    """
    if mode == "d":
        if a < b :
            return True
        else:
            return False

def partitiion(ndlist: list, lowid, hid, mode = "1st"):
    """
    the partition function for use by quicksort function, contain two modes
    :param ndlist: the list to be sorted
    :param lowid: the starting index of partitioning
    :param hid: the end index of partitioning
    :param mode: the parameter to toggle different pivot choose, "1st" for choosing the first item, "mo3" for choosing median of 3
    :return: the list, no. of comparisons and exchange make
    """
    cpnos = 0
    exnos = 0
    if mode == "mo3":
        pivot = median(ndlist[lowid], ndlist[lowid + (hid - lowid)//2], ndlist[hid])
    else:
        pivot = ndlist[lowid]
    finish  = False
    while not finish:
        while priority(ndlist[lowid],pivot):
            lowid+=1
            cpnos += 1
        cpnos += 1
        while priority(pivot,ndlist[hid]):
            hid -= 1
            cpnos += 1
        cpnos += 1
        if lowid >= hid:
            finish = True
        else:
            temp = ndlist[lowid]
            ndlist[lowid] = ndlist[hid]
            ndlist[hid] = temp
            lowid +=1
            hid-=1
            exnos += 1
    return hid, cpnos, exnos