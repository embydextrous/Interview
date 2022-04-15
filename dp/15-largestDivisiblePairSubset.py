'''
Given an array of n distinct elements, find length of the largest subset such that every pair in the subset 
is such that the larger element of the pair is divisible by smaller element. 

Examples: 

Input : arr[] = {10, 5, 3, 15, 20} 
Output : 3 
Explanation: The largest subset is 10, 5, 20.
10 is divisible by 5, and 20 is divisible by 10.

Input : arr[] = {18, 1, 3, 6, 13, 17} 
Output : 4
Explanation: The largest subset is 18, 1, 3, 6,
In the subsequence, 3 is divisible by 1, 
6 by 3 and 18 by 6.
'''
def largestSubset(a):
    n = len(a)
    a.sort()
    dp = [1] * n
    # dp[i] denotes subset if largest element is this and only smaller elements are to be picked up.
    for i in range(1, n):
        for j in range(i):
            if a[i] % a[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    print(dp)
    return max(dp)

'''
1 1 0 0 0 0 0 0 0 0 0
1 1 1 1 0 0 0 0 0 0 0
1 1 1 2 1 1 1 0 0 0 0
1 1 1 2 2 2 2 2 1 1 1
1 1 1 2 2 3 3 3 3 3 3
'''

a = [18, 1, 3, 6, 13, 17]
print(largestSubset(a))