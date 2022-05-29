import sys

# 11, 6, 18, 5, 15, 10
'''
            11
          /    \ 
         6      13  
        /       /   
       5       12
'''
from collections import deque

def check(level):
    n = len(level)
    if n == 0:
        return True
    MIN = -sys.maxsize-1
    MAX = sys.maxsize
    q = deque([(level[0], MIN, MAX)])
    i = 1
    while i < n and len(q) > 0:
        print(q)
        (data, low, high) = q.popleft()
        if level[i] < data:
            if level[i] >= low:
                q.append((level[i], low, data - 1))
                i += 1
        if i < n and level[i] > data:
            if level[i] <= high:
                q.append((level[i], data + 1, high))
                i += 1
    return i == n

level = [11, 6, 13, 5, 12, 10]
print(check(level))
