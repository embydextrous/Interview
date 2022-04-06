'''
Given an array arr[], count number of pairs arr[i], arr[j] such that arr[i] + arr[j] is maximum and i < j.

Example :
Input  : arr[] = {1, 1, 1, 2, 2, 2}
Output : 3
Explanation: The maximum possible pair 
sum where i<j is  4, which is given 
by 3 pairs, so the answer is 3
the pairs are (2, 2), (2, 2) and (2, 2)

Input  : arr[] = {1, 4, 3, 3, 5, 1}
Output : 1
Explanation: The pair 4, 5 yields the 
maximum sum i.e, 9 which is given by 1 pair only
'''
import sys

def numPairs(arr):
    d = {}
    a = b = -sys.maxsize-1
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        if i >= a:
            a, b = i, a
        elif i > b:
            b = i
    if a == b:
        return (d[a] * (d[a] - 1)) // 2
    return d[b]

a = [1, 2, 2, 1, 2, 1, 2, 1, 2, 3]
print(numPairs(a))