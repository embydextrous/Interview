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
def subsetModuloSum(a, m):
    dp = [False for i in range(m)]
    for i in a:
        temp = dp[:]
        if i % m == 0:
            return True
        for j in range(m):
            if j == i % m:
                temp[j] = True
            elif dp[j] == True:
                temp[(j + i % m) % m] = True
        dp = temp
    print(dp)
    return dp[0]

a = [3, 1, 7, 5]
m = 15
print(subsetModuloSum(a, m))
