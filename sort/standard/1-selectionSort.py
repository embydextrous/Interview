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
def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        j = i - 1
        x = a[i]
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x
        
# 
a = [3, 2, 7, 8, 3, 1, 9, 6, 2, 1]
insertionSort(a)
print(a)
