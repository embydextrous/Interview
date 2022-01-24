def isValid(M, R, C, i, j):
    return i >= 0 and i < R and j >= 0 and j < C and M[i][j] == 1

def shortestPath(M, source, destination):
    R, C = len(M), len(M[0])
    visited = [[False for i in range(C)] for j in range(R)]
    q = [[source[0], source[1], 0]]
    while len(q) > 0:
        (i, j, d) = q.pop(0)
        #print(i, j, d)
        if i == destination[0] and j == destination[1]:
            return d
        visited[i][j] = True
        if isValid(M, R, C, i, j - 1) and not visited[i][j-1]:
            q.append([i, j-1, d + 1])
        if isValid(M, R, C, i-1, j) and not visited[i-1][j]:
            q.append([i-1, j, d + 1])
        if isValid(M, R, C, i, j+1) and not visited[i][j+1]:
            q.append([i, j+1, d + 1])
        if isValid(M, R, C, i+1, j) and not visited[i+1][j]:
            q.append([i+1, j, d + 1])
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
dest = (7,4)

print(shortestPath(M, source, dest))