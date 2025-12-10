def totalusercost(allocationlist, costtable):
    sum = 0
    if len(allocationlist) == len(costtable[0]):
        for i in range(len(allocationlist)):
            sum += costtable[allocationlist[i]][i]
        return sum
    else:
        return -1

def brute(costm,scost, minc, combin, level:int,records):
    mincinternal = minc
    chosen = None
    if level>0:
        for x in combin:
            newrecords = records[:]
            newrecords.append(x)
            tempc, temprecord = brute(costm,scost,minc,combin, level-1,newrecords)
            if tempc<mincinternal:
                mincinternal = tempc
                chosen = temprecord
    else:
        temp = totalusercost(records, costm)
        for x in combin:
            if x in records:
                temp+=scost[x]
        return temp , records[:]
    return mincinternal, chosen

if __name__ == "__main__":
    """
    listA=[15,4,5,7,2,7,9,5,8,6,7,20,11,8,10]
    listB=[8,9,20,6,3,7,5,9,4,1,9,11,1,10,12]
    listC=[13,9,15,6,5,14,16,20,1,13,23,3,15,2,4]
    listD=[11,2,7,9,20,9,15,6,9,13,11,2,14,6,10]
    sitecost = [10,15,20,17]
    """
    listA=[15,4,5,7]
    listB=[8,9,20,6]
    listC=[13,9,15,6]
    listD=[11,2,7,9]
    sitecost = [4, 5, 10, 2]
    costmatrix = [listA,listB,listC,listD]
    option = [i for i in range(len(costmatrix))]
    pick = list()
    lv = len(listA)
    mincost = float('inf')
    mincost, pick= brute(costmatrix,sitecost,mincost,option,lv,pick)
    print(mincost,pick)