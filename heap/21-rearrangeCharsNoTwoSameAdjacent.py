def maxHeapify(a, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and a[l][0] > a[largest][0]:
        largest = l
    if r < n and a[r][0] > a[largest][0]:
        largest = r
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

def rearrangeCharacters(inp):
    f = { x: inp.count(x) for x in inp }
    h = [[f[key], key] for key in f.keys()]
    maxHeap(h)
    result = ""
    lastChar = [-1, "#"]
    while len(h) > 0:
        currentChar = heapPop(h)
        result += currentChar[1]
        if lastChar[0] > 0:
            heapPush(h, lastChar)
        currentChar[0] -= 1
        lastChar = currentChar
    if len(inp) == len(result):
        return result
    else:
        return "Impossible"

inp = "aabbccddee"
print(rearrangeCharacters(inp))
        