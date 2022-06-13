'''
Other sorting algorithms:

1 - BogoSort - generate a permutation and check if it is sorted or not.
    O(inf) worst case [sorted permutation never generated], 
    O(n) best case [first permutation is sorted] and O(n * n!) in average case.
    # https://www.geeksforgeeks.org/bogosort-permutation-sort/

2 - TreeSort - Insert elements of array in a BST and traverse in inorder fashion and fill the array.
    Time Complexity - 
    O(n^2) (can be improved to O(nlogn) with balanced BSTs) - Already sorted or reverse sorted
    Average case and best case (forms a height balanced BST) is O(nlogn)
    Space Complexity - O(n)
    # https://www.geeksforgeeks.org/tree-sort/

3 - SleepSort - sleep for time proportional to value. Indeterministic due to CPU Scheduling of threads.
    # https://www.geeksforgeeks.org/sleep-sort-king-laziness-sorting-sleeping/

4 - Timsort - Modified merge sort which uses insertion sort if array length falls below blockSize 
    (may be 32 or 64). Used in python sort() and sorted() as well as in Java's Arrays.sort()
    Stable and O(nlogn) algorithms.
    # https://www.geeksforgeeks.org/timsort/

5 - Shell Sort - https://www.geeksforgeeks.org/shellsort/
'''
from random import randint

def heapify(a, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def buildMaxHeap(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        heapify(a, n, i)

def heapSort(a):
    n = len(a)
    buildMaxHeap(a)
    for i in range(n - 1, -1, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

a = [randint(1, 20) for i in range(10)]
print(a)
heapSort(a)
print(a)