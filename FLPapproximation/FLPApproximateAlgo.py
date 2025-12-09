listA=[15,4,5,7,2,7,9,5,8,6,7,20,11,8,10]
listB=[8,9,20,6,3,7,5,9,4,1,9,11,1,10,12]
listC=[13,9,15,6,5,14,16,20,1,13,23,3,15,2,4]
listD=[11,2,7,9,20,9,15,6,9,13,11,2,14,6,10]
costmatrix = [listA, listB, listC, listD]
sitecost = [10, 15, 20, 17]
option = [i for i in range(len(costmatrix))]
usernos = len(listA)

def totalusercost(allocationlist, costtable):
    sum = 0
    if len(allocationlist) == len(costtable[0]):
        for i in range(len(allocationlist)):
            sum += costtable[allocationlist[i]][i]
        return sum
    else:
        return -1

def alternate_minsite(userid,currentsite,cost):
    #return alternate site with minimum user cost
    site = -1
    minimum = float('inf')
    for i in range(len(cost)):
        if i !=currentsite and cost[i][userid]<minimum:
            site = i
            minimum = cost[i][userid]
    return site

#pick initial site
result = [None,float('inf')]
pick = None
mincost = float('inf')

for i in range(len(sitecost)):
    temppick = [i]*usernos
    sum = totalusercost(temppick,costmatrix)
    sum+=sitecost[i]
    print(temppick,sum)
    if sum<mincost:
        pick = temppick
        mincost = sum

print(mincost)
print(pick)

#loop thr remaining site and look for additional sites
base = pick[0]
for x in option:
    if x != base:
        tempchange = pick[:]
        saving = 0
        for i in range(len(tempchange)):
            if costmatrix[x][i]<costmatrix[tempchange[i]][i]:
                saving = saving - costmatrix[tempchange[i]][i]+costmatrix[x][i]
                tempchange[i]=x
        saving = saving + sitecost[x]
        print(saving)
        print(tempchange)
        # add site if beneficial
        if saving<0:
            pick = tempchange
            mincost = mincost + saving
        # check if possible to delete location after added one
"""
            for y in option:
                if y in pick:
                    tempchangeii = pick[:]
                    saving2 = 0
                    for j in range(len(tempchangeii)):
                        alternate = alternate_minsite(j, result[0][j], costmatrix)
                        diff = diff + costmatrix[alternate][j] - costmatrix[result[0][j]][j]
                        #[userid,new site]
                        swaplist.append([j,alternate])
                    print(diff, sitecost[z])
                    if diff < sitecost[z]:
                        print(f'swap = {swaplist}')
                        for zz in swaplist:
                            result[0][zz[0]]=zz[1]
                        pick.remove(z)
                        print(result)
                        print(pick)
"""