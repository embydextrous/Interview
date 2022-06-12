'''
Given two arrays A1[] and A2[], sort A1 in such a way that the relative order among the elements will 
be same as those are in A2. For the elements not present in A2, append them at last in sorted order. 
Example: 

Input: A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
       A2[] = {2, 1, 8, 3}
Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}
'''
from collections import Counter

def sort(A1, A2):
    c = Counter(A1)
    k = 0
    for x in A2:
        if x in c:
            for i in range(c[x]):
                A1[k] = x
                k += 1
            c.pop(x)
    for x in sorted(c.keys()):
        A1[k] = x
        k += 1

A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
A2 = [2, 1, 8, 3]
sort(A1, A2)
print(A1)