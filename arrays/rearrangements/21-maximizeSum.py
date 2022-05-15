# https://www.geeksforgeeks.org/maximize-sum-consecutive-differences-circular-array/

'''
Given an array of n elements. Consider array as circular array i.e element after an is a1. The task is 
to find maximum sum of the difference between consecutive elements with rearrangement of array element 
allowed i.e after rearrangement of element find |a1 - a2| + |a2 - a3| + …… + |an - 1 - an| + |an - a1|. 
 
Examples: 

Input : arr[] = { 4, 2, 1, 8 }
Output : 18
Rearrange given array as : { 1, 8, 2, 4 }
Sum of difference between consecutive element
= |1 - 8| + |8 - 2| + |2 - 4| + |4 - 1|
= 7 + 6 + 2 + 3
= 18.
# 1 2 4 8
Input : arr[] = { 10, 12, 15 }
Output : 10
'''
def maximize(a):
    a.sort()
    l = 0
    r = len(a) - 1
    result = 0
    for i in range(len(a) - 1):
        result += abs(a[r] - a[l])
        if i % 2 == 0:
            l += 1
        else:
            r -= 1
    if len(a) % 2 == 0:
        result += abs(a[0] - a[r])
    else:
        result += abs(a[0] - a[l])
    return result

a = [6, 9, 12, 10, 1, 15]
print(maximize(a))