# https://www.geeksforgeeks.org/number-pair-positions-matrix-not-accessible/
'''
Given a positive integer N. Consider a matrix of N X N. No cell can be accessible from any other cell, 
except the given pair cell in the form of (x1, y1), (x2, y2) i.e there is a path (accessible) between 
(x2, y2) to (x1, y1). The task is to find the count of pairs (a1, b1), (a2, b2) such that cell (a2, b2)
is not accessible from (a1, b1).
Examples: 
 
Input : N = 2
Allowed path 1: (1, 1) (1, 2)
Allowed path 2: (1, 2) (2, 2)
Output : 6
Cell (2, 1) is not accessible from any cell
and no cell is accessible from it.
'''
def dfs(d, i, j, count, visited):
    visited.add((i, j))
    count[0] += 1
    for (x, y) in d[(i, j)]:
        if (x, y) not in visited:
            dfs(d, x, y, count, visited)

def numPairs(N, edges):
    d = {}
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            d[(i, j)] = []
    for edge in edges:
        d[edge[0]].append(edge[1])
        d[edge[1]].append(edge[0])

    result = 0
    visited = set()
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if (i, j) not in visited:
                count = [0]
                dfs(d, i, j, count, visited)
                result += count[0] * (N * N - count[0])
    return result

N = 2
edges = [[(1, 1), (1, 2)], [(1, 2), (2, 2)]]
print(numPairs(N, edges))
