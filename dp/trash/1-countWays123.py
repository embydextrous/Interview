'''
Given a distance 'dist', count total number of ways to cover the distance with 1, 2 and 3 steps.

Input: n = 3
Output: 4
Explanation:
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input: n = 4
Output: 7
Explanation:
Below are the four ways
 1 step + 1 step + 1 step + 1 step
 1 step + 2 step + 1 step
 2 step + 1 step + 1 step 
 1 step + 1 step + 2 step
 2 step + 2 step
 3 step + 1 step
 1 step + 3 step
'''
def count(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    a, b, c = 1, 1, 2
    for i in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c

n = 4
print(count(n))