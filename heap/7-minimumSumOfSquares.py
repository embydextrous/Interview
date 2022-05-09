# https://www.geeksforgeeks.org/minimum-sum-squares-characters-counts-given-string-removing-k-characters/
from collections import Counter
import heapq

def minimumSumOfSquares(s, k):
    d = Counter(s)
    h = []
    for key in d:
        heapq.heappush(h, -d[key])
    for i in range(k):
        x = heapq.heappop(h) * -1
        if x > 1:
            heapq.heappush(h, (x - 1) * -1)
    sum = 0
    while len(h) > 0:
        sum += heapq.heappop(h) ** 2
    return sum

s = "abbccc"
k = 3
print(minimumSumOfSquares(s, 3))



