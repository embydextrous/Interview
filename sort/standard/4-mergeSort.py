# Time Complexity - O(nlogn) for all cases.
# T(n) = 2T(n/2) + θ(n)
# Stable Yes
# Usually used in external sorting

'''
no optimization is possible if the left and right sub-arrays involved in the merge operation
have alternate elements of the sorted array. For example, if the left and right sub-array are
{1,3,5,7} and {2,4,6,8} respectively,
'''
def mergeSort(a, l, r):
    if l < r:
        m = l + (r - l) // 2
        left = a[:m+1]
        right = a[m+1:]
        mergeSort(left, 0, m)
        mergeSort(right, m + 1, r)
        merge(a, left, right)

def merge(a, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1

a = [3, 2, 7, 8, 3, 1, 9, 6, 2, 1]
mergeSort(a, 0, len(a) - 1)
print(a) 

    
