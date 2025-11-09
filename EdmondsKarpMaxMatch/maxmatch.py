import queue
from pathlib import Path
import csv
from BFS import readgraph, flow,BFS


def EdmondKarpMaxMatch(adj):
    """
    find max flow with Edmonds-Karp algorithm between two vertex on a di-graph with flow capacity
    :param adj :adjacency dict: in form of {'s': ['1', '2'], '1': ['3'],...}
    :param F :flow capacity dict for each edge, {'s': {'1': [0, 16], '2': [0, 13]},...}
    :param s :start
    :param t :end
    :return: max flow between two vertex
    """

    left = [keys for keys in adj]
    adj.update({"s":[keys for keys in left]})
    for keys in left:
        for x in adj[keys]:
            if x not in adj:
                adj.update({x:["t"]})
                break
    
    adj.update({"t":list()})

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
            #update total flow, residual capacity and add reverse edge
            for i in range(len(path)-1):
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
    return totalflow

# Testing
if __name__ == "__main__":
    inpath = Path('testgraph.txt')
    adj = readgraph(inpath)
    print(f'max flow: {EdmondKarpMaxMatch(adj)}')
