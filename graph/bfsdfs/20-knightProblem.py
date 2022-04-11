'''
Given a square chessboard of N x N size, the position of Knight and position of a target is given. 
We need to find out the minimum steps a Knight will take to reach the target position.
Examples: 
 

In above diagram Knight takes 3 step to reach 
from (4, 5) to (1, 1) (4, 5) -> (5, 3) -> (3, 2) -> (1, 1)  as shown in diagram
'''
# https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/

def isSafe(N, i, j):
    return i >= 1 and i <= N and j >=1 and j <= N

def minHops(N, sx, sy, fx, fy):
    if fx == sx and fy == sy:
        return 0
    visited = set()
    q1, q2 = [(sx, sy)], []
    ROW = [1, -1, -2, -2, -1, 1, 2, 2]
    COL = [-2, -2, -1, 1, 2, 2, 1, -1]
    steps = 0
    result = {}
    while len(q1) > 0:
        steps += 1
        while len(q1) > 0:
            (i, j) = q1.pop(0)
            for k in range(8):
                x, y = i + ROW[k], j + COL[k]
                if x == fx and y == fy:
                    result[(x, y)] = (i, j)
                    break
                point = (x, y)
                if isSafe(N, x, y) and point not in visited:
                    result[(x, y)] = (i, j)
                    visited.add(point)
                    q2.append(point)
        q1, q2 = q2, q1
        if (fx, fy) in result:
            break
    s = []
    i, j = fx, fy
    while (i, j) != (sx, sy):
        s.append((i, j))
        (i, j) = result[(i, j)]
    s.append((sx, sy))
    return s[::-1]

N = 30
sx, sy = 1, 1
fx, fy = 30, 30
print(minHops(N, sx, sy, fx, fy))

