import sys

def maxSubArraySum(a):
    maxSoFar = -sys.maxsize-1
    maxEndingHere = 0
    for i in a:
        maxEndingHere += i
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
        if maxEndingHere < 0:
            maxEndingHere = 0
    return maxSoFar

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySum(a))