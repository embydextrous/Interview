# https://www.geeksforgeeks.org/convert-an-array-to-reduced-form-set-1-simple-and-hashing/
'''
Given an array with n distinct elements, convert the given array to a form where all elements are 
in the range from 0 to n-1. The order of elements is the same, i.e., 0 is placed in the place of the 
smallest element, 1 is placed for the second smallest element, … n-1 is placed for the largest element. 

Input:  arr[] = {10, 40, 20}
Output: arr[] = {0, 2, 1}

Input:  arr[] = {5, 10, 40, 30, 20}
Output: arr[] = {0, 1, 4, 3, 2}
'''
def reduce(a):
    aux = [[a[i], i] for i in range(len(a))]
    aux.sort(key = lambda x : x[0])
    for i in range(len(a)):
        a[i] = aux[i][1]

a = [5, 10, 40, 30, 20]
reduce(a)
print(a)