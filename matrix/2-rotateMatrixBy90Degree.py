# anti-clockwise rotation
from matrix import printS

def rotateRingAntiClockwise(m, n, k):
    backValue = m[k][k+1]
    # rotate left
    for i in range(k, n - k):
        m[i][k], backValue = backValue, m[i][k]
    # rotate bottom
    for i in range(k+1, n - k):
        m[n-k-1][i], backValue = backValue, m[n-k-1][i]
    # rotate right
    for i in range(n-k-2, k - 1, -1):
        m[i][n-k-1], backValue = backValue, m[i][n-k-1]
    # rotate top
    for i in range(n - k - 2, k, -1):
        m[k][i], backValue = backValue, m[k][i]

def rotateMatrix(m):
    n = len(m)
    for i in range(n//2):
        rotateRingAntiClockwise(m, n, i)

# Complexity O()
def rotateMatrixBy90Degree(m):
    n = len(m)
    for i in range(n//2):
        for j in range(n - 2 * i - 1):
            rotateRingAntiClockwise(m, n, i)

# Complexity O(n^2)
def rotateMatrixBy90Degree2(m):
    # transpose
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]

    # reverse all columns
    for i in range(n):
        l, r = 0, n - 1
        while l < r:
            m[l][i], m[r][i] = m[r][i], m[l][i]
            l += 1
            r -= 1


matrix =[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ] 
        ]

rotateMatrixBy90Degree2(matrix)
printS(matrix)