'''
Given an array that contains both positive and negative integers, find the product of the maximum product 
subarray. Expected Time complexity is O(n) and only O(1) extra space can be used.

Examples:

Input: arr[] = {6, -3, -10, 0, 2}
Output:   180  // The subarray is {6, -3, -10}

Input: arr[] = {-1, -3, -10, 0, 60}
Output:   60  // The subarray is {60}

Input: arr[] = {-2, -40, 0, -2, -3}
Output:   80  // The subarray is {-2, -40}
'''
def maxProduct(a):
    maxSoFar = a[0]
    maxEndingHere = a[0]
    minEndingHere = a[0]
    for i in range(1, len(a)):
        x = a[i]
        temp = max(x, maxEndingHere * x, minEndingHere * x)
        minEndingHere = min(x, maxEndingHere * x, minEndingHere * x)
        maxEndingHere = temp
        maxSoFar = max(maxSoFar, minEndingHere, maxEndingHere)
    return maxSoFar

a = [6, -3, -10, 0, 2]
print(maxProduct(a))
    