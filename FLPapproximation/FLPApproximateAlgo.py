def totalusercost(allocationlist, costtable):
    sum = 0
    if len(allocationlist) == len(costtable[0]):
        for i in range(len(allocationlist)):
            sum += costtable[allocationlist[i]][i]
        return sum
    else:
        return -1

def alternate_minsite(alloption,delete,cost,userid,siteavailable):
    #return alternate site with minimum user cost
    alternateMin = float('inf')
    alternatesite = -1
    for x in alloption:
        if x != delete and x in siteavailable:
            if cost[x][userid]<alternateMin:
                alternateMin = cost[x][userid]
                alternatesite = x
    return alternatesite

def FLPapproximate(costmatrix,sitecost,):
    #pick initial site with lowest total fixed+user cost
    pickedsite = []
    pick = None
    mincost = float('inf')

    for i in range(len(sitecost)):
        temppick = [i]*len(costmatrix[0])
        sum = totalusercost(temppick,costmatrix)
        sum+=sitecost[i]
        if sum<mincost:
            pick = temppick
            mincost = sum

    #loop thr remaining site and look for additional sites with net benefit
    pickedsite.append(pick[0])
    for x in option:
        if x not in pickedsite:
            tempchange = pick[:]
            saving = 0
            for i in range(len(tempchange)):
                if costmatrix[x][i]<costmatrix[tempchange[i]][i]:
                    saving = saving - costmatrix[tempchange[i]][i]+costmatrix[x][i]
                    tempchange[i]=x
            saving = saving + sitecost[x]
            # add site if beneficial
            if saving<0:
                pick = tempchange
                mincost = mincost + saving
                pickedsite.append(x)
            # check if possible to delete site from current site selections
                newcost = mincost
                newpickedsite = None
                newpicked = None
                for y in pickedsite[:]:
                    tempchangeii = pick[:]
                    for i in range(len(pick)):
                        tempchangeii[i]=alternate_minsite(option,y,costmatrix,i,pickedsite)
                    tempcost = totalusercost(tempchangeii,costmatrix)
                    temppickedsite = [z for z in pickedsite if z != y]
                    for z in temppickedsite:
                        tempcost = tempcost + sitecost[z]
                    if tempcost < newcost:
                        newcost = tempcost
                        newpicked = tempchangeii
                        newpickedsite = temppickedsite
                if newcost<mincost:
                    mincost = newcost
                    pick = newpicked
                    pickedsite = newpickedsite
    return pickedsite,pick,mincost

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
    ps,p,mc = FLPapproximate(costmatrix,sitecost)
    print("final")
    print(f'selected sites are {ps}')
    print(f'user allocations = {p}')
    print(f'total cost = {mc}')
    