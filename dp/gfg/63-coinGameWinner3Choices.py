'''
A and B are playing a game. At the beginning there are n coins. Given two more numbers x and y. In each move a player can pick x or y or 1 coins. 
A always starts the game. The player who picks the last coin wins the game or the person who is not able to pick any coin loses the game. For a given 
value of n, find whether A will win the game or not if both are playing optimally.

Examples: 

Input :  n = 5, x = 3, y = 4
Output : A
There are 5 coins, every player can pick 1 or
3 or 4 coins on his/her turn.
A can win by picking 3 coins in first chance.
Now 2 coins will be left so B will pick one 
coin and now A can win by picking the last coin.

Input : 2 3 4
Output : B
'''
def winner(n, x, y):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if dp[i-1] == 0:
            dp[i] = 1
        elif i >= x and dp[i-x] == 0:
            dp[i] = 1
        elif i >= y and dp[i-y] == 0:
            dp[i] = 1
    return dp[n]

n = 11
x = 3
y = 4
print(winner(n, x, y))