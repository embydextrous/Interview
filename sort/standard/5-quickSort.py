'''
QuickSort is faster in practice, because its inner loop can be efficiently implemented on most 
architectures, and in most real-world data. QuickSort can be implemented in different ways by 
changing the choice of pivot, so that the worst case rarely occurs for a given type of data. 
However, merge sort is generally considered better when data is huge and stored in external storage. 
'''

'''
Worst case
The answer depends on the strategy for choosing pivot. In early versions of Quick Sort where the leftmost
 (or rightmost) element is chosen as a pivot, the worst occurs in the following cases. 

1) Array is already sorted in the same order. 
2) Array is already sorted in reverse order. 
3) All elements are the same (a special case of cases 1 and 2) 

Optimizations in Quicksort
1) Partition process is the same in both recursive and iterative. 
The same techniques to choose optimal pivot can also be applied to the iterative version.
2) To reduce the stack size, first push the indexes of smaller half.
3) Use insertion sort when the size reduces below an experimentally calculated threshold.
'''
from random import randint

# Time Complexity - O(nlogn) for best and average cases, O(n^2) for worst case
# To be used with Hoare's partition.
def quickSort(a, l, r):
    if l < r:
        #p = partition(a, l, r)
        p = partition2(a, l, r)
        quickSort(a, l, p)
        quickSort(a, p + 1, r)

# To be used with Lomuto's partition.
def qsort(a, l, r):
    if l < r:
        #p = partition(a, l, r)
        p = partition(a, l, r)
        quickSort(a, l, p - 1)
        quickSort(a, p + 1, r)
'''
Hoare's scheme is more efficient than Lomuto's partition scheme because it does three times fewer swaps 
on average, and it creates efficient partitions even when all values are equal.
# https://cs.stackexchange.com/a/11550

Like Lomuto's partition scheme, Hoare partitioning also causes Quick sort to degrade to O(n^2) when the 
input array is already sorted, it also doesn't produce a stable sort.

Hoare's is difficult to understand and implement.
'''
# Lomuto's Partition
def partition(a, l, r):
    x = a[r]
    i = l
    for j in range(l, r):
        if a[j] <= x:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i

# Hoare's Partition
def partition2(a, l, r):
    x = a[l]
    i, j = l - 1, r + 1
    while True:
        i += 1
        while a[i] < x:
            i += 1
        j -= 1
        while a[j] > x:
            j -= 1
        if j <= i:
            return j
        a[i], a[j] = a[j], a[i]

def randomPartition(a, l, r):
    randomIndex = randint(l, r - 1)
    a[randomIndex], a[r] = a[r], a[randomIndex]
    return partition(a, l, r)

def iterativeQuickSort(a):
    n = len(a)
    if n <= 1:
        return
    l, r = 0, n - 1
    s = [(l, r)]
    while len(s) > 0:
        (l, r) = s.pop()
        p = partition(a, l, r)
        if p - 1 > l:
            s.append((l, p - 1))
        if p + 1 < r:
            s.append((p + 1, r))

# https://www.geeksforgeeks.org/quicksort-tail-call-optimization-reducing-worst-case-space-log-n/
def quickSortWithTailCallOptimization(a, l, r):
    while (l < r):
        # pi is partitioning index, arr[p] is now
        #  at right place '''
        p = partition(a, l, r)
        # Separately sort elements before
        # partition and after partition
        if p - l < r - p:
            quickSortWithTailCallOptimization(a, l, p - 1)
            l = p + 1
        else:
            quickSortWithTailCallOptimization(a, p + 1, r)
            r = p - 1

def quickSortWorstNLogN(a, l, r):
    if l < r:
        p = partition(a, l, r, medianUtil(a, l, r, l + (r - l) // 2))
        quickSortWorstNLogN(a, l, p - 1)
        quickSortWorstNLogN(a, p + 1, r)

def partition(a, l, r, median):
    for i in range(l, r):
        if a[i] == median:
            a[i], a[r] = a[r], a[i]
            break
    i = l
    for j in range(l, r):
        if a[j] <= median:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[r], a[i] = a[i], a[r]
    return i

def findMedian(a, l, n):
    lis = [a[i] for i in range(l, l+n)]
    lis.sort()
    return lis[n//2]

def medianUtil(a, l, r, k):
    n = r - l + 1
    if n > 0 and k >= l and k <= r:
        medians = []
        i = 0
        while i < n // 5:
            medians.append(findMedian(a, l + i * 5, 5))
            i += 1
        if i * 5 < n:
            medians.append(findMedian(a, l + i * 5, n % 5))
            i += 1
        if i == 1:
            medianOfMedians = medians[i-1]
        else:
            medianOfMedians = medianUtil(medians, 0, i - 1, i // 2)
        pos = partition(a, l, r, medianOfMedians)
        if pos == k:
            return a[pos]
        if pos > k:
            return medianUtil(a, l, pos - 1, k)
        return medianUtil(a, pos + 1, r, k)

a = [3, 2, 7, 8, 3, 1, 9, 6, 2, 1]
quickSort(a, 0, len(a) - 1)
print(a) 

# This is the worst case for quick sort and fails due to recursion depth. So have to use random partition
# instead of last one.
b = [i for i in range(1, 1200)]
#quickSortWithTailCallOptimization(b, 0, len(b) - 1)
#print(b)

a = [randint(1, 50) for i in range(20)]
quickSortWorstNLogN(a, 0, len(a) - 1)
print(a) 