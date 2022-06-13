'''
Input 
s = "Geeks for Geeks presents word wrap problem"
k = 15

Geeks for geeks
presents word
wrap problem

0 * 0 + 2 * 2 + 3 * 3 = 13
'''
INT_MAX = 10 ** 9

def length(preSum, i, j):
    if i == 0:
        return preSum[j] + j
    return preSum[j] - preSum[i-1] + (j - i)

def wordWrap(s, k):
    wL = [len(word) for word in s.split()]
    print(wL)
    n = len(wL)
    preSum = wL[:]
    for i in range(1, n):
        preSum[i] += preSum[i-1]
    cost = [[INT_MAX if i != j else (k - wL[i]) ** 2 for i in range(n)] for j in range(n)]
    for size in range(2, n + 1):
        for i in range(n - size + 1):
            j = i + size - 1
            l = length(preSum, i, j)
            if l <= k:
                cost[i][j] = (k - l) ** 2
    for row in cost:
        print(row)
    print()
    dp = [INT_MAX] * n
    dp[0] = cost[0][0]
    print(dp)
    for i in range(1, n):
        if cost[0][i] < INT_MAX:
            dp[i] = cost[0][i]
        else:
            for j in range(i):
                dp[i] = min(dp[i], dp[j] + cost[j+1][i])
    print(dp)

s = "Geeks for Geeks presents word wrap problem"
k = 15
print(wordWrap(s, k))
