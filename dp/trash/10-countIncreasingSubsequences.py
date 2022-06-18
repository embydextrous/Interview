'''
We are given an array of digits (values lie in range from 0 to 9). The task is to count all the sub sequences possible in array such that in each subsequence every digit is greater than its previous digits in the subsequence.

Examples: 

Input : arr[] = {1, 2, 3, 4}
Output: 15
There are 15 increasing subsequences
{1}, {2}, {3}, {4}, {1,2}, {1,3}, {1,4}, 
{2,3}, {2,4}, {3,4}, {1,2,3}, {1,2,4}, 
{1,3,4}, {2,3,4}, {1,2,3,4}

Input : arr[] = {4, 3, 6, 5}
Output: 8
Sub-sequences are {4}, {3}, {6}, {5}, 
{4,6}, {4,5}, {3,6}, {3,5}

Input : arr[] = {3, 2, 4, 5, 4}
Output : 14
Sub-sequences are {3}, {2}, {4}, {3,4},
{2,4}, {5}, {3,5}, {2,5}, {4,5}, {2,4,5}
{3,4,5}, {4}, {3,4}, {2,4}
'''
from collections import defaultdict

def count(a):
    c = [0] * 10
    for i in a:
        c[i] += 1
        for j in range(i - 1, -1, -1):
            c[i] += c[j]
    return sum(c)

# [0, 0, 1, 1, 2, 1, 0, 0, 0, 0]
# 1 2 5 9

a = [3, 2, 4, 5, 4]
print(count(a))