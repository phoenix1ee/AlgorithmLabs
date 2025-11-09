import queue
from pathlib import Path
import csv

def readflowgraph(in_path):
    #for reading di-graph with flow
    #each row: u,v,4
    #an edge u->v with capacity 4 
    adjlist=dict()
    F = dict()
    with open(in_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',')  # Change delimiter if needed
        for row in reader:
            if row:
                #update adjaceny list
                if row[0] not in adjlist:
                    adjlist.update({row[0]:[(row[1] if row[1] != '' else None)]})
                else:
                    adjlist[row[0]].append((row[1] if row[1] != '' else None))
                #update flow function
                if row[1] and row[2] != '':
                    if row[0] in F:
                        F[row[0]].update({row[1]:[0,int(row[2])]})
                    else:
                        F.update({row[0]:{row[1]:[0,int(row[2])]}})
    return adjlist, F

def readgraph(in_path):
    #for reading simple di-graph without flow
    #each row: u,v
    #an edge u->v
    adjlist=dict()
    with open(in_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',')  # Change delimiter if needed
        for row in reader:
            if row:
                if row[0] not in adjlist:
                    adjlist.update({row[0]:[row[1]]})
                else:
                    adjlist[row[0]].append(row[1])
    return adjlist

def flow(adj):
    F = dict()
    #assign a flow capacity of 1 to each edge
    #built Flow dict, u[v][remaining capacity,capacity]
    for u in adj.keys():
        for v in adj[u]:
            if u in F:
                F[u].update({v:[0,1]})
            else:
                F.update({u:dict()})
                F[u].update({v:[0,1]})
    return F

#BFS with flow capacity
def BFS(adj,F,s,t):
    Q = queue.Queue(-1)
    G = dict()

    #bulit graph with dict, with distance from root and predecessor
    for keys in adj.keys():
        G.update({keys:{"d":float('inf'),"pre":None}})

    if s not in G or t not in G:
        print("input vertex not found")
        return None

    visited = set()
    enqueued = set()
    G[s]["d"]=0
    G[s]["pre"]=None
    Q.put(s)
    enqueued.add(s)

    while not Q.empty():
        current = Q.get()
        if current not in visited:
            visited.add(current)
            #print(f'visiting {current}, distance from {s}: {G[current]["d"]}')
            for x in adj[current]:
                #add adjacent vertex only if they are not enqueued/visited and have remaining flow
                if x and x not in enqueued and x not in visited and F[current][x][1]-F[current][x][0]>0:
                    Q.put(x)
                    enqueued.add(x)
                    G[x]["d"]=G[current]["d"]+1
                    G[x]["pre"]=current

    if G[t]["d"] < float('inf'):
        p = list()
        v = t
        while v:
            p.insert(0,v)
            v = G[v]["pre"]
        return p
    else:
        return None

# Testing
if __name__ == "__main__":
    inpath = Path('testflowgraph.txt')
    adj , F = readflowgraph(inpath)
    print(adj)
    #F = flow(adj)
    print(F)
    print(f'path between s and t:{BFS(adj,F,"s", "t")}')
    print("finished")