'''
Given an integer N and a 2D array cost[][3], where cost[i][0], cost[i][1], and cost[i][2] is the cost of painting ith house with colors red, blue, and 
green respectively, the task is to find the minimum cost to paint all the houses such that no two adjacent houses have the same color.

Examples:

    Input: N = 3, cost[][3] = {{14, 2, 11}, {11, 14, 5}, {14, 3, 10}}
    Output: 10
    Explanation: 
    Paint house 0 as blue. Cost = 2. Paint house 1 as green. Cost = 5. Paint house 2 as blue. Cost = 3.
    Therefore, the total cost = 2 + 5 + 3 = 10.

    Input: N = 2, cost[][3] = {{1, 2, 3}, {1, 4, 6}}
    Output: 3
'''
def minCost(a):
    r, g, b = a[0]
    n = len(a)
    for i in range(1, n):
        r, g, b = a[i][0] + min(g, b), a[i][1] + min(r, b), a[i][2] + min(r, g)
    return min(r, g, b)

a = [[1, 2, 3], [1, 4, 6]]
print(minCost(a))