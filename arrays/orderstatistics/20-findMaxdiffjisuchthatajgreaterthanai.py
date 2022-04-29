# https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/

'''
Given an array arr[], find the maximum j - i such that arr[j] > arr[i].

Examples : 

  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

  34 8 8 3 2 2 2 2 1
  80 80 80 80 80 80 33 33 1
  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
  Output: 8 ( j = 8, i = 0)

  Input:  {1, 2, 3, 4, 5, 6}
  Output: 5  (j = 5, i = 0)

  Input:  {6, 5, 4, 3, 2, 1}
  Output: -1 
'''
def findMaxDiff(a):
    n = len(a)
    lMin = [a[i] for i in range(n)]
    rMax = [a[i] for i in range(n)]
    for i in range(1, n):
        lMin[i] = min(lMin[i], lMin[i-1])
    for i in range(n-2, -1, -1):
        rMax[i] = max(rMax[i], rMax[i+1])
    i, j = 0, 0
    maxDiff = -1
    while i < n and j < n:
        if lMin[i] <= rMax[j]:
            maxDiff = max(maxDiff, j - i)
            j += 1
        else:
            i += 1
    return maxDiff

a = [34, 8, 10, 3, 2, 80, 30, 33, 1]
print(findMaxDiff(a))