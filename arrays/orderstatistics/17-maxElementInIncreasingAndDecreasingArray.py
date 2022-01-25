# https://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/
def findMax(a, l, r):
    # if only one element return it
    if l == r:
        return a[l]
    # if two elements return higher
    if r == l + 1:
        return max(a[l], a[r])
    mid = (l + r) // 2
    # Check if mid is a peak element
    if a[mid] > a[mid-1] and a[mid] > a[mid+1]:
        return a[mid]
    # if mid - 1 < mid < mid + 1, natural order, recur for right subarray
    if a[mid] < a[mid + 1] and a[mid-1] < a[mid]:
        return findMax(a, mid+1, r)
    # if mid - 1 > mid > mid + 1, reverse order, recur for left subarray
    return findMax(a, l, mid - 1)

a = [1, 3, 50, 10, 9, 7, 6] 
print(findMax(a, 0, len(a)))
