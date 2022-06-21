'''
Given a number K, and N bars of height from 1 to N, the task is to find the number of ways to arrange the N bars such that only K bars are visible from 
the left.

Examples: 

    Input: N=4, K=3
    Output:
    6
    Explanation: The 6 permutations where only 3 bars are visible from the left are:

        1 2 4 3
        1 3 2 4
        1 3 4 2
        2 1 3 4
        2 3 1 4
        2 3 4 1

    The Underlined bars are not visible.

    Input: N=5, K=2
    Output:
    50
'''

'''
From the given n numbers, the largest number will be n. so last position can be filled any of given numbers.if we fill last position with largest number, 
then using remaining n - 1 numbers we have to create combinations with k - 1 visible sticks from left, because largest number always contributes to visible 
item.
Thats the reason we have first part as db[n - 1][k - 1] as we only need to arrange remaining n - 1 sticks with k - 1 visible sticksif we fill last position
with any other(not largest) number then, that number will be definately smaller than largest number and it is not visible from left. so we have n - 1 such
numbers, and no difference in k as that number will not be visible from left.
Thats the reason we have second part as = (n - 1) * db[n - 1][k]
'''
def numWays(n, k):
    if k == 0:
        return 0
    if n == 0:
        return 1
    dp = [[0 for i in range(k+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, k+1):
            dp[i][j] = dp[i-1][j-1] + (i-1) * dp[i-1][j]
    for row in dp:
        print(row)
    return dp[n][k]

n = 5
k = 2
print(numWays(5, 2))