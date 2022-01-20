# https://www.geeksforgeeks.org/minimum-sum-squares-characters-counts-given-string-removing-k-characters/
import heapq

def minimumSumOfSquares(s, k):
    # 1. find frequency of each element - value is -ve to simulate maxHeap
    d = { x : -1 * s.count(x) for x in s }
    values = list(d.values())
    # Build max heap
    heapq.heapify(values)
    # In each turn check if heap top
    # if heap top is 0 return 0
    # else remove 1 from top element and call heapify again
    for i in range(k):
        x = -values[0]
        if x == 0:
            return 0
        values[0] += 1
        heapq.heapify(values)
    sum = 0
    for i in range(len(values)):
        sum += values[i] ** 2
    return sum

s = "abbccc"
k = 3
print(minimumSumOfSquares(s, 3))



