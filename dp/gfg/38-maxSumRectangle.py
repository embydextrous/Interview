'''
Given a 2D array, find the maximum sum subarray in it. For example, in the following 2D array, the maximum sum subarray is highlighted with blue rectangle and sum of this 
subarray is 29.

M = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [4, -1, 1, 7, -6]]
'''
def kadane(a):
    maxSoFar = -10 ** 9
    maxEndingHere = 0
    start = finish = s = 0
    for i in range(len(a)):
        maxEndingHere += a[i]
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
            finish = i
            start = s
        if maxEndingHere < 0:
            maxEndingHere = 0
            s = i + 1
    return maxSoFar, start, finish

def largestRectangleSum(M):
    R, C = len(M), len(M[0])
    maxRectangleSum = -10 ** 9
    fl = fr = ft = fb = 0
    for left in range(C):
        temp = [0 for i in range(R)]
        for right in range(left, C):
            for i in range(R):
                temp[i] += M[i][right]
            maxSum, start, finish = kadane(temp)
            if maxSum > maxRectangleSum:
                fl = left
                fr = right
                ft = start
                fb = finish
                maxRectangleSum = maxSum
    for i in range(ft, fb + 1):
        for j in range(fl, fr + 1):
            print(M[i][j], end = " ")
        print()
    return maxRectangleSum
        
M = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]

print(largestRectangleSum(M))