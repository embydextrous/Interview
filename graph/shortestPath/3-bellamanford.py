'''
1) Negative weights are found in various applications of graphs. For example, instead of paying cost for a path, we may get some advantage if we follow 
the path.
2) Bellman-Ford works better (better than Dijkstra's) for distributed systems. Unlike Dijkstra's where we need to find the minimum value of all vertices, 
in Bellman-Ford, edges are considered one by one.                                                                  
3) Bellman-Ford does not work with undirected graph with negative edges as it will declared as negative cycle.
Exercise 
1) The standard Bellman-Ford algorithm reports the shortest path only if there are no negative weight cycles. Modify it so that it reports minimum 
distances even if there is a negative weight cycle.
2) Can we use Dijkstra's algorithm for shortest paths for graphs with negative weights - one idea can be, calculate the minimum weight value, 
add a positive value (equal to absolute value of minimum weight value) to all weights and run the Dijkstra's algorithm for the modified graph. 
Will this algorithm work?
'''
from graph import WeightedGraph

# Also see, https://www.geeksforgeeks.org/detect-negative-cycle-graph-bellman-ford/

INF = 10 ** 9

'''
Why V-1 passes? So that every path from u-v is considered.
'''

def bellmanford(g, s):
    dist = [INF] * g.V
    dist[s] = 0
    for i in range(g.V - 1):
        for u in range(g.V):
            for (v, w) in g.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        print(dist)
    for u in range(g.V):
            for (v, w) in g.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    print("Graph Contains Negative Weight Cycle")
    print(dist)

g = WeightedGraph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

bellmanford(g, 0)