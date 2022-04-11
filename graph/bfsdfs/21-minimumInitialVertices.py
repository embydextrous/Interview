'''
We are given a matrix that contains different values in each cell. Our aim is to find the minimal set 
of positions in the matrix such that the entire matrix can be traversed starting from the positions in the set. 
We can traverse the matrix under the below conditions: 

We can move only to those neighbors that contain values less than or equal to the current cell's value. 
A neighbor of the cell is defined as the cell that shares a side with the given cell.

Examples: 

Input : 1 2 3
        2 3 1
        1 1 1
Output : 1 1
         0 2
If we start from 1, 1 we can cover 6 
vertices in the order (1, 1) -> (1, 0) -> (2, 0) 
-> (2, 1) -> (2, 2) -> (1, 2). We cannot cover
the entire matrix with this vertex. Remaining 
vertices can be covered (0, 2) -> (0, 1) -> (0, 0). 

Input : 3 3
        1 1
Output : 0 1
If we start from 0, 1, we can traverse 
the entire matrix from this single vertex 
in this order (0, 0) -> (0, 1) -> (1, 1) -> (1, 0). 
Traversing the matrix in this order 
satisfies all the conditions stated above.
'''
def isSafe(R, C, i, j):
    return i >=0 and i < R and j >=0 and j < R

def dfs(M, R, C, i, j, visited):
    visited.add((i, j))
    ROW = [-1, 0, 1, 0]
    COL = [0, 1, 0, -1]
    for k in range(4):
        x, y = i + ROW[k], j + COL[k]
        if isSafe(R, C, x, y) and (x, y) not in visited and M[x][y] <= M[i][j]:
            dfs(M, R, C, x, y, visited)

def findStartingPoints(M):
    R, C = len(M), len(M[0])
    vArr = []
    visited = set()
    for i in range(R):
        for j in range(C):
            vArr.append((M[i][j], (i, j)))
    vArr.sort(key = lambda x : -x[0])
    print(vArr)
    result = []
    for element in vArr:
        (i, j) = element[1]
        if (i, j) not in visited:
            result.append((i, j))
            dfs(M, R, C, i, j, visited)
    return result


M = [[3, 3],
     [1, 1]]

print(findStartingPoints(M))