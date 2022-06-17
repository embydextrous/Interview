'''
Given two arrays, find length of the longest common increasing subsequence [LCIS] and print one of such sequences (multiple sequences may exist)
Suppose we consider two arrays -
arr1[] = {3, 4, 9, 1} and 
arr2[] = {5, 3, 8, 9, 10, 2, 1}

Output - 2
'''
def lcis(a, b):
    n = len(a)
    m = len(b)
    dp = [0] * m
    for i in range(n):
        current = 0
        for j in range(m):
            print(a[i], b[j], current, dp[j])
            if a[i] == b[j]:
                if current + 1 > dp[j]:
                    dp[j] = current + 1
            if a[i] > b[j]:
                if dp[j] > current:
                    current = dp[j]
    return max(dp)

a = [3, 4, 9, 1]
b = [5, 3, 8, 9, 10, 2, 1]

print(lcis(a, b))
