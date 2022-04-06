'''
Given an array of positive distinct integers. We need to find the only element whose replacement 
with any other value makes array elements distinct consecutive. If it is not possible to make array 
elements consecutive, return -1.

Examples :

Input : arr[] = {45, 42, 46, 48, 47}
Output : 42
Explanation: We can replace 42 with either
44 or 48 to make array consecutive.

Input : arr[] = {5, 6, 7, 9, 10}
Output : 5 [OR 10]
Explanation: We can either replace 5 with 8
or 10 with 8 to make array elements 
consecutive.

Input : arr[] = {5, 6, 7, 9, 8}
Output : Already Consecutive
'''
from search import binarySearchUtil

def check(a):
    a.sort()
    n = len(a)
    missCount = 0
    for i in range(a[0] + 1, a[0] + n):
        if binarySearchUtil(a, 0, n - 1, i) == -1:
            missCount += 1
    if missCount == 0:
        return "Already Sorted"
    if missCount == 1:
        return a[n-1]
    missCount = 0
    for i in range(a[n-1] - 1, a[n-1] - n, -1):
        if binarySearchUtil(a, 0, n - 1, i) == -1:
            missCount += 1
    if missCount == 0:
        return "Already Sorted"
    if missCount == 1:
        return a[0]
    return -1

a = [5, 6, 7, 9, 8]
print(check(a))