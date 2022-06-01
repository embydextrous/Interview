'''
Given an array arr[] of integers and an integer k, we need to print k maximum elements of given array. 
The elements should printed in the order of the input.
Note : k is always less than or equal to n.


Examples:  

Input : arr[] = {10 50 30 60 15}
        k = 2
Output : 50 60
The top 2 elements are printed
as per their appearance in original
array.

Input : arr[] = {50 8 45 12 25 40 84}
            k = 3
Output : 50 45 84
'''

# Also see, https://www.geeksforgeeks.org/find-n-smallest-element-given-array-order-array/
from collections import defaultdict

def printKMaxInOrder(a, k):
    c = sorted(a, reverse=True)
    count = 0
    for i in range(k-1, -1, -1):
        if c[i] != c[k-1]:
            break
        count += 1
    print(count)
    for i in a:
        if i > c[k-1]:
            print(i, end = " ")
        elif i == c[k-1] and count > 0:
            print(i, end = " ")
            count -= 1
    print()

a = [1, 2, 3, 2, 3, 1, 2, 3, 4, 3]
k = 5
printKMaxInOrder(a, k)

