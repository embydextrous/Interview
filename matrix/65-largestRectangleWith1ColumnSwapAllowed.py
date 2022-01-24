from matrix import printS

def largestRectangle(M):
    R, C = len(M), len(M[0])
    # Complexity - O(n^2)
    for i in range(R):
        for j in  range(C):
            if i != 0:
                if M[i][j] == 1:
                    M[i][j] = M[i-1][j] + 1
    # Count Sort - O(n)
    d = { x : M[R-1].count(x) for x in M[R-1] }
    k = 0
    for i in range(R, -1, -1):
        if i in d:
            for j in range(d[i]):
                M[R-1][k] = i
                k += 1
    maxArea = 0
    # O(n)
    for i in range(C):
        h = M[R-1][i]
        l = i + 1
        maxArea = max(maxArea, h * l)
    return maxArea


M = [[0, 1, 0, 1, 0],
     [0, 1, 0, 1, 1],
     [1, 1, 0, 1, 0]]

print(largestRectangle(M))