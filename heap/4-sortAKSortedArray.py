from heap import minHeapify, buildMinHeap

def sort(a, k):
    n = len(a)
    h = a[:k+1]
    buildMinHeap(h)
    for i in range(n-k-1):
        a[i] = h[0]
        h[0] = a[i + k + 1]
        minHeapify(h, k + 1, 0)
    for i in range(k+1):
        a[n - k - 1 + i] = h[0]
        h[0], h[k-i] = h[k-i], h[0]
        minHeapify(h, k - i, 0)

a = [10, 9, 8, 7, 4, 70, 60, 50]
sort(a, 4)
print(a)
