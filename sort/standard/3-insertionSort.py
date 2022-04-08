# https://www.geeksforgeeks.org/insertion-sort/
# Time Complexity - O(n^2) for average and worst case, O(n) for best case.
# Makes 0 swaps if array already sorted.
# Stable
def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        x = a[i]
        j = i - 1
        while j >= 0 and x < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x

a = [3, 2, 7, 8, 3, 1, 9, 6, 2, 1]
insertionSort(a)
print(a) 
