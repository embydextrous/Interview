'''
Given a directed tree with V vertices and V-1 edges, we need to choose such a root 
(from given nodes from where we can reach to every other node) with a minimum number of edge reversal. 

Examples:  

        0 (-->) 1 <-- 2 <-- (3) --> 4 (<--) 5 --> 6 (<--) 7

Minimum edge reversals to make a root

In above tree, if we choose node 3 as our 
root then we need to reverse minimum number
of 3 edges to reach every other node, 
changed tree is shown on the right side.
5 is also a solution.
'''
def dfs(g, s, dis, visited):
    visited[s] = True
    print(g[s])
    for (v, w) in g[s]:
        if not visited[v]:
            dis[v][0] = dis[s][0] + 1
            if w == 1:
                dis[v][1] = dis[s][1] + 1
            else:
                dis[v][1] = dis[s][1]
            dfs(g, v, dis, visited)


def minReversals(edges):
    V = len(edges) + 1 # Each edge connecting two vertices
    g = { i:[] for i in range(V) }
    for edge in edges:
        (u, v) = edge
        # Add edge with weight 0
        g[u].append([v, 0])
        # Add back edge with weight 1
        g[v].append([u, 1])
    visited = [False] * V
    dis = [[0, 0] for i in range(V)]
    dfs(g, 0, dis, visited)
    minEdgesToReverse = 10 ** 9
    selectedVertex = -1
    for i in range(V):
        # dis[i][0] - dis[i][1] - gives edges to be reversed to go back from i to start
        # dis[V-1][1] - dis[i][1] - gives edges to be reversed to reach end from i
        edgesToReverse = (dis[i][0] - dis[i][1]) + dis[V-1][1] - dis[i][1] 
        if edgesToReverse < minEdgesToReverse:
            minEdgesToReverse = edgesToReverse
            selectedVertex = i
    return (minEdgesToReverse, selectedVertex)


edges = [[ 0, 1 ], [ 2, 1 ], [ 3, 2 ], [ 3, 4 ], [ 5, 4 ], [ 5, 6 ], [ 7, 6 ]]
print(minReversals(edges))