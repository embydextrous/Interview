'''
Given an array of n integers, find the 3 elements such that a[i] < a[j] < a[k] and i < j < k in 0(n) time. 
If there are multiple such triplets, then print any one of them.

Examples:  

Input: arr[] = {12, 11, 10, 5, 6, 2, 30}
Output: 5, 6, 30
Explanation: As 5 < 6 < 30, and they 
appear in the same sequence in the array 

Input: arr[] = {1, 2, 3, 4}
Output: 1, 2, 3 OR 1, 2, 4 OR 2, 3, 4
Explanation: As the array is sorted, for every i, j, k,
where i < j < k, arr[i] < arr[j] < arr[k] 

Input: arr[] = {4, 3, 2, 1}
Output: No such triplet exists.
'''
def findTriplet(a):
    n = len(a)
    leftMin = [-1 for i in range(n)]
    rightMax = [-1 for i in range(n)]
    for i in range(n):
        if i == 0:
            leftMin[i] = a[i]
        else:
            leftMin[i] = min(leftMin[i-1], a[i])
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            rightMax[i] = a[i]
        else:
            rightMax[i] = max(rightMax[i+1], a[i])
    for i  in range(1, n - 1):
        if a[i] > leftMin[i] and a[i] < rightMax[i]:
            return (leftMin[i], a[i], rightMax[i])
    return None

a = [12, 11, 10, 5, 6, 2, 30]
print(findTriplet(a))