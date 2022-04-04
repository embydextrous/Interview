def linearSearch(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

def binarySearch(arr, x):
    return binarySearchUtil(arr, 0, len(arr) - 1, x)

def binarySearchUtil(arr, l, r, x):
    if l > r:
        return -1
    mid = l + (r - l) // 2
    if arr[mid] == x:
        return mid
    if arr[mid] > x:
        return binarySearchUtil(arr, l, mid - 1, x)
    return binarySearchUtil(arr, mid + 1, r, x)

def binarySearchIterative(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1

