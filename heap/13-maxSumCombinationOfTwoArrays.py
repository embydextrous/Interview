# https://www.geeksforgeeks.org/k-maximum-sum-combinations-two-arrays/

def maxHeapify(a, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and a[left][0] > a[largest][0]:
        largest = left
    if right < n and a[right][0] > a[largest][0]:
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

def maxSumCombination(a, b, k):
    a.sort()
    b.sort()
    result = []
    i, j = len(a) - 1, len(b) - 1
    heapPush(result, (a[i] + b[j], i, j))
    indexSet = set()
    indexSet.add((i, j))
    for i in range(k):
        #print(result, end = " ")
        (s, _i, _j) = heapPop(result)
        print(s, end = " ")
        if _j > 0 and (_i, _j-1) not in indexSet:
            heapPush(result, (a[_i] + b[_j-1], _i, _j-1))
            indexSet.add((_i, _j-1))
        if _i > 0 and (_i-1, _j) not in indexSet:
            heapPush(result, (a[_i-1] + b[_j], _i-1, _j))
            indexSet.add((_i-1, _j))
    print()

a = [4, 2, 5, 1]
b = [8, 0, 3, 5]
k = 3
maxSumCombination(a, b, 14)

# 0 3 5 8
# 1 2 4 5

# 13 12 10 10 9 9 8 7 7 6 5 5 4 4 2 1

# 13 12 10
