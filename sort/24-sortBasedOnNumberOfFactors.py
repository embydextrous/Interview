'''
Given an array of positive integers. Sort the given array in decreasing order of number of factors of 
each element, i.e., element having the highest number of factors should be the first to be displayed 
and the number having least number of factors should be the last one. Two elements with equal number 
of factors should be in the same order as in the original array.
Examples: 
 

Input : {5, 11, 10, 20, 9, 16, 23}
Output : 20 16 10 9 5 11 23
Number of distinct factors:
For 20 = 6, 16 = 5, 10 = 4, 9 = 3
and for 5, 11, 23 = 2 (same number of factors
therefore sorted in increasing order of index)

Input : {104, 210, 315, 166, 441, 180}
Output : 180 210 315 441 104 166
'''
import math

def numFactors(n):
    c = 0
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            c += 1
            if (n // i) * (n // i) != n:
                c += 1
    return c

def sort(a):
    a.sort(key = lambda x : (-numFactors(x)))

a = [104, 210, 315, 166, 441, 180]
sort(a)
print(a)