'''
Given an array, a positive integer, sort the array in ascending order such that the element at index K 
in the unsorted array stays unmoved and all other elements are sorted. 

Examples: 

ibs - 2
ias - 4
4 6 11 7 10 20
Input : arr[] = {10, 4, 11, 7, 6, 20}
            k = 2;
Output : arr[] = {4, 6, 11, 7, 10, 20}

Input : arr[] = {30, 20, 10}
         k = 0
Output : arr[] = {30, 10, 20} 
'''
from search import binarySearchUtil

def sort(a, k):
    n = len(a)
    x = a[k]
    a.sort()
    ias = binarySearchUtil(a, 0, n - 1, x)
    if ias > k:
        for i in range(ias, k, -1):
            a[i] = a[i - 1]
    else:
        for i in range(ias, k):
            a[i] = a[i + 1]
    a[k] = x
# 4 6 7 10 11 20

a = [10, 4, 11, 7, 6, 20]
sort(a, 2)
print(a)