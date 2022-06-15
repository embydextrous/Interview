'''
The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. The problem is to find shortest distances between every pair of 
vertices in a given edge weighted directed Graph. 
Example: 

Input:
       graph[][] = { {0,   5,  INF, 10},
                    {INF,  0,  3,  INF},
                    {INF, INF, 0,   1},
                    {INF, INF, INF, 0} }

which represents the following graph
             10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3       
Note that the value of graph[i][j] is 0 if i is equal to j 
And graph[i][j] is INF (infinite) if there is no edge from vertex i to j.

Output:
Shortest distance matrix
      0      5      8      9
    INF      0      3      4
    INF    INF      0      1
    INF    INF    INF      0
'''
# Also see, https://www.geeksforgeeks.org/detecting-negative-cycle-using-floyd-warshall/

INF = 10 ** 9

def floydWarshall(G):
    V = len(G)
    result = [[G[i][j] for j in range(V)] for i in range(V)]
    for v in range(V):
        for i in range(V):
            for j in range(V):
                    result[i][j] = min(result[i][j], result[i][v] + result[v][j])
    return result

G = [[0, 5, INF, 10],
     [INF, 0, 3, INF],
     [INF, INF, 0, 1],
     [INF, INF, INF, 0]]

result = floydWarshall(G)
for row in result:
    print(row)