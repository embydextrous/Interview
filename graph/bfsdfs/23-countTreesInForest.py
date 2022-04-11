from graph import UndirectedGraph

'''
Given n nodes of a forest (collection of trees), find the number of trees in the forest.
Tree is represented as Undirected Acyclic Graph. [Simple DFS Would Work]
Examples : 
 

Input :  edges[] = {0, 1}, {0, 2}, {3, 4}
Output : 2
Explanation : There are 2 trees
                   0       3
                  / \       \
                 1   2       4
'''

def dfs(g, s, visited):
    visited[s] = True
    for v in g.graph[s]:
        if not visited[v]:
            dfs(g, v, visited)

def countTrees(g):
    c = 0
    visited = [False] * g.V
    for i in range(g.V):
        if not visited[i]:
            dfs(g, i, visited)
            c += 1
    return c

g = UndirectedGraph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(3, 4)
g.print()
print(countTrees(g))