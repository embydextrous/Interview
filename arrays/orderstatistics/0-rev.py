from collections import Counter
from random import randint
from heapq import heappush, heapreplace, heappop, heapify

# 16, 20, 21, 23, 26
# 5, 10, 30
def kSmallestElements(a, k):
    n  =len(a)
    for i in range(k, n):
        maxindex = 0
        for j in range(1, k):
            if a[j] > a[maxindex]:
                maxindex = j
        x = a[maxindex]
        for j in range(maxindex, k):
            a[j] = a[j+1]
        a[i], a[k] = x, a[i]
    return a[:k]

# 3 1 9 2 7 4
    

a = [9, 3, 1, 7, 2, 4]
k = 3
print(kSmallestElements(a, k))



