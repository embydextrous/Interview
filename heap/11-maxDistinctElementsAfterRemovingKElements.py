import heapq

def maxDistinctElements(a, k):
    d = { x : -1 * a.count(x) for x in a }
    h = list(d.values())
    heapq.heapify(h)
    for i in range(k):
        if h[0] == 0:
            return 0
        h[0] += 1
        heapq.heapify(h)
    c = 0
    for f in h:
        if f != 0:
            c += 1
    return c

a = [5, 7, 5, 5, 1, 2, 2]
k = 3
print(maxDistinctElements(a, 4))