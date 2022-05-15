'''
Given n numbers (both +ve and -ve), arranged in a circle, find the maximum sum of consecutive numbers. 

Examples: 

Input: a[] = {8, -8, 9, -9, 10, -11, 12}
Output: 22 (12 + 8 - 8 + 9 - 9 + 10)

Input: a[] = {10, -3, -4, 7, 6, 5, -4, -1} 
Output:  23 (7 + 6 + 5 - 4 -1 + 10) 

Input: a[] = {-1, 40, -14, 7, 6, 5, -4, -1}
Output: 52 (7 + 6 + 5 - 4 - 1 - 1 + 40)
'''
def kadane(a):
    maxSoFar = -10 ** 9
    maxEndingHere = 0
    for i in range(len(a)):
        maxEndingHere += a[i]
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
        if maxEndingHere < 0:
            maxEndingHere = 0
    return maxSoFar

def maxCircularSubarraySum(a):
    c1 = kadane(a)
    sum = 0
    for i in range(len(a)):
        sum += a[i]
        a[i] *= -1
    c2 = sum + kadane(a)
    print(sum, c1, c2, kadane(a))
    return max(c1, c2)

a = [-1, 40, -14, 7, 6, 5, -4, -1]
print(maxCircularSubarraySum(a))
    
