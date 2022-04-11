'''
A surpasser of an element of an array is a greater element to its right, therefore x[j] is a surpasser of x[i] if i < j 
and x[i] < x[j]. The surpasser count of an element is the number of surpassers. Given an array of distinct integers, 
for each element of the array find its surpasser count i.e. count the number of elements to the right that are greater
than that element.
Examples : 
 
Input:  [2, 7, 5, 3, 0, 8, 1]
Output: [4, 1, 1, 1, 2, 0, 0]
'''
def mergeSort(a, surpasser):
    if len(a) < 2:
        return
    m = len(a) // 2
    L = a[:m]
    R = a[m:]
    mergeSort(L, surpasser)
    mergeSort(R, surpasser)
    merge(a, L, R, surpasser)

def merge(a, L, R, surpasser):
    i = 0
    j = 0
    k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            if L[i] < R[j]:
                surpasser[L[i]] += len(R) - j
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

def surpasserCount(arr):
    a = arr[:]
    n = len(a)
    if n == 0:
        return []
    if n == 1:
        return [0]
    surpasser = { x : 0 for x in a }
    mergeSort(a, surpasser)
    return surpasser

a = [2, 7, 5, 3, 0, 8, 1]
#    [2, 7, 5]          [3, 0, 8, 1]
#     [2, 5, 7]         [0, 3]  [1, 8] 
# 2:2, 7:0, 5:0, 3:0, 0:2, 8:0, 1:0
print(surpasserCount(a).values())