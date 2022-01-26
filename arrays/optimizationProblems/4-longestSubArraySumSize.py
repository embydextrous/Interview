import sys

def maxSubArraySumSize(a):
    maxSoFar = -sys.maxsize-1
    maxEndingHere = 0
    start = 0
    size = 0
    for i in range(len(a)):
        maxEndingHere += a[i]
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
            size = i - start + 1
        if maxEndingHere < 0:
            maxEndingHere = 0
            start = i + 1
    return size

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySumSize(a))