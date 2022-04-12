'''
Given a directed graph, a source vertex src and a destination vertex dst, print all paths from given src to dst.
Consider the following directed graph. Let the src be 2 and dst be 3. There are 3 different paths from 2 to 3.
 
'''
from graph import Graph

def printAllPaths(g, s, d):
    q = [[s]]
    while len(q) > 0:
        path = q.pop(0)
        if path[-1] == d:
            print(path)
        else:
            for v in g.graph[path[-1]]:
                if v not in path:
                    pathCopy = path[:]
                    pathCopy.append(v)
                    q.append(pathCopy)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
printAllPaths(g, 2, 3)
