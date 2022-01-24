def checkSortedAndRotated(a):
    n = len(a)
    minIndex = 0
    for i in range(1, n):
        if a[i] < a[minIndex]:
            minIndex = i
    # Definitely not rotated
    if i == 0:
        return False
    # Definitely not sorted
    if a[0] < a[-1]:
        return False
    # Check if two parts are sorted
    for i in range(minIndex - 1):
        if a[i] > a[i+1]:
            return False
    for i in range(minIndex, n - 1):
        if a[i] > a[i+1]:
            return False
    return True

a = [6, 7, 8, 1, 2, 3, 4, 5]
print(checkSortedAndRotated(a))
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(checkSortedAndRotated(a))
a = [5, 7, 8, 1, 2, 3]
print(checkSortedAndRotated(a))