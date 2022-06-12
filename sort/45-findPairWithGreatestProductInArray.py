'''
Given an array of n elements, the task is to find the greatest number such that it is product of two 
elements of given array. If no such element exists, print -1. Elements are within the range of 1 to 10^5.
Examples : 

Input :  arr[] = {10, 3, 5, 30, 35}
Output:  30
Explanation: 30 is the product of 10 and 3.

Input :  arr[] = {2, 5, 7, 8}
Output:  -1
Explanation: Since, no such element exists.

Input :  arr[] = {10, 2, 4, 30, 35}
Output:  -1

Input :  arr[] = {10, 2, 2, 4, 30, 35}
Output:  4

Input  : arr[] = {17, 2, 1, 35, 30}
Output : 35
'''
from collections import Counter

def findPair(a):
    n = len(a)
    a.sort()
    c = Counter(a)
    for i in range(n-1, 1, -1):
        x = 1
        while x * x <= a[i]:
            if a[i] % x == 0:
                if x == a[i] // x and c[x] == 2:
                    return a[i]
                if x in c and a[i] // x in c:
                    return a[i]
            x += 1
    return None

a = [17, 2, 1, 35, 30]
print(findPair(a))