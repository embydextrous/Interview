'''
Given an array arr[] of integers and an integer K, the task is to print all subsets of the given array with the sum equal to the given target K.
Examples: 
 
Input: arr[] = {5, 10, 12, 13, 15, 18}, K = 30
Output: {12, 18}, {5, 12, 13}, {5, 10, 15}
Explanation: 
Subsets with sum 30 are:
12 + 18 = 30
5 + 12 + 13 = 30
5 + 10 + 15 = 30

Input: arr[] = {1, 2, 3, 4}, K = 5
Output: {2, 3}, {1, 4}
'''
from collections import deque


def perfectSum(a, x):
    n = len(a)
    dp = [[False for i in range(x + 1)] for j in range(n+1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        k = a[i-1]
        for j in range(x+1):
            if j < k:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-k]
    printUtil(a, dp, n, x, deque())

def printUtil(a, M, x, y, path):
    if x < 0 or y < 0:
        return
    if not M[x][y]:
        return
    if x == 0 and y == 0:
        print(path)
    printUtil(a, M, x - 1, y, path)
    path.appendleft(a[x-1])
    printUtil(a, M, x - 1, y - a[x-1], path)
    path.popleft()

a = [1, 2, 3, 4]
x = 5
perfectSum(a, x)

