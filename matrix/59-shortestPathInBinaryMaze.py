'''
Given a MxN matrix where each element can either be 0 or 1. We need to find the shortest path between
a given source cell to a destination cell. The path can only be created out of a cell if its value is 1.
Expected time complexity is O(MN).
For example - 

Input:
mat[ROW][COL]  = {{1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
                  {1, 0, 1, 0, 1, 1, 1, 0, 1, 1 },
                  {1, 1, 1, 0, 1, 1, 0, 1, 0, 1 },
                  {0, 0, 0, 0, 1, 0, 0, 0, 0, 1 },
                  {1, 1, 1, 0, 1, 1, 1, 0, 1, 0 },
                  {1, 0, 1, 1, 1, 1, 0, 1, 0, 0 },
                  {1, 0, 0, 0, 0, 0, 0, 0, 0, 1 },
                  {1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
                  {1, 1, 0, 0, 0, 0, 1, 0, 0, 1 }};
Source = {0, 0};
Destination = {3, 4};

Output:
Shortest Path is 11 
'''

def isValid(R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C

def shortestPath(M, source, destination):
    R, C = len(M), len(M[0])
    q = [[source[0], source[1], 0]]
    ROW = [0, -1, 0, 1]
    COL = [-1, 0, 1, 0]
    visited = set()
    visited.add(source)
    while len(q) > 0:
        x, y, d = q.pop(0)
        if x == destination[0] and y == destination[1]:
            return d
        for k in range(4):
            i, j = x + ROW[k], y + COL[k]
            if isValid(R, C, i, j) and (i, j) not in visited and M[i][j] == 1:
                q.append([i, j, d + 1])
                visited.add((i, j))
    return -1        
    
    
M = [[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
     [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
     [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
     [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
     [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
     [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
     [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
     [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
     [ 1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]
source = (0,0)
dest = (3,4)

print(shortestPath(M, source, dest))