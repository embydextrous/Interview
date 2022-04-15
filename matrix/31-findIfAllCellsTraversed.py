# https://www.geeksforgeeks.org/find-2-d-array-completely-traversed-not-following-cell-values/

'''
You are given a 2-D array. We have to traverse each and every cell of the given array by following the cell
locations then return true else false. The value of each cell is given by (x, y) where (x, y) is also shown
next following cell position. Eg. (0, 0) shows starting cell. And 'null' shows our final destination after
traversing every cell. 
 
Examples: 
 
Input : { 0, 1   1, 2   1, 1 
          0, 2   2, 0   2, 1 
          0, 0   1, 0   null }
Output : false

Input : { 0, 1   2, 0 
          null  1, 0
          2, 1   1, 1 }
Output : true

'''
def traverse(M):
    R, C = len(M), len(M[0])
    visited = set()
    i, j = 0, 0
    while M[i][j] != None and (i, j) not in visited:
        visited.add((i, j))
        i, j = M[i][j]
    if M[i][j] is None:
        visited.add(M[i][j])
    print(visited)
    return len(visited) == R * C

cell = [[[] for j in range(3)] for i in range(3)]
cell[0][0] = [0, 1]
cell[0][1] = [1, 2]
cell[0][2] = [1, 1]
cell[1][0] = [0, 2]  
cell[1][1] = [2, 0]  
cell[1][2] = [2, 1]  
cell[2][0] = [0, 0]
cell[2][1] = [1, 0]
cell[2][2] = None

print(traverse(cell))
