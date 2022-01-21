# Also see https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/ - pivot + 1 (also satisfies no rotation case)
# Also see https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/ - a[pivot + 1] (also satisfies no rotation case)
# Also see Find max element - for python we can simply return a[pivot] as -1 gives last element

def findPivot(a, l, r):
    if l > r:
        return -1
    m = (l + r) // 2
    if m < r and a[m+1] < a[m]:
        return m
    if m > l and a[m-1] > a[m]:
        return m-1
    if a[l] > a[m]:
        return findPivot(a, l, m-1)
    return findPivot(a, m+1, r) 

def reverse(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

def sort(a):
    n = len(a)
    pivot = findPivot(a, 0, n - 1)
    # Array not rotated at all
    if pivot == -1:
        return
    # Reverse rotate to sort
    reverse(a, 0, pivot)
    reverse(a, pivot+1, n-1)
    reverse(a, 0, n-1)

a = [4, 5, 6, 7, 1, 2, 3]
sort(a)
print(a)
    