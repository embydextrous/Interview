def eggDrop(n, k):
    dp = [[10 ** 9  if i != 0 and j != 0 else 0 for i in range(n+1)] for j in range(k+1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if i == 1:
                dp[i][j] = j
            elif j == 1:
                dp[i][j] = 1
            else:
                for x in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][x-1], dp[i][j-x]))
    for row in dp:
        print(row)
    return dp[k][n]

n = 200
k = 5
print(eggDrop(n, k))

'''
0   1   2   3   4   5
1   2   2   3   3   3
1   2   3   3   3   4
'''
