'''
Consider a highway of M miles. The task is to place billboards on the highway such that revenue is maximized.
The possible sites for billboards are given by number x1 < x2 < ….. < xn-1 < xn, specifying positions in 
miles measured from one end of the road. If we place a billboard at position xi, we receive a revenue of 
ri > 0. There is a restriction that no two billboards can be placed within t miles or less than it. 
Note : All possible sites from x1 to xn are in range from 0 to M as need to place billboards on a highway 
of M miles.
Examples: 
 

Input : M = 20
        x[]       = {6, 7, 12, 13, 14}
        revenue[] = {5, 6, 5,  3,  1}
        t = 5
Output: 10
By placing two billboards at 6 miles and 12
miles will produce the maximum revenue of 10.

Input : M = 15
        x[] = {6, 9, 12, 14}
        revenue[] = {5, 6, 3, 7}
        t = 2
Output : 18  
'''

def billboard(M, distance, revenue, t):
    dp = [0] * (M + 1)
    idx = 0
    for i in range(1, M + 1):
        if idx >= len(distance) or i < distance[idx]:
            dp[i] = dp[i-1]
        elif i == distance[idx]:
            if idx == 0:
                dp[i] = revenue[idx]
            else:
                if i - t > 0:
                    dp[i] = max(dp[i-1], dp[i-t-1] + revenue[idx])
                else:
                    dp[i] = revenue[idx]
            idx += 1
    return dp[M]

M = 15
distance = [6, 9, 12, 14]
revenue = [5, 6, 3, 7]
t = 2
print(billboard(M, distance, revenue, t))