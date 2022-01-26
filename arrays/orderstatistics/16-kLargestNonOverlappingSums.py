# https://www.geeksforgeeks.org/k-maximum-sums-non-overlapping-contiguous-sub-arrays/
# We can use Kadane's Algorithm for it
# We need to modify kadane's algorithm as under:
# Get start and finish indexes and set all elements to - inf
# Perform this k times
import sys

def modifiedKadane(a):
    maxSoFar = -sys.maxsize-1
    maxEndingHere = 0
    finalPair = (0, 0)
    start = 0
    for i in range(len(a)):
        maxEndingHere += a[i]
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
            finalPair = (start, i)
        if maxEndingHere < 0:
            maxEndingHere = 0
            start = i + 1    
    print(finalPair)  
    for i in range(finalPair[0], finalPair[1] + 1):
        a[i] = -sys.maxsize-1
    print(a)
    return maxSoFar

def kLargestNonOverlappingSubArrays(a, k):
    result = [0] * k
    for i in range(k):
        result[i] = modifiedKadane(a)
    return result

a = [4, 1, 1, -1, -3, -5, 6, 2, -6, -2]
k = 3
print(kLargestNonOverlappingSubArrays(a, k))