# https://www.geeksforgeeks.org/cycle-sort/
'''
Cycle sort is an in-place sorting Algorithm, unstable sorting algorithm, a comparison sort that 
is theoretically optimal in terms of the total number of writes to the original array. 
 
It is optimal in terms of number of memory writes. It minimizes the number of memory writes to sort 
(Each value is either written zero times, if it's already in its correct position, or written one time 
to its correct position.)

It is based on the idea that array to be sorted can be divided into cycles. 
Cycles can be visualized as a graph. We have n nodes and an edge directed from node i to node j 
if the element at i-th index must be present at j-th index in the sorted array. 
   
'''
'''
Time Complexity : O(n^2) 
Worst Case : O(n^2) 
Average Case: O(n^2) 
Best Case : O(n^2)
'''
# Python program to implement cycle sort

def cycleSort(a):
    writes = 0
    n = len(a)
    for cycleStart in range(n-1):
        item = a[cycleStart]
        pos = cycleStart
        for i in range(cycleStart + 1, n):
            if a[i] < item:
                pos += 1
        if pos == cycleStart:
            continue
        while item == a[pos]:
            pos += 1
        a[pos], item = item, a[pos]
        writes += 1
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, n):
                if a[i] < item:
                    pos += 1
            while item == a[pos]:
                pos += 1
            a[pos], item = item, a[pos]
            writes += 1
    return writes


# driver code
a = [1, 8, 3, 9, 10, 10, 2, 4 ]
n = len(a)
print(cycleSort(a))
print(a)
