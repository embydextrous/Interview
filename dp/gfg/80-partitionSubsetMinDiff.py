'''
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) - sum(Subset2)) 
should be minimum.

Example: 

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11        
'''
def minDiff(a):
    m = sum(a)
    dp = [False for i in range(m//2 + 1)]
    dp[0] = True
    for i in a:
        for j in range(m//2, i - 1, -1):
            if dp[j-i]:
                dp[j] = True
    for i in range(m // 2, -1, -1):
        if dp[i]:
            return m - 2 * i

a = [1, 6, 11, 5]
print(minDiff(a))