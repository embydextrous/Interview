'''
Partition problem is to determine whether a given set can be partitioned into two subsets such that 
the sum of elements in both subsets is the same. 

Examples: 

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.
'''
def subsetSum(a, x):
    dp = [False] * (x + 1)
    dp[0] = True
    for i in a:
        for j in range(x, i - 1, -1):
            if dp[j-i]:
                dp[j] = True
    return dp[x]

def partitionProblem(a):
    sum = 0
    for i in a:
        sum += i
    if sum % 2 == 1:
        return False
    return subsetSum(a, sum // 2)

a = [1, 5, 3]
print(partitionProblem(a))