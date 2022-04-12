'''
Given two arrays that have the same values but in a different order, we need to make a second array the 
same as a first array using the minimum number of swaps. 
Examples:  

Input  : arrA[] = {3, 6, 4, 8}, 
         arrB[] = {4, 6, 8, 3}
Output : 2
we can make arrB to same as arrA in 2 swaps 
which are shown below,
swap 4 with 8,   arrB = {8, 6, 4, 3}
swap 8 with 3,   arrB = {3, 6, 4, 8}
'''
import array
import random

def minSwap(a, b):
    n = len(a)
    d = {b[i]:i for i in range(n)}
    arr = [d[a[i]] for i in range(n)]
    arrPos = [[arr[i], i] for i in range(n)]
    arrPos.sort(key = lambda x : x[0])
    i = 0
    visited = set()
    result = 0
    while i < n:
        cycleLength = 0
        while i not in visited:
            visited.add(i)
            cycleLength += 1
            i = arrPos[i][1]
        result += max(cycleLength - 1, 0)
        i += 1
    return result

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [4, 9, 1, 2, 7, 5, 3, 8, 6]
print(a)
print(b)
print(minSwap(a, b))
