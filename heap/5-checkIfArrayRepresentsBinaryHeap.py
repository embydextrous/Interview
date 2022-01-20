def checkIfArrayRepresentsBinaryMaxHeap(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and a[left] > a[i]:
            return False
        if right < n and a[right] > a[i]:
            return False
    return True

a = [90, 15, 10, 7, 16, 2]
print(checkIfArrayRepresentsBinaryMaxHeap(a))