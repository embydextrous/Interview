'''
Given an array of integers, update every element with multiplication of previous and next 
elements with following exceptions. 

a) First element is replaced by multiplication of first and second. 
b) Last element is replaced by multiplication of last and second last.

Example:  

Input: arr[] = {2, 3, 4, 5, 6}
Output: arr[] = {6, 8, 15, 24, 30}

// We get the above output using following
// arr[] = {2*3, 2*4, 3*5, 4*6, 5*6} 
'''
from re import L


def replace(a):
    n = len(a)
    if n <= 1:
        return
    prevElement = None
    for i in range(n):
        if i == 0:
            prevElement = a[i]
            a[i] *= a[i+1]
        elif i == n - 1:
            a[i] *= prevElement
        else:
            prevElement, a[i] = a[i], prevElement * a[i+1]

a = [2, 3, 4, 5, 6]
replace(a)
print(a)