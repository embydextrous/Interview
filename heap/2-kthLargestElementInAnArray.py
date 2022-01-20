from heap import buildMinHeap, minHeapify

def kthLargestElement(a, k):
    h = a[:k]
    buildMinHeap(h)
    for i in range(k, len(a)):
        if a[i] > h[0]:
            h[0] = a[i]
            minHeapify(h, k, 0)
    return h[0]

a = [14, 9, 22, 31, 3, 4, 11, 2, 7, 24, 31, 6]
print(kthLargestElement(a, 4))
print(sorted(a))