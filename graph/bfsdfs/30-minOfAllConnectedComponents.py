'''
Given an array A of N numbers where Ai represent the value of the (i+1)th node. Also given are M pair 
of edges where u and v represent the nodes that are connected by an edge. The task is to find the sum 
of the minimum element in all the connected components of the given undirected graph. 
If a node has no connectivity to any other node, count it as a component with one node.
Examples:

    Input: a[] = {1, 6, 2, 7, 3, 8, 4, 9, 5, 10} m = 5
    1 2
    3 4
    5 6
    7 8
    9 10

    Output: 15
    Connected components are: 1-2, 3-4, 5-6, 7-8 and 9-10
    Sum of Minimum of all them : 1 + 2 + 3 + 4 + 5 = 15

    Input: a[] = {2, 5, 3, 4, 8} m = 2
    1 4
    4 5
    Output: 10
'''
from graph import UndirectedGraph

def dfs(g, i, visited, a, mini):
    visited[i] = True
    if a[i] < mini[0]:
        mini[0] = a[i]
    for v in g.graph[i]:
        if not visited[v]:
            dfs(g, v, visited, a, mini)

def findMinSum(a, edges):
    g = UndirectedGraph(len(a))
    for edge in edges:
        g.addEdge(edge[0] - 1, edge[1] - 1)
    visited = [False] * g.V
    result = 0
    for i in range(g.V):
        if not visited[i]:
            mini = [a[i]]
            dfs(g, i, visited, a, mini)
            result += mini[0]
    return result

a = [2, 5, 3, 4, 8]
edges = [[1, 4], [4, 5]]
print(findMinSum(a, edges))
