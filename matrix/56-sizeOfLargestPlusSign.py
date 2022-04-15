# https://www.geeksforgeeks.org/find-size-of-the-largest-formed-by-all-ones-in-a-binary-matrix/
from matrix import printS

def createLeft(M, R, C):
    left = [[0 for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(1, C):
            if M[i][j-1] == 0:
                left[i][j] = 0
            else:
                left[i][j] = left[i][j-1] + 1
    return left

def createRight(M, R, C):
    right = [[0 for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C-2, -1, -1):
            if M[i][j+1] == 0:
                right[i][j] = 0
            else:
                right[i][j] = right[i][j+1] + 1
    return right

def createTop(M, R, C):
    top = [[0 for i in range(C)] for j in range(R)]
    for i in range(1, R):
        for j in range(C):
            if M[i-1][j] == 0:
                top[i][j] = 0
            else:
                top[i][j] = top[i-1][j] + 1
    return top

def createBottom(M, R, C):
    bottom = [[0 for i in range(C)] for j in range(R)]
    for i in range(R-2, -1, -1):
        for j in range(C):
            if M[i+1][j] == 0:
                bottom[i][j] = 0
            else:
                bottom[i][j] = bottom[i+1][j] + 1
    return bottom

M = [ [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
      [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
      [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
      [ 0, 0, 0, 0, 1, 0, 0, 1, 0, 0 ],
      [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
      [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
      [ 1, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
      [ 1, 0, 1, 1, 1, 1, 0, 0, 1, 1 ],
      [ 1, 1, 0, 0, 1, 0, 1, 0, 0, 1 ],
      [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ]]

def findMaxPlusSign(M):
    R, C = len(M), len(M[0])
    left = createLeft(M, R, C)
    top = createTop(M, R, C)
    right = createRight(M, R, C)
    bottom = createBottom(M, R, C)
    maxPlusSize = 1
    for i in range(R):
        for j in range(C):
            plusSize = min(left[i][j], top[i][j], right[i][j], bottom[i][j]) * 4 + 1
            maxPlusSize = max(plusSize, maxPlusSize)
    return maxPlusSize

print(findMaxPlusSign(M))