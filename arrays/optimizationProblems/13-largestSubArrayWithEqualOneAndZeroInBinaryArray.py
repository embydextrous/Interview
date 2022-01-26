# https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/

'''
Given an array containing only 0s and 1s, find the largest subarray which contains equal no of 0s and 1s. 
The expected time complexity is O(n). 

Examples: 

Input: arr[] = {1, 0, 1, 1, 1, 0, 0}
Output: 1 to 6 
(Starting and Ending indexes of output subarray)

Input: arr[] = {1, 1, 1, 1}
Output: No such subarray

Input: arr[] = {0, 0, 1, 1, 0}
Output: 0 to 3 Or 1 to 4
'''
from re import A


def maxSubarraySize(a):
    n = len(a)
    # Convert all 0's to -1 to make things easy
    for i in range(n):
        if a[i] == 0:
            a[i] = -1

    # Calculate sum of left elements including this
    cSum = [0] * n
    cSum[0] = a[0]
    for i in range(1, n):
        cSum[i] = cSum[i-1] + a[i]

    # Case 1 - If starting element is part
    maxCase1 = 0
    for i in range(n - 1, -1, -1):
        if cSum[i] == 0:
            maxCase1 = n - 1
            break
    
    # Case 2 - If Starting Element is not part
    maxCase2 = 0
    d = {}
    for i in range(n):
        if cSum[i] not in d:
            cSum[i] = d
        else:
            maxCase2 = (maxCase2, i - d[i])
    return max(maxCase1, maxCase2)

a = [0, 0, 1, 1, 0]
print(maxSubarraySize(a))