from heap import buildMaxHeap
from heap import maxHeapify

def heapSort(a):
    n = len(a)
    buildMaxHeap(a)
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        maxHeapify(a, i, 0)

a = [9, 6, 1, 8, 7, 3, 5, 2, 4]
heapSort(a)
print(a)