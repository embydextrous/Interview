import sys

def kadane(a):
    n = len(a)
    maxSoFar = -sys.maxsize-1
    maxEndingHere = 0
    start = finish =  0
    s = 0
    for i in range(n):
        maxEndingHere += a[i]
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
            # Finish is always right
            start = s
            finish = i
        if maxEndingHere < 0:
            maxEndingHere = 0
            s = i + 1
    # In case maxEnding here later becomes 0
    return (maxSoFar, start, finish)

def largestRectangleSum(M):
    R, C = len(M), len(M[0])
    maxSum = -sys.maxsize-1
    finalLeft = finalTop = finalRight = finalBottom = 0
    for left in range(C):
        temp = [0] * R
        for right in range(left, C):
            for i in range(R):
                temp[i] += M[i][right]
            (sum, start, finish) = kadane(temp)
            if sum > maxSum:
                maxSum = sum
                finalLeft = left
                finalRight = right
                finalTop = start
                finalBottom = finish
    return(maxSum, [finalLeft, finalTop], [finalBottom, finalRight])

# -2 -5 22 3


M = [[1,  2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3,  8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]

print(largestRectangleSum(M))
