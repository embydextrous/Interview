# https://www.geeksforgeeks.org/sort-n-numbers-range-0-n2-1-linear-time/
'''
Given an array of numbers of size n. It is also given that the array elements are in range from 0 to n2 - 1. 
Sort the given array in linear time.

Examples: 

Since there are 5 elements, the elements can be from 0 to 24.
Input: arr[] = {0, 23, 14, 12, 9}
Output: arr[] = {0, 9, 12, 14, 23}

Since there are 3 elements, the elements can be from 0 to 8.
Input: arr[] = {7, 0, 2}
Output: arr[] = {0, 2, 7}
'''
import math

def countSort(a, N, exp):
    count = [0] * N
    output = [0] * len(a)
    for i in a:
        count[(i // exp) % N] += 1
    for i in range(N-1):
        count[i+1] += count[i]
    for i in range(N-1, -1, -1):
        idx = (a[i] // exp) % N
        output[count[idx] - 1] = a[i]
        count[idx] -= 1
    a[:] = output[:]


def sort(a):
    maxi = max(a)
    N = math.ceil(math.sqrt(maxi + 1))
    exp = 1
    for i in range(2):
        countSort(a, N, exp)
        exp = exp * N

a = [0, 23, 14, 12, 9]
sort(a)
print(a)