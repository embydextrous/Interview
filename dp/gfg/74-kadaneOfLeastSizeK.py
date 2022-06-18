'''
Given an array, find the subarray (containing at least k numbers) which has the largest sum. 

Example:
a = [2, 3, 1, -7, 6, -5, -4, 4, 3, 3, 2, -9, -5, 6, 1, 2, 1, 1]
'''
def maxSum(a, k):
    n = len(a)
    meh = [-10 ** 9] * n
    maxSoFar = -10 ** 9
    maxEndingHere = 0
    for i in range(n):
        maxEndingHere += a[i]
        meh[i] = maxEndingHere
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
        if maxEndingHere < 0:
            maxEndingHere = 0
    kSum = 0
    for i in range(k):
        kSum += a[i]
    maxi = kSum
    for i in range(k, n):
        enter, exit = a[i], a[i-k]
        kSum += enter - exit
        maxi = max(maxi, kSum + max(0, meh[i-k]))
    return maxi


a = [2, 3, 1, -7, 6, -5, -4, 4, 3, 3, 2, -9, -5, 6, 1, 2, 1, 1]
k = 5
print(maxSum(a, k))