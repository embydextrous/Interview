'''
Print the elements of an array in the decreasing frequency if 2 numbers have same frequency 
then print the one which came first. 

Examples:  

Input:  arr[] = {5, 2, 5, 8, 2, 6, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}
'''
from typing import Counter


def sortByFreq(a):
    d = Counter(a)
    a.sort(key = lambda x : (-d[x], x))

a = [2, 5, 5, 8, 2, 6, 8, 8]
sortByFreq(a)
print(a)