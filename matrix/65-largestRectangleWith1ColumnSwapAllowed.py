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
    for i in range(R):
        d = { x : M[i].count(x) for x in M[i] }
        p = 0
        for j in range(i+1, -1, -1):
            if j in d:
                for k in range(d[j]):
                    M[i][p] = j
                    p += 1
    maxArea = 0
    for i in range(R):
        for j in range(C):
            h = M[i][j]
            l = j + 1
            print(h * l, end = " ")
            maxArea = max(maxArea, h * l)
        print()
    return maxArea


M = [[0, 1, 0, 1, 0],
     [0, 1, 0, 1, 1],
     [1, 1, 0, 1, 0]]

print(largestRectangle(M))