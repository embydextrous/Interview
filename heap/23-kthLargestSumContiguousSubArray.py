def minHeapify(a, n, i):
    smallest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and a[l][0] < a[smallest][0]:
        smallest = l
    if r < n and a[r][0] < a[smallest][0]:
        smallest = r
    if smallest != i:
        a[smallest], a[i] = a[i], a[smallest]
        minHeapify(a, n, smallest)

def maxHeap(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        minHeapify(a, n, i)

def heapPop(a):
    a[0], a[-1] = a[-1], a[0]
    minHeapify(a, len(a) - 1, 0)
    return a.pop()

def heapPush(a, x):
    a.append(x)
    print(a)
    if len(a) == 1:
        return
    child = len(a) - 1
    parent = (child - 1) // 2
    while True:
        if a[parent][0] > a[child][0]:
            a[parent], a[child] = a[child], a[parent]
        if parent == 0:
            break
        child = parent
        parent = (child - 1) // 2  

def subArraySum(preSum, i, j):
    if i == 0:
        return preSum[j]
    return preSum[j] - preSum[i-1]

def kthLargestSumSubArray(a, k):
    preSum = [x for x in a]
    for i in range(1, len(a)):
        preSum[i] = preSum[i - 1] + preSum[i]
    h = []
    for i in range(len(a)):
        for j in range(i, len(a)):
            if len(h) < k:
                heapPush(h, [subArraySum(preSum, i, j), i, j])
            else:
                if subArraySum(preSum, i, j) > h[0][0]:
                    heapPop(h)
                    heapPush(h, [subArraySum(preSum, i, j), i, j])
    (s, i, j) = h[0]
    return (s, a[i:j+1])

a = [10, -10, 20, -40]
print(kthLargestSumSubArray(a, 2))

# 20 20 10 10 0 -10 -20 -20 -30 -40