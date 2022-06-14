'''
Given an array of integers, find two non-overlapping contiguous sub-arrays such that the absolute difference between the sum of two sub-arrays is maximum.

Example:

Input: [-2, -3, 4, -1, -2, 1, 5, -3]
Output: 12
Two subarrays are [-2, -3] and [4, -1, -2, 1, 5]

Input: [2, -1, -2, 1, -4, 2, 8]
Output: 16
Two subarrays are [-1, -2, 1, -4] and [2, 8] 
'''
def kadane(a):
    maxSoFar = -10 ** 9
    maxEndingHere = 0
    for i in a:
        maxEndingHere += i
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
        if maxEndingHere < 0:
            maxEndingHere = 0
    return maxSoFar


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

def solution(a):
    return kadane(a) - minKadane(a)

a = [2, -1, -2, 1, -4, 2, 8]
print(solution(a))