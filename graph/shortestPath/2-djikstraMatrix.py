INF = 10**9

def findClosestVertex(V, dist, sptSet):
    minDist = INF
    u = -1
    for v in range(V):
        if v not in sptSet and dist[v] < minDist:
            minDist = dist[v]
            u = v
    return u

def djikstra(G, s):
    V = len(G)
    sptSet = set()
    dist = [INF if i != s else 0 for i in range(V)]
    print(dist)
    for i in range(V):
        u = findClosestVertex(V, dist, sptSet)
        sptSet.add(u)
        for v in range(V):
            if v not in sptSet and G[u][v] != 0 and dist[u] + G[u][v] < dist[v]:
                dist[v] = dist[u] + G[u][v]
    print(dist)

G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

djikstra(G, 0)