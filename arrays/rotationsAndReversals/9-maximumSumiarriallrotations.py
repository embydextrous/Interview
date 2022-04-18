# https://www.geeksforgeeks.org/maximum-sum-iarri-among-rotations-given-array/
'''
Given an array arr[] of n integers, find the maximum that maximizes the sum of the value of i*arr[i] where i 
varies from 0 to n-1.

Examples:  

Input: arr[] = {8, 3, 1, 2}
Output: 29
Explanation: Lets look at all the rotations,
{8, 3, 1, 2} = 8*0 + 3*1 + 1*2 + 2*3 = 11
{3, 1, 2, 8} = 3*0 + 1*1 + 2*2 + 8*3 = 29
{1, 2, 8, 3} = 1*0 + 2*1 + 8*2 + 3*3 = 27
{2, 8, 3, 1} = 2*0 + 8*1 + 3*2 + 1*3 = 17

Input: arr[] = {3, 2, 1}
Output: 7
Explanation: Lets look at all the rotations,
{3, 2, 1} = 3*0 + 2*1 + 1*2 = 4
{2, 1, 3} = 2*0 + 1*1 + 3*2 = 7
{1, 3, 2} = 1*0 + 3*1 + 2*2 = 7
'''
def findMaxRotationSum(a):
    n = len(a)
    sum = 0
    for i in a:
        sum += i
    rotationSum = 0
    for i in range(n):
        rotationSum += i * a[i]
    maxRotationSum = rotationSum
    print(rotationSum)
    for i in range(n-1):
        rotationSum = rotationSum - sum + n * a[i]
        print(rotationSum)
        maxRotationSum = max(maxRotationSum, rotationSum)
    return maxRotationSum

a = [8, 3, 1, 2]
findMaxRotationSum(a)