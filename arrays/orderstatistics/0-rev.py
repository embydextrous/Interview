from collections import Counter
from random import randint
from heapq import heappush, heapreplace, heappop, heapify

# 14, 16, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29
# 5, 10, 30
def maxDiff(a):
    mini = a[0]
    maxDiff = 0
    for i in a:
        if i < mini:
            mini = i
        else:
            maxDiff = max(maxDiff, i - mini)
    return maxDiff

a = [4, 8, 1, 9, 7, 2, 11]
print(maxDiff(a))



