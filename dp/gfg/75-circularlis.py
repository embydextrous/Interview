'''
Given an array, the task is to find to LIS (Longest Increasing Subsequence) in a circular way.
Examples : 
 

Input : arr[] = {5, 4, 3, 2, 1}
Output : 2
Although there is no LIS in a given array 
but in a circular form there can be
{1, 5}, {2, 5}, ...... 

Input : arr[]= {5, 6, 7, 1, 2, 3}
Output : 6
{1, 2, 3, 5, 6, 7} will be the LIS in the
circular manner.
'''
def lis(a, k):
    n = len(a)
    dp = [1] * n
    maxi = dp[0]
    for i in range(k, k+n):
        for j in range(k, i):
            if a[i%n] > a[j%n] and dp[j%n] + 1 > dp[i%n]:
                dp[i%n] = dp[j%n] + 1
                maxi = max(maxi, dp[i%n])
    print(dp)
    return maxi

def circularlis(a):
    maxi = 0
    n = len(a)
    for i in range(n):
        maxi = max(maxi, lis(a, i))
    return maxi

a = [5, 6, 7, 1, 2, 3]
print(circularlis(a))