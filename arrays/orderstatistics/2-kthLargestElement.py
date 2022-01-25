import heapq

# Also, see K Largest ELements (Simply return h and not h[0])

def kthLargestElement(a, k):
    h = a[:k]
    heapq.heapify(h)
    for i in range(k, len(a)):
        if a[i] > h[0]:
            heapq.heappushpop(h, a[i])
    return (h, h[0])

a = [7, 10, 4, 3, 20, 15]
print(kthLargestElement(a, 4))