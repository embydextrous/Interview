'''
Given an integer array of which both first half and second half are sorted. Task is to merge two sorted 
halves of array into single sorted array.

Examples: 

Input : A[] = { 2, 3, 8, -1, 7, 10 }
Output : -1, 2, 3, 7, 8, 10 

Input : A[] = {-4, 6, 9, -1, 3 }
Output : -4, -1, 3, 6, 9
'''
def sort(a):
    n = len(a)
    m = (n + 1) // 2
    L = a[:m]
    R = a[m:]
    i = j = k = 0
    if L[m - 1] <= R[0]:
        return
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
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

a = [-4, 6, 9, -1, 3]
sort(a)
print(a)
    