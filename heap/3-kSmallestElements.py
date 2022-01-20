from heap import buildMaxHeap, maxHeapify

def kSmallestElements(a, k):
    h = a[:k]
    buildMaxHeap(h)
    for i in range(k, len(a)):
        if a[i] < h[0]:
            h[0] = a[i]
            maxHeapify(h, k, 0)
    return h

a = [14, 9, 22, 31, 3, 4, 11, 2, 7, 24, 31, 6]
print(kSmallestElements(a, 4))
print(sorted(a))