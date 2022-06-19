'''
We have been given N balloons, each with a number of coins associated with it. On bursting a balloon i, the number of coins gained is equal to A[i-1]*A[i]*A[i+1]. 
Also, balloons i-1 and i+1 now become adjacent. Find the maximum possible profit earned after bursting all the balloons. Assume an extra 1 at each boundary.
Examples: 

Input : 5, 10
Output : 60
Explanation - First Burst 5, Coins = 1*5*10
              Then burst 10, Coins+= 1*10*1
              Total = 60

Input : 1, 2, 3, 4, 5
Output : 110
'''
def burstBalloons(a):
    n = len(a)
    a = [1] + a + [1]
    dp = [[0 for i in range(n+2)] for j in range(n+2)]
    for size in range(1, n+1):
        for i in range(1, n-size+2):
            j = i + size - 1
            for k in range(i, j+1):
                dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + a[i-1] * a[k] * a[j+1])
    for row in dp:
        print(row)
    return dp[1][n]

i = 0
j = 1
k = 0
a = [1, 2, 3, 4, 5]
print(burstBalloons(a))
