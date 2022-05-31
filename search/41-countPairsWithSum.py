'''
Given an array of integers, and a number 'sum', find the number of pairs of integers in the array 
whose sum is equal to 'sum'.

Examples:  

Input  :  arr[] = {1, 5, 7, -1}, 
          sum = 6
Output :  2
Pairs with sum 6 are (1, 5) and (7, -1)

Input  :  arr[] = {1, 5, 7, -1, 5}, 
          sum = 6
Output :  3
Pairs with sum 6 are (1, 5), (7, -1) &
                     (1, 5)         

Input  :  arr[] = {1, 1, 1, 1}, 
          sum = 2
Output :  6
There are 3! pairs with sum 2.

Input  :  arr[] = {10, 12, 10, 15, -1, 7, 6, 
                   5, 4, 2, 1, 1, 1}, 
          sum = 11
Output :  9
'''
from collections import defaultdict

def countPairs(a, x):
    d = defaultdict(int)
    c = 0
    for i in a:
        if x - i in d:
            c += d[x-i]
        d[i] += 1
    return c
    
a = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
x = 11
print(countPairs(a, x))