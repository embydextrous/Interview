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
    dp = [0 for i in range(M+1)]
    for i in range(len(distance)):
        x = distance[i]
        if i == 0:
            dp[x] = revenue[i]
        else:
            for j in range(distance[i-1] + 1, distance[i]):
                dp[j] = dp[j-1]
            if x - t > distance[i-1]:
                dp[x] = dp[x-1] + revenue[i]
            else:
                dp[x] = max(dp[x-1], dp[x-t-1] + revenue[i])
    print(dp)
    return dp[min(distance[-1], M)]

M = 15
distance = [6, 9, 12, 14]
revenue = [5, 6, 3, 7]
t = 2
print(billboard(M, distance, revenue, t))