# https://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/
'''
Given an array of integers and a number x, find the smallest subarray with sum greater than the given value. 

Examples:
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

arr[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}

arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
    x = 280
Output: 4
Minimum length subarray is {100, 1, 0, 200}

arr[] = {1, 2, 4}
    x = 8
Output : Not Possible
Whole array sum is smaller than 8.
'''
def minLengthSubArray(a, k):
    n = len(a)
    l = r = 0
    minArraySize = n + 1
    sum = 0
    while l < n or r < n:
        if r < n and sum <= k:
            sum += a[r]
            r += 1
        if sum > k:
            minArraySize = min(minArraySize, r - l)
            sum -= a[l]
            l += 1
        if l == n and r ==  n:
            break
    if minArraySize == n + 1:
        return 0
    return minArraySize

a = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
k = 200
print(minLengthSubArray(a, k))
# How to handle negatives? Find smallest negative number and increment every number by its abs value (x)
# and look for sum k + n * x where n is length of array.
