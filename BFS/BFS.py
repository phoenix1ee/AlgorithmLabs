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

Q = queue.Queue(-1)

inpath = Path('testgraph.txt')

"""
adj = dict()
adj.update({"a":["b","c"]})
adj.update({"b":["a","d"]})
adj.update({"c":["a","d"]})
adj.update({"d":["b","c"]})
"""
adj = readgraph(inpath)
G = dict()

for keys in adj.keys():
    G.update({keys:{"d":float('inf'),"pre":None}})

visited = set()
enqueued = set()
root = "1"
G[root]["d"]=0
Q.put(root)
enqueued.add(root)

while not Q.empty():
    current = Q.get()
    if current not in visited:
        visited.add(current)
        print(current, G[current]["d"])
        for x in adj[current]:
            if x not in enqueued and x not in visited:
                Q.put(x)
                enqueued.add(x)
                G[x]["d"]=G[current]["d"]+1
                G[x]["pre"]=current

print("finished")