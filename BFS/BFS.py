import queue
from pathlib import Path
import csv

def readgraph(in_path):
    readin=dict()
    with open(in_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',')  # Change delimiter if needed
        for row in reader:
            if row:
                if row[0] not in readin:
                    readin.update({row[0]:[row[1]]})
                else:
                    readin[row[0]].append(row[1])
    return readin

def flow(adj):
    F = dict()
    #built Flow dict, u.v.[remaining capacity,capacity]
    for u in adj.keys():
        for v in adj[u]:
            if u in F:
                F[u].update({v:[0,1]})
            else:
                F.update({u:dict()})
                F[u].update({v:[0,1]})
    return F


def BFS(adj,s,t):
    Q = queue.Queue(-1)
    G = dict()

    #bulit graph with dict, with distance from root and predecessor
    for keys in adj.keys():
        G.update({keys:{"d":float('inf'),"pre":None}})

    if s not in G or t not in G:
        return None

    visited = set()
    enqueued = set()
    G[s]["d"]=0
    Q.put(s)
    enqueued.add(s)

    while not Q.empty():
        current = Q.get()
        if current not in visited:
            visited.add(current)
            print(f'visiting {current}, distance from {s}: {G[current]["d"]}')
            for x in adj[current]:
                if x not in enqueued and x not in visited:
                    Q.put(x)
                    enqueued.add(x)
                    G[x]["d"]=G[current]["d"]+1
                    G[x]["pre"]=current
    return G[t]["d"]

# Testing
if __name__ == "__main__":
    inpath = Path('testgraph.txt')
    adj = readgraph(inpath)
    F = flow(adj)
    print(F)
    print(f'distance 1 and 4:{BFS(adj,"1", "4")}')
    print("finished")