'''
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with 
sum equal to given sum. 

Example: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.

Form an array dp of length sum + 1, dp[0] = 0 (empty set case)
For each element start from right and if dp[right - element] = 1 set dp[right] = 1
Why start from right?
To avoid false positives. For ex let's first entry be 3, dp[3] = 1
Now, second element is 4 which makes dp[4] = 1 and dp[7] = 1. But it will also make dp[10] = 1 as dp[7] 
and dp[3] both are 1. So, start with last till element as higher element will be encountered before to
avoid any false positives.
'''
def subsetSum(a, x):
    dp = [False] * (x + 1)
    dp[0] = True
    for i in a:
        for j in range(x, i - 1, -1):
            if dp[j-i]:
                dp[j] = True
    print(dp)
    return dp[x]

a = [3, 4, 3, 5]
x = 20
print(subsetSum(a, x))