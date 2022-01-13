# https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/

def isvalid(M, R, C, i, j):
    return (i >= 0 and j >= 0 and i < R and j < C and M[i][j] == 1)

def checkall(M):
    R, C = len(M), len(M[0])
    for i in range(R):
       for j in range(C):
          if (M[i][j] == 1):
             return False
    return True

def rotOranges(M):
    q = []
    ans = 0
    R, C = len(M), len(M[0])
    visited = [[False for i in range(C)] for j in range(R)]
    for i in range(R):
       for j in range(C):
            if (M[i][j] == 2):
                q.append((i, j, 0))
    while len(q) > 0:
        (i, j, d) = q.pop(0)
        visited[i][j] = True
        ans = d
        if isvalid(M, R, C, i + 1, j) and not visited[i+1][j]:
            M[i + 1][j] = 2
            q.append((i + 1, j, d + 1))
        if isvalid(M, R, C, i - 1, j) and not visited[i-1][j]:
            M[i - 1][j] = 2
            q.append((i - 1, j, d + 1))
        if isvalid(M, R, C, i, j-1) and not visited[i][j-1]:
            M[i][j - 1] = 2
            q.append((i, j - 1, d + 1))
        if isvalid(M, R, C, i, j+1) and not visited[i][j+1]:
            M[i][j + 1] = 2
            q.append((i, j + 1, d + 1))
    return ans if(checkall(M)) else -1

# Driver program
if __name__ == '__main__':
    M = [[2, 1, 0, 2, 1],
         [1, 0, 1, 2, 1],
         [1, 0, 0, 2, 1]]
    ans = rotOranges(M)
    if (ans == -1):
        print("All oranges cannot rot")
    else:
        print("Time required for all oranges to rot => " , ans)

        # This code is contributed by mohit kumar 29