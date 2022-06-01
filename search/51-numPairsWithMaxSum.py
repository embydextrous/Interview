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
from collections import defaultdict

def numPairs(arr):
    maxi = secMaxi = -10 ** 9
    d = defaultdict(int)
    for i in a:
        if i > maxi:
            maxi, secMaxi = i, maxi
        elif i > secMaxi:
            secMaxi = i
        d[i] += 1
    if maxi == secMaxi:
        return (d[maxi] * (d[maxi] - 1)) // 2
    else:
        return d[secMaxi]

a = [1, 2, 2, 1, 2, 1, 2, 1, 2]
print(numPairs(a))