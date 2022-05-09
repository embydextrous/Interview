from collections import Counter, deque
from heapq import heapify, heappop, heappush, heapreplace
from random import randint

# 12, 13, 17, 19, 20, 21, 22, 23
def minPossibleSum(a):
    n1 = n2 = 0
    heapify(a)
    while len(a) > 0:
        n1 = 10 * n1 + heappop(a)
        if len(a) > 0:
            n2 = 10 * n2 + heappop(a)
    return n1 + n2


print(minPossibleSum([5, 0, 7, 4, 3]))

