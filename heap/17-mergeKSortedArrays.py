import heapq

def mergeKSortedArrays(arrays, k):
    h = []
    for i in range(k):
        if len(arrays[i]) > 0:
            heapq.heappush(h, arrays[i][0])
    arrayIndexes = [0] * k
    result = []
    while len(h) > 0:
        x = heapq.heappop(h)
        result.append(x)
        for i in range(k):
            if arrayIndexes[i] < len(arrays[i]) and x == arrays[i][arrayIndexes[i]]:
                arrayIndexes[i] += 1
                if arrayIndexes[i] < len(arrays[i]):
                    heapq.heappush(h, arrays[i][arrayIndexes[i]])
                break
    return result

a = [[2, 4], [], [1, 2, 3, 4], [2, 4, 5], [1, 3, 6, 8]]
print(mergeKSortedArrays(a, 5))


