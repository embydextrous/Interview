'''
Given an unsorted array arr of nonnegative integers and an integer sum, 
find a continuous subarray which adds to a given sum. There may be more than 
one subarrays with sum as the given sum, print first such subarray. 
Examples : 

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Output: Sum found between indexes 2 and 4
Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33
'''
# Doesn't work if negative numbers. Use prefixArray.
def subArray(a, x):
    n = len(a)
    sum = a[0]
    l = 0
    r = 1
    while r <= n:
        while sum > x and l < r - 1:
            sum -= a[l]
            l += 1
        if sum == x:
            return a[l:r]
        if r < n:
            sum += a[r]
        r += 1

# Also see, https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/
def subArrayWithNegative(a, x):
    d = {}
    sum = 0
    for i in range(len(a)):
        sum += a[i]
        if sum == x:
            return a[0:i+1]
        if sum - x in d:
            return a[d[sum - x] + 1:i+1]
        else:
            d[sum] = i

a = [1, 2, 3, 4, 5]
x = -2
print(subArrayWithNegative(a, x))
