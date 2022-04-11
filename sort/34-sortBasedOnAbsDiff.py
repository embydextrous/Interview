'''
Given an array of n distinct elements and a number x, arrange array elements according to the absolute 
difference with x, i. e., an element having minimum difference comes first, and so on. 
Note: If two or more elements are at equal distance arrange them in the same sequence as in the given array.
Examples : 

Input : arr[] : x = 7, arr[] = {10, 5, 3, 9, 2}
Output : arr[] = {5, 9, 10, 3, 2}
Explanation:
7 - 10 = 3(abs)
7 - 5 = 2
7 - 3 = 4 
7 - 9 = 2(abs)
7 - 2 = 5
So according to the difference with X, 
elements are arranged as 5, 9, 10, 3, 2.

Input : x = 6, arr[] = {1, 2, 3, 4, 5}   
Output :  arr[] = {5, 4, 3, 2, 1}

Input : x = 5, arr[] = {2, 6, 8, 3}   
Output :  arr[] = {6, 3, 2, 8}
'''
def mergeSort(a, x):
    if len(a) < 2:
        return
    m = len(a) // 2
    L = a[:m]
    R = a[m:]
    mergeSort(L, x)
    mergeSort(R, x)
    merge(a, L, R, x)

def merge(a, L, R, x):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if abs(L[i] - x) <= abs(R[j] - x):
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        a[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        a[k] = R[j]
        j += 1
        k += 1

a = [2, 6, 8, 3]
x = 5
mergeSort(a, x)
print(a)
