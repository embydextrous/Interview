from collections import Counter
import heapq

def maxDistinctElements(a, k):
    d = Counter(a)
    h = []
    countOnes = 0
    for key in d:
        if d[key] > 1:
            heapq.heappush(h, d[key])
        else:
            countOnes += 1
    while k > 0:
        if len(h) > 0:
            x = heapq.heappop(h)
            if x == 2:
                countOnes += 1
            else:
                heapq.heappush(h, x - 1)
        else:
            countOnes -= 1
        k -= 1
    result = countOnes
    while len(h) > 0:
        if heapq.heappop(h) == 1:
            result += 1
    return result

a = [5, 7, 5, 5, 1, 2, 2]
k = 3
print(maxDistinctElements(a, 1))