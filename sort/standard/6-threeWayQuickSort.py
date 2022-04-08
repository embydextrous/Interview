'''
In simple QuickSort algorithm, we select an element as pivot, partition the array around a pivot
and recur for subarrays on the left and right of the pivot. 
Consider an array which has many redundant elements. For example, 
{1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4}. 
If 4 is picked as a pivot in Simple Quick Sort, we fix only one 4 and recursively 
process remaining occurrences.
The idea of 3 way Quick Sort is to process all occurrences of the pivot and is based on 
Dutch National Flag 🇳🇱 algorithm. 

In 3 Way QuickSort, an array arr[l..r] is divided in 3 parts:
a) arr[l..i] elements less than pivot.
b) arr[i+1..j-1] elements equal to pivot.
c) arr[j..r] elements greater than pivot.
'''
from random import randint

def quickSort(a, l, r):
    if l < r:
        (i, j) = partition(a, l, r)
        quickSort(a, l, i - 1)
        quickSort(a, j + 1, r)

def partition(a, l, r):
    x = a[r]
    i = l
    m = l
    j = r
    while m <= j:
        if a[m] < x:
            a[m], a[i] = a[i], a[m]
            i += 1
            m += 1
        elif a[m] == x:
            m += 1
        else:
            a[m], a[j] = a[j], a[m]
            j -= 1
    return (i, j)

a = [randint(1, 9) for i in range(20)]
print(a)
quickSort(a, 0, len(a) - 1)
print(a)