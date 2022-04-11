# https://www.geeksforgeeks.org/counting-inversions/

# Another way to ask same problem, https://www.geeksforgeeks.org/number-swaps-sort-adjacent-swapping-allowed/
'''
Inversion Count for an array indicates - how far (or close) the array is from being sorted. 
If the array is already sorted, then the inversion count is 0, but if the array is sorted 
in the reverse order, the inversion count is the maximum. 
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j 
Example: 

Input: arr[] = {8, 4, 2, 1}
Output: 6

Explanation: Given array has six inversions:
(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).

Input: arr[] = {3, 1, 2}
Output: 2
(3, 1), (3, 2)
'''
def countInversions(a):
    n = len(a)
    if n <= 1:
        return 0
    m = n // 2
    L = a[:m]
    R = a[m:]
    left = countInversions(L)
    right = countInversions(R)
    # total inversions = inversions in left subarray + inversions in right subarray + inversions during merge
    return left + right + merge(a, L, R)

def merge(a, left, right):
    i = 0
    j = 0
    k = 0
    c = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
            # All elements left to be processed in left subarray will contribute to inversion
            c += len(left) - i
        k += 1
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
    return c

a = [9, 1, 3, 8, 2, 4]
print(countInversions(a))