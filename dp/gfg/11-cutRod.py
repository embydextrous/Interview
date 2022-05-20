'''
Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller 
than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, 
if the length of the rod is 8 and the values of different pieces are given as the following, then the maximum 
obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
'''
def cutRod(a):
    n = len(a)
    dp =  [a[i] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if dp[j] + dp[i-j-1] > dp[i]:
                dp[i] = dp[i-j-1] + dp[j]
    print(dp)
    return max(dp)

a = [3, 5, 8, 9, 10, 17, 17, 20]
print(cutRod(a))

