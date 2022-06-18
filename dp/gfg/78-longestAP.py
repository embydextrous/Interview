'''
Given a sorted set of numbers, find the Length of the Longest Arithmetic Progression (LLAP) in it. 

Examples: 

set[] = {1, 7, 10, 15, 27, 29}
output = 3
The longest arithmetic progression is {1, 15, 29}

set[] = {5, 10, 15, 20, 25, 30}
output = 6
The whole set is in AP
'''
# Also see, https://www.geeksforgeeks.org/longest-geometric-progression/

def llap(a):
    n = len(a)
    if n < 3:
        return n
    dp = [[2 if j > i else -1 for j in range(n)] for i in range(n)]
    maxi = 2
    for j in range(n - 1, 0, -1):
        i = j - 1
        k = j + 1
        while i >= 0 and k < n:
            if a[i] + a[k] == 2 * a[j]:
                dp[i][j] = 1 + dp[j][k]
                maxi = max(maxi, dp[i][j])
                i -= 1
                k += 1
            elif a[i] + a[k] < 2 * a[j]:
                dp[i][j] = 2
                k += 1
            else:
                dp[i][j] = 2
                i -= 1
    for row in dp:
        print(row)
    return maxi

a = [5, 7, 10, 15, 20, 29]
print(llap(a))

