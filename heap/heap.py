# https://www.geeksforgeeks.org/why-is-binary-heap-preferred-over-bst-for-priority-queue/

def maxHeapify(a, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[largest], a[i] = a[i], a[largest]
        maxHeapify(a, n, largest)

# Time Complexity is O(n)
def buildMaxHeap(a):
    n = len(a)
    # https://www.geeksforgeeks.org/leaf-starting-point-binary-heap-data-structure/ (n//2 is first leaf and n//2 - 1 is first non-leaf node)
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(a, n, i)

def minHeapify(a, n, i):
    smallest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and a[left] < a[smallest]:
        smallest = left
    if right < n and a[right] < a[smallest]:
        smallest = right
    if smallest != i:
        a[smallest], a[i] = a[i], a[smallest]
        minHeapify(a, n, smallest)

def buildMinHeap(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        minHeapify(a, n, i)