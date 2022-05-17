'''
Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of 
numbers that has the largest sum. 

For ex:

a = [-2, -3, 4, -1, -2, 1, 5, -3]

Output:
7   [4, -1, -2, 1, 5]
'''
# Variations
# 1. Find Array
# 2. Find Nax Circular Sum SubArray - c1 = kadane(a), c2 = sum(s) + kadane(-a), max(c1, c2)
# 3. Find Largest Sum Rectangle - Left right top bottom using 1
# 4. Find K Non Overlapping Max Sums - Use Kadane K times and set all elements of array found to -INF
def kadane(a):
    maxSoFar = -10 ** 9
    maxEndingHere = 0
    for i in a:
        maxEndingHere += i
        maxSoFar = max(maxSoFar, maxEndingHere)
        maxEndingHere = max(maxEndingHere, 0)
    return maxSoFar

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kadane(a))