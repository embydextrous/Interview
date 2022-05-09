'''
Given a square chessboard of N x N size, the position of Knight and position of a target is given. 
We need to find out the minimum steps a Knight will take to reach the target position.
Examples: 
 

In above diagram Knight takes 3 step to reach 
from (4, 5) to (1, 1) (4, 5) -> (5, 3) -> (3, 2) -> (1, 1)  as shown in diagram
'''
# https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/

from collections import deque

def isSafe(N, x, y):
    return x > 0 and x <= N and y > 0 and y <= N

def knightTour(N, sx, sy, fx, fy):
    q = deque([[sx, sy, 0]])
    result = {}
    result[(sx, sy)] = (-1, -1)
    ROW = [1, -1, -2, -2, -1, 1, 2, 2]
    COL = [-2, -2, -1, 1, 2, 2, 1, -1]
    minSteps = 0
    while len(q) > 0:
        i, j, d = q.popleft()
        if i == fx and j == fy:
            minSteps = d
            break
        for k in range(8):
            x, y = i + ROW[k], j + COL[k]
            if isSafe(N, x, y) and (x, y) not in result:
                result[(x, y)] = (i, j)
                q.append([x, y, d + 1])
    print(f"Minimum steps to reach {(fx, fy)} from {(sx, sy)} are {minSteps}.")
    s = deque()
    i, j = fx, fy
    while (i, j) != (-1, -1):
        s.appendleft((i, j))
        i, j = result[(i, j)]
    print(s)

N = 30
sx, sy = 1, 1
fx, fy = 30, 30
print(knightTour(N, sx, sy, fx, fy))

