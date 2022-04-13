'''
            5 ----> 0 <---- 4
            |               | 
            ↓               ↓ 
            2 ----> 3 ----> 1

1. Add all vertices with degree 0 to path, mark them visited and reduce their neighbors degree by 1
2. if len(path) == V return from recursion
3. else, call recursively
'''
def findTopo(g, V, indegrees, visited, path):
    for u in range(V):
        if indegrees[u] == 0 and  not visited[u]:
            path.append(u)
            visited[u] = True
            for v in g[u]:
                indegrees[v] -= 1
    if len(path) == V:
        return
    findTopo(g, V, indegrees, visited, path)

def topo(edges, V):
    g = {i:[] for i in range(V)}
    indegrees = [0] * V
    visited = [False] * V
    for (u, v) in edges:
        indegrees[v] += 1
        g[u].append(v)
    path = []
    findTopo(g, V, indegrees, visited, path)
    return path

edges = [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]
print(topo(edges, 6))