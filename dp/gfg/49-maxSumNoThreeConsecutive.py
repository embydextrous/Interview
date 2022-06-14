'''
Given a sequence of positive numbers, find the maximum sum that can be formed which has no three consecutive elements present.
Examples : 

Input: arr[] = {1, 2, 3}
Output: 5
We can't take three of them, so answer is
2 + 3 = 5

Input: arr[] = {3000, 2000, 1000, 3, 10}
Output: 5013 
3000 + 2000 + 3 + 10 = 5013

Input: arr[] = {100, 1000, 100, 1000, 1}
Output: 2101
100 + 1000 + 1000 + 1 = 2101

Input: arr[] = {1, 1, 1, 1, 1}
Output: 4

Input: arr[] = {1, 2, 3, 4, 5, 6, 7, 8}
Output: 27
'''
def maxSum(a):
    n = len(a)
    if n == 0:
        return 0
    if n == 1:
        return a[0]
    if n == 2:
        return a[0] + a[1]
    x, y, z = 0, a[0], a[0] + a[1]
    for i in range(2, n):
        x, y, z = y, z, max(z, y + a[i], x + a[i] + a[i-1])
    return z

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(maxSum(a))