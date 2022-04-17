import sys

def maxSubArraySumSize(a):
    maxSoFar = -sys.maxsize-1
    maxEndingHere = 0
    start = 0
    finish = 0
    s = 0
    for i in range(len(a)):
        maxEndingHere += a[i]
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
            finish = i
            start  = s
        if maxEndingHere < 0:
            maxEndingHere = 0
            s = i + 1
    return (finish - start + 1)

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySumSize(a))