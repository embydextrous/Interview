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
def printKMaxInOrder(a, k):
    c = a[:]
    c.sort()
    c = c[::-1]
    d = {}
    for i in range(k):
        if c[i] in d:
            d[c[i]] += 1
        else:
            d[c[i]] = 1
    for i in a:
        if i in d and d[i] > 0:
            print(i, end = " ")
            d[i] -= 1
    print()

a = [42, 42, 45]
k = 2
printKMaxInOrder(a, k)

