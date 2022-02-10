'''
A vertex is mother vertex if all nodes can be reached through it.

1. For disconnected graphs, there is no mother vertex.
2. For connected undirected graphs, all vertices are mother vertices.
3. For connected directed graphs, the last vertex when we visit dfs can be mother vertex.

Let us say V is last vertex in dfs. Let say there is an edge from U -> V where U is not a mother vertex.

1. if U is visited before V, there can't be edge U -> V otherwise V would be visited.
2. if V is visited before U, if there would have been an edge V must be also visited.
'''
from graph import Graph

def dfsUtil(vertex, visited):
    visited.add(vertex)
    for neighbor in vertex.next:
        if neighbor not in visited:
            dfsUtil(neighbor, visited)

def findMother(graph):
    v = None
    visited = set()
    for vertex in graph.vertices:
        if vertex not in visited:
            dfsUtil(vertex, visited)
            v = vertex
    if v is None:
        return None
    visited = set()
    q = [v]
    visited.add(v)
    while len(q) > 0:
        u = q.pop(0)
        for neighbor in u.next:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return v if len(visited) == len(graph.vertices) else None

g = Graph()
node0 = g.addVertex(0)
node1 = g.addVertex(1)
node2 = g.addVertex(2)
node3 = g.addVertex(3)
node4 = g.addVertex(4)
node5 = g.addVertex(5)
node6 = g.addVertex(6)

g.addEdge(node0, node1)
g.addEdge(node0, node2)
g.addEdge(node1, node3)
g.addEdge(node4, node1)
g.addEdge(node5, node2)
g.addEdge(node5, node6)
g.addEdge(node6, node0)
g.addEdge(node6, node4)

mother = findMother(g)
if mother:
    print(mother.data)
else:
    print(None)