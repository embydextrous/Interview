'''
Count the total number of ways or paths that exist between two vertices in a directed graph. These paths 
don't contain a cycle, the simple enough reason is that a cycle contains an infinite number of paths and 
hence they create a problem. 
Examples: 

For the following Graph:

https://media.geeksforgeeks.org/wp-content/uploads/paths1.png
  
Input: Count paths between A and E
Output : Total paths between A and E are 4
Explanation: The 4 paths between A and E are:
                      A -> E
                      A -> B -> E
                      A -> C -> E
                      A -> B -> D -> C -> E 

Input : Count paths between A and C
Output : Total paths between A and C are 2
Explanation: The 2 paths between A and C are:
                      A -> C
                      A -> B -> D -> C
'''
from graph import Graph

# Time Complexity - O(N!)
def dfs(g, s, d, count, visited):
    visited[s] = True
    if s == d:
        count[0] += 1
    else:
        for i in g.graph[s]:
            if not visited[i]:
                dfs(g, i, d, count, visited)
    visited[s] = False

def countPaths(g, s, d):
    count = [0]
    visited = [False] * g.V
    dfs(g, s, d, count, visited)
    print(visited)
    return count[0]

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(0, 4)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(3, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(1, 4)
 
s = 0
d = 4
print(countPaths(g, s, d))