from heapq import heapify, heappop, heappush

def mergeKSortedArrays(arrs, k):
    indexes = [0] * k
    h = []
    result = []
    for i in range(k):
        if len(arrs[i]) > 0:
            h.append([arrs[i][0], i])
    heapify(h)
    while len(h) > 0:
        x, i = heappop(h)
        result.append(x)
        indexes[i] += 1
        if indexes[i] < len(arrs[i]):
            heappush(h, [arrs[i][indexes[i]],i])
    return result

a = [[2, 4], [], [1, 2, 3, 4], [2, 4, 5], [1, 3, 6, 8]]
print(mergeKSortedArrays(a, 5))


