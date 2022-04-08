'''
Given an array of n integers, We need to find all pairs with difference less than k

Examples :  

Input : a[] = {1, 10, 4, 2}
        K = 3
Output : 2
We can make only two pairs 
with difference less than 3.
(1, 2) and (4, 2)

Input : a[] = {1, 8, 7}
        K = 7
Output : 2
Pairs with difference less than 7
are (1, 7) and (8, 7)
'''
# 1 3 5 7 9 11
def numPairs(a, x):
    n = len(a)
    a.sort()
    c = 0
    for i in range(n-1):
        key = x + a[i] - 1
        idx = floor(a, i + 1, n - 1, key)
        if idx != -1:
            c += idx - i
    return c

def floor(a, l, r, x):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if a[m] == x:
        return m
    if a[m] < x and (r == m or a[m+1] > x):
        return m
    if a[m] > x:
        return floor(a, l, m - 1, x)
    return floor(a, m + 1, r, x)

a = [1, 10, 4, 2]
print(numPairs(a, 3))
