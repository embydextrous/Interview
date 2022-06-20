'''
There are N employees in a company, and each employee has some ratings. The employees are given a hike in their salary
based on their ratings, i.e., employees with higher ratings will get a higher hike in their salary. An employee only
knows the hike and rating of its neighbors i.e., on the left and right side of the employee. 
Given an array arr[] of N positive integers which denotes the ratings of N employees, the task is to find the minimum
hike that should be raised for each employee, such that no employee feels unfair.

Note: The hikes are positive integers only and the ratings are always greater than zero.

Example: 

    Input: arr[] = {1, 3, 5, 4} 
    Output: 1 2 3 1 
    Explanation: 
    The distribution of minimum hike for each employee must be: 
    1 + 2 + 3 + 1 = 7

    Input: arr[] = {5, 3, 4, 2, 1, 6} 
    Output: 2 1 3 2 1 2 
    Explanation: 
    The distribution of minimum hike for each employee must be: 
    2 + 1 + 3 + 2 + 1 + 2 = 11 
'''
def minHike(a):
    n = len(a)
    dp = [1] * n
    for i in range(1, n):
        if a[i] > a[i-1]:
            dp[i] = 1 + dp[i-1]
    for i in range(n-2, -1, -1):
        if a[i] > a[i+1]:
            dp[i] = max(dp[i], 1 + dp[i+1])
    print(dp)
    return sum(dp)

a = [1, 3, 5, 4]
print(minHike(a))