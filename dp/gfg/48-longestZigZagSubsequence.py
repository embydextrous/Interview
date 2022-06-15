'''
The longest Zig-Zag subsequence problem is to find length of the longest subsequence of given sequence such that all elements of this are alternating. 
If a sequence {x1, x2, .. xn} is alternating sequence then its element satisfy one of the following relation : 

  x1 < x2 > x3 < x4 > x5 < …. xn or 
  x1 > x2 < x3 > x4 < x5 > …. xn 

Examples :

Input: arr[] = {1, 5, 4}
Output: 3
The whole arrays is of the form  x1 < x2 > x3 

Input: arr[] = {1, 4, 5}
Output: 2
All subsequences of length 2 are either of the form 
x1 < x2; or x1 > x2

Input: arr[] = {10, 22, 9, 33, 49, 50, 31, 60}
Output: 6
The subsequences {10, 22, 9, 33, 31, 60} or
{10, 22, 9, 49, 31, 60} or {10, 22, 9, 50, 31, 60}
are longest Zig-Zag of length 6.
'''
def lzs(a):
    maxi = 1
    n = len(a)
    dp = [[1, 1] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and 1 + dp[j][1] > dp[i][0]:
                dp[i][0] = 1 + dp[j][1]
                maxi = max(maxi, dp[i][0])
            elif a[i] < a[j] and 1 + dp[j][0] > dp[i][1]:
                dp[i][1] = 1 + dp[j][0]
                maxi = max(maxi, dp[i][1])
    return maxi

def mzs(a):
    maxi = a[0]
    n = len(a)
    dp = [[a[i], a[i]] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and a[i] + dp[j][1] > dp[i][0]:
                dp[i][0] = a[i] + dp[j][1]
                maxi = max(maxi, dp[i][0])
            elif a[i] < a[j] and a[i] + dp[j][0] > dp[i][1]:
                dp[i][1] = a[i] + dp[j][0]
                maxi = max(maxi, dp[i][1])
    return maxi

a = [10, 22, 9, 33, 49, 50, 31, 60]
print(lzs(a))
print(mzs(a))
'''
10  32  9   55  82  99  53   190
10  22  19  33  49  50  130  60
'''
