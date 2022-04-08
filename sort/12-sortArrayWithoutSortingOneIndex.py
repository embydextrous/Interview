'''
Given an array, a positive integer, sort the array in ascending order such that the element at index K 
in the unsorted array stays unmoved and all other elements are sorted. 

Examples: 

Input : arr[] = {10, 4, 11, 7, 6, 20}
            k = 2;
Output : arr[] = {4, 6, 11, 7, 10, 20}

Input : arr[] = {30, 20, 10}
         k = 0
Output : arr[] = {30, 10, 20} 
'''
from search import binarySearchUtil

def sort(a, k):
    v = a[k]
    a.sort()
    indexAfterSorting = binarySearchUtil(a, 0, len(a) - 1, v)
    if indexAfterSorting == k:
        return
    if indexAfterSorting > k:
        v = a[indexAfterSorting]
        for i in range(indexAfterSorting, k, -1):
            a[i] = a[i-1]
        a[k] = v
    else:
        v = a[indexAfterSorting]
        for i in range(indexAfterSorting, k):
            a[i] = a[i+1]
        a[k] = v
# 4 6 7 10 11 20

a = [10, 4, 11, 7, 6, 20]
sort(a, 4)
print(a)