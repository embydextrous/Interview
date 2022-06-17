'''
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a 
given sequence such that all elements of the subsequence are sorted in increasing order. For example, 
the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
longest-increasing-subsequence

More Examples:

Input  : arr[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : arr[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input : arr[] = {50, 3, 10, 7, 40, 80}
Output : Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}
'''
# Variations 
# https://www.geeksforgeeks.org/longest-subsequence-such-that-difference-between-adjacents-is-one/
from collections import deque

def lis(a):
    dp = [1] * len(a)
    maxi = 1
    for i in range(1, len(a)):
        for j in range(i):
            if a[i] > a[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                maxi = max(maxi, dp[i])
    print(dp)
    return maxi

a = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis(a))

def constructLis(a):
    n = len(a)
    result = [deque() for i in range(n)]
    lis = []
    for i in range(0, n):
        for j in range(i):
            if a[i] > a[j] and len(result[j]) + 1 > len(result[i]) + 1:
                result[i] = result[j].copy()
        result[i].append(a[i])
        if len(result[i]) > len(lis):
            lis = result[i]
    return lis

print(constructLis(a))



    