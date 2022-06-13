'''

        20      30      2       10
20      20      30      22      40
30      X       30      30      32
2       X       X       2       10
10      X       X       X       10
'''
def getSum(pSum, i, j):
    if i == 0:
        return pSum[j]
    return pSum[j] - pSum[i-1]

def optimalStrategy(a):
    n = len(a)
    pSum = a[:]
    for i in range(1, n):
        pSum[i] += pSum[i-1]
    dp = [[a[i] if i == j else 0 for i in range(n)] for j in range(n)]
    for size in range(2, n + 1):
        for i in range(n - size + 1):
            j = i + size - 1
            dp[i][j] = getSum(pSum, i, j) - min(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]
    
a = [20, 30, 2, 10]
print(optimalStrategy(a))