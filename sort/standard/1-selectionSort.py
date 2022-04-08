'''
The selection sort algorithm sorts an array by repeatedly finding the minimum element 
(considering ascending order) from unsorted part and putting it at the beginning. 
The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted. 
2) Remaining subarray which is unsorted.
'''
# Time Complexity - O(n^2) for all cases.
# Selection sort never makes more than O(n) swaps. Good if writes are costly.
# Not stable.
def selectionSort(a):
    n = len(a)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if a[j] < a[minIndex]:
                minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]

a = [3, 2, 7, 8, 3, 1, 9, 6, 2, 1]
selectionSort(a)
print(a)
