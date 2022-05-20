'''
Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of 
the given array such that the integers in the subsequence are sorted in increasing order. For example,
 if input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100), if the input array
  is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10) and if the input array is {10, 5, 4, 3},
   then output should be 10
'''
def mis(a):
    n = len(a)
    dp = [a[i] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and dp[j] + a[i] > dp[i]:
                dp[i] = dp[j] + a[i]
    return max(dp)

a = [2, 3, 5, 3, 4, 7, 6, 7, 8]
print(mis(a))
