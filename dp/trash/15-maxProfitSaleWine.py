'''
Given n wines in a row, with integers denoting the cost of each wine respectively. Each year you can sale the 
first or the last wine in the row. However, the price of wines increases over time. Let the initial profits 
from the wines be P1, P2, P3…Pn. On the Yth year, the profit from the ith wine will be Y*Pi. For each year, 
your task is to print “beg” or “end” denoting whether first or last wine should be sold. Also, calculate the 
maximum profit from all the wines.
Examples : 
 
Input: Price of wines: 2 4 6 2 5
Output: beg end end beg beg 
         64
Explanation :
'''
def maxProfitUtil(a, start, end, y, c, dp):
    c[0] += 1
    if start == end:
        return y * a[start]
    if dp[start][end][y] != -1:
        return dp[start][end][y]
    dp[start][end][y] = max(y * a[start] + maxProfitUtil(a, start + 1, end, y + 1, c, dp), y * a[end] + maxProfitUtil(a, start, end - 1, y + 1, c, dp))
    return dp[start][end][y]

a = [2, 4, 6, 2, 5, 3, 5, 2, 1, 4, 6, 3,2,4, 1]
c = [0]
n = len(a)
dp = [[[-1 for i in range(n+1)] for j in range(n)] for j in range(n)]
print(maxProfitUtil(a, 0, len(a) - 1, 1, c, dp)) 
print(c[0])