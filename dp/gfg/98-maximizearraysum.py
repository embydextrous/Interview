'''
Given an array arr[] of N integers, the task is to find the maximum sum of the array that can be obtained by flipping signs of any subarray of the given array at most once.

Examples:

    Input: arr[] = {-2, 3, -1, -4, -2} 
    Output: 8
    Explanation: 
    Flipping the signs of subarray {-1, -4, -2} modifies the array to {-2, 3, 1, 4, 2}. Therefore, the sum of the array = -2 + 3 + 1 + 4 + 2 = 8, which is the maximum possible.

    Input: arr[] = {1, 2, -10, 2, -20}
    Output: 31 
    Explanation: 
    Flipping the signs of subarray {-10, 2, -20} modifies the array to {1, 2, 10, -2, 20}. Therefore, the sum of the array = 1 + 2 + 10 - 2 + 20 = 31, which is the maximum possible.
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
        print(maxSoFar, maxEndingHere)
    return -maxSoFar

def maximizeSum(a):
    total = sum(a)
    minSum = minKadane(a)
    print(minSum)
    return max(total, total - 2 * minKadane(a))

a = [-2, 3, -1, -4, -2]
print(maximizeSum(a))