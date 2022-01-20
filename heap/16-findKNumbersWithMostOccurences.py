def maxHeapify(a, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and (a[left][0] > a[largest][0] or (a[left][0] == a[largest][0] and a[left][1] > a[largest][1])):
        largest = left
    if right < n and (a[right][0] > a[largest][0] or (a[right][0] == a[largest][0] and a[right][1] > a[largest][1])):
        largest = right
    if largest != i:
        a[largest], a[i] = a[i], a[largest]
        maxHeapify(a, n, largest)

def maxHeap(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(a, n, i)

def heapPop(a):
    a[0], a[-1] = a[-1], a[0]
    maxHeapify(a, len(a) - 1, 0)
    return a.pop()

def heapPush(a, x):
    a.append(x)
    if len(a) == 1:
        return
    child = len(a) - 1
    parent = (child - 1) // 2
    while True:
        if a[parent][0] < a[child][0]:
            a[parent], a[child] = a[child], a[parent]
        if parent == 0:
            break
        child = parent
        parent = (child - 1) // 2
    print(a)

def findKNumbers(a, k):
    d = { x : a.count(x) for x in a }
    h = []
    for v in d.keys():
        heapPush(h, (d[v], v))
    print(h)
    for i in range(k):
        print(heapPop(h)[1], end = " ")
    print()

a = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
k = 4
findKNumbers(a, k)