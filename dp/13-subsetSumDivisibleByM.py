'''
Given a set of non-negative distinct integers, and a value m, determine if there is a subset of the given 
set with sum divisible by m. 

Input : arr[] = {3, 1, 7, 5};
        m = 6;
Output : YES

Input : arr[] = {1, 6};
        m = 5;
Output : NO
'''
# Variation of last problem
def subsetModuloSum(a, k):
    temp = [0] * k
    dp = [0] * k
    for x in a:
        if x % k == 0:
            return True
        if dp[k - x % k] == 1:
            return True
        temp[x % k] = 1
        for j in range(k):
            if dp[j] == 1:
                temp[(x + j) % k] = 1
        for i in range(k):
            if temp[i] == 1:
                dp[i] = 1
                temp[i] = 0
        print(dp)
    return dp[0] == 1

a = [3, 1, 7, 5]
m = 16
print(subsetModuloSum(a, m))