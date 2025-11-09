import queue
from pathlib import Path
import csv
from BFS import readgraph, flow,BFS

def printmatch(F):
    output = dict()
    for keys in F["s"]:
        for x in F[keys]:
            for y in F[x]:
                if F["s"][keys][0]==1 and F[keys][x][0]==1 and F[x][y][0]==1:
                    output.update({keys:x})
    return output

def EdmondKarpMaxMatch(adj):
    """
    find max match with Edmonds-Karp algorithm between s and t for a bipartite-graph
    :param adj :adjacency dict: in form of {'s': ['1', '2'], '1': ['3'],...}
    :return: max matching
    """

    left = [keys for keys in adj]
    adj.update({"s":[keys for keys in left]})
    for keys in left:
        for x in adj[keys]:
            if x not in adj:
                adj.update({x:["t"]})

    adj.update({"t":list()})
    #add unit capacity to every input edge
    F = flow(adj)

    totalflow = 0
    cont = True
    while cont:
        path = BFS(adj,F,"s","t")
        print(path)
        if path:
            #find the maximum augmented flow
            af = float('inf')
            for i in range(len(path)-1):
                af = min(af, F[path[i]][path[i+1]][1]-F[path[i]][path[i+1]][0])
            #update total flow, residual capacity and add reverse edge, update adjacency list
            for i in range(len(path)-1):
                #add reverse edge to adjacency list
                if path[i+1] not in adj:
                    adj.update({path[i+1]:[path[i]]})
                else:
                    if path[i] not in adj[path[i+1]]:
                        adj[path[i+1]].append(path[i])
                #updated flow
                F[path[i]][path[i+1]][0] += af
                if path[i+1] in F:
                    if path[i] in F[path[i+1]]:
                        F[path[i+1]][path[i]][0]+=af
                    else:
                        F[path[i+1]].update({path[i]:[0,af]})
                else:
                    F.update({path[i+1]:{path[i]:[0,af]}})
            totalflow +=af
        else:
            cont = not cont
    return totalflow, printmatch(F)

# Testing
if __name__ == "__main__":
    inpath = Path('testgraph.txt')
    adj = readgraph(inpath)
    maxflow, m = EdmondKarpMaxMatch(adj)
    print(f'max flow: {maxflow}')
    print(f'matching: {m}')