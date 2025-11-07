import queue

class vertex:
    def __init__(self,name):
        self.d = None
        self.label = name
        self.pre = None
        self.color = None

Q = queue.Queue(-1)

G = list()
G.append({"a":["b","c","d"]})
G.append({"b":["d"]})
G.append({"c":["d"]})

root = vertex("a")
Q.put(root)
while Q.not_empty():
    pass