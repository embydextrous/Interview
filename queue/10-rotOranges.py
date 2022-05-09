# https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/

from collections import deque

ROW = [0, -1, 0, 1]
COL = [-1, 0, 1, 0]

def isSafe(R, C, x, y):
    return x >= 0 and x < R and y >= 0 and y < C

def bfs(M, R, C, i, j, result):
    visited = set()
    visited.add((i, j))
    q = deque([[i, j, 0]])
    while len(q) > 0:
        i, j, d = q.popleft()
        if d < result[i][j]:
            result[i][j] = d
        for k in range(4):
            x, y = i + ROW[k], j + COL[k]
            if isSafe(R, C, x, y) and M[x][y] == 1 and (x, y) not in visited:
                visited.add((x, y))
                q.append([x, y, d + 1])

def minTime(M):
    R, C = len(M), len(M[0])
    result = [[10**9 for j in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            if M[i][j] == 2:
                bfs(M, R, C, i, j, result)
    maxi = 0
    print(result)
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                if result[i][j] == 0:
                    return -1
                else:
                    maxi = max(maxi, result[i][j])
    return maxi
            

# Driver program
if __name__ == '__main__':
    M = [[2, 1, 0, 2, 1],
         [1, 0, 1, 2, 1],
         [1, 0, 0, 2, 1]]
    ans = minTime(M)
    if (ans == -1):
        print("All oranges cannot rot")
    else:
        print("Time required for all oranges to rot => " , ans)

        # This code is contributed by mohit kumar 29