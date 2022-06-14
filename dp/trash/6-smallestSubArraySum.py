'''
Given an array containing n integers. The problem is to find the sum of the elements of the contiguous subarray having the smallest(minimum) sum.
Examples: 
 

Input : arr[] = {3, -4, 2, -3, -1, 7, -5}
Output : -6
Subarray is {-4, 2, -3, -1} = -6

Input : arr = {2, 6, 8, 1, 4}
Output : 1
'''
def minKadane(a):
    maxSoFar = -10 ** 9
    maxEndingHere = 0
    for i in a:
        maxEndingHere += -i
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
        if maxEndingHere < 0:
            maxEndingHere = 0
    return -maxSoFar

a = [2, 6, 8, 1, 4]
print(minKadane(a))