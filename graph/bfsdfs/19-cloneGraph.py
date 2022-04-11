class GraphNode:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

    def __repr__(self):
        return str(self.data)

class Graph:
    def __init__(self):
        self.vertices = []

    def addVertex(self, u):
        self.vertices.append(u)

    def addEdge(self, u, v):
        u.neighbors.append(v)

    def print(self):
        for vertex in self.vertices:
            print("{} -> {}".format(vertex, vertex.neighbors))

def bfs(clone, vertex, nodeMap):
    q = [vertex]
    while len(q) > 0:
        node = q.pop(0)
        if node not in nodeMap:
            nodeMap[node] = GraphNode(node.data)
        cloneNode = nodeMap[node]
        for v in node.neighbors:
            if v not in nodeMap:
                nodeMap[v] = GraphNode(v.data)
                q.append(v)
            cloneNode.neighbors.append(nodeMap[v])
        clone.addVertex(cloneNode)

def cloneGraph(g):
    clone = Graph()
    nodeMap = {}
    for vertex in g.vertices:
        if vertex not in nodeMap:
            bfs(clone, vertex, nodeMap)
    return clone

g = Graph()
g0 = GraphNode(0)
g1 = GraphNode(1)
g2 = GraphNode(2)
g3 = GraphNode(3)
g4 = GraphNode(4)
g5 = GraphNode(5)
g6 = GraphNode(6)
g.addVertex(g0)
g.addVertex(g1)
g.addVertex(g2)
g.addVertex(g3)
g.addVertex(g4)
g.addVertex(g5)
g.addVertex(g6)
g.addEdge(g0, g1)
g.addEdge(g0, g3)
g.addEdge(g0, g6)
g.addEdge(g1, g2)
g.addEdge(g5, g4)
g.addEdge(g6, g3)
g.print()
print()
cloneGraph(g).print()



    