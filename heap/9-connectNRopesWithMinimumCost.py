import heapq

def connectRopes(a):
    heapq.heapify(a)
    cost = 0
    while len(a) > 1:
        l1, l2 = heapq.heappop(a), heapq.heappop(a)
        cost += l1 + l2
        heapq.heappush(a, l1 + l2)
    return cost

a = [4, 3, 2, 6]
print(connectRopes(a))
