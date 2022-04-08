from random import randint

# Time Complexity - O(nlogn) for all cases.
# T(n) = 2T(n/2) + θ(n)
# Stable Yes
# Usually used in external sorting
def maxHeapify(a, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        maxHeapify(a, n, largest)

def buildMaxHeap(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(a, n, i)

def heapSort(a):
    n = len(a)
    buildMaxHeap(a)
    for i in range(n-1, -1, -1):
        a[0], a[i] = a[i], a[0]
        maxHeapify(a, i, 0)

a = [randint(1, 20) for i in range(10)]
print(a)
heapSort(a)
print(a)