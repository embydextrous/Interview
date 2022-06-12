'''
Given a set of elements, find which permutation of these elements would result in worst case of Merge Sort.
Asymptotically, merge sort always takes O(nLogn) time, but the cases that require more comparisons generally 
take more time in practice. We basically need to find a permutation of input elements that would lead to 
maximum number of comparisons when sorted using a typical Merge Sort algorithm.

Example: 

Consider the below set of elements 
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}

Below permutation of the set causes 153
comparisons.
{1, 9, 5, 13, 3, 11, 7, 15, 2, 10, 6, 14, 4, 12, 8, 16}

And an already sorted permutation causes
30 comparisons. 

See this for a program that counts 
comparisons and shows above results.
'''
def generateWorstPermutationUtil(a):
    if len(a) < 2:
        return
    m = len(a) // 2
    L = a[:m]
    R = a[m:]
    generateWorstPermutationUtil(L)
    generateWorstPermutationUtil(R)
    worstMerge(a, L, R)

def worstMerge(a, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        a[k] = L[i]
        i += 1
        k += 1
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

def generateWorstPermutation(a):
    a.sort()
    generateWorstPermutationUtil(a)

def mergeSort(a):
    if len(a) < 2:
        return 0
    m = len(a) // 2
    L = a[:m]
    R = a[m:]
    l = mergeSort(L)
    r = mergeSort(R)
    t = 1 + l + r + merge(a, L, R)
    return t

def merge(a, L, R):
    i = j = k = 0
    count = 0
    while i < len(L) and j < len(R):
        count += 2
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
            count += 1
        else:
            a[k] = R[j]
            j += 1
            count += 1
        k += 1
    while i < len(L):
        count += 1
        a[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        count += 1
        a[k] = R[j]
        j += 1
        k += 1
    if L[i - 1] <= R[0]:
        return 1
    return count

a = [5, 2, 4, 8, 6, 7, 1, 3]
a.sort()
print(mergeSort(a))
print(a)
generateWorstPermutation(a)
print(a)
print(mergeSort(a))
    