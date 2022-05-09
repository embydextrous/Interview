'''
Given two integers 'n' and 'm', find all the stepping numbers in range [n, m]. 
A number is called stepping number if all adjacent digits have an absolute difference of 1. 
321 is a Stepping Number while 421 is not.

Examples : 

Input : n = 0, m = 21
Output : 0 1 2 3 4 5 6 7 8 9 10 12 21

Input : n = 10, m = 15
Output : 10, 12
'''
from collections import deque

def steppingNumbers(n, m):
    if m < 10:
        return [i for i in range(n, m + 1)]
    q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    result = []
    if n == 0:
        result.append(0)
    while True:
        x = q.popleft()
        if x >= n and x <= m:
            result.append(x)
        if x % 10 != 0:
            next = 10 * x + (x % 10 - 1)
            if next > m:
                break
            else:
                q.append(next)
        if x % 10 != 9:
            next = 10 * x + (x % 10 + 1)
            if next > m:
                break
            else:
                q.append(next)
    while len(q) > 0 and q[0] < n:
        q.popleft()
    result.extend(q)
    return result

print(steppingNumbers(100, 1000))