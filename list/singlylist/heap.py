def maxHeapify(arr, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * (i + 1)
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        maxHeapify(arr, n, largest)

def minHeapify(arr, n, i):
    smallest = i
    l, r = 2 * i + 1, 2 * (i + 1)
    if l < n and arr[l] < arr[smallest]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        minHeapify(arr, n, smallest)

def popMinHeap(minHeap):
    minHeap[0], minHeap[len(minHeap) - 1] = minHeap[len(minHeap) - 1], minHeap[0]
    v = minHeap.pop()
    minHeapify(minHeap, len(minHeap), 0)

def replaceMinHeap(minHeap, v):
    r, minHeap[0] = minHeap[0], v
    minHeapify(minHeap, len(minHeap), 0)
    return r

def buildMaxHeap(arr):
    n = len(arr)
    # index of last non-leaf node
    s = n // 2 - 1
    for i in range(s, -1, -1):
        maxHeapify(arr, n, i)

def buildMinHeap(arr):
    n = len(arr)
    # index of last non-leaf node
    s = n // 2 - 1
    for i in range(s, -1, -1):
        minHeapify(arr, n, i)

