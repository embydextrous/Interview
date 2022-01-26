# https://www.geeksforgeeks.org/longest-span-sum-two-binary-arrays/
'''
Given two binary arrays, arr1[] and arr2[] of the same size n. 
Find the length of the longest common span (i, j) where j >= i such that 
arr1[i] + arr1[i+1] + … + arr1[j] = arr2[i] + arr2[i+1] + …. + arr2[j].
The expected time complexity is Θ(n).

Examples:  

Input: arr1[] = {0, 1, 0, 0, 0, 0};
       arr2[] = {1, 0, 1, 0, 0, 1};
Output: 4
The longest span with same sum is from index 1 to 4.

Input: arr1[] = {0, 1, 0, 1, 1, 1, 1};
       arr2[] = {1, 1, 1, 1, 1, 0, 1};
Output: 6
The longest span with same sum is from index 1 to 6.

Input: arr1[] = {0, 0, 0};
       arr2[] = {1, 1, 1};
Output: 0

Input: arr1[] = {0, 0, 1, 0};
       arr2[] = {1, 1, 1, 1};
Output: 1 
'''
# if diff of prevSum is 0 or difference of indexes
def longestSpanSum(a, b):
    n = len(a)
    cSum1 = cSum2 = 0
    differences = [-1] * (2 * n + 1)
    maxLen = 0
    for i in range(n):
        cSum1 += a[i]
        cSum2 += b[i]
        diff = cSum1 - cSum2
        if diff == 0:
            maxLen = i
        else:
            diffIndex = n + diff
            if differences[diffIndex] == -1:
                differences[diffIndex] = i
            else:
                maxLen = max(maxLen, i - differences[diffIndex])
    return maxLen

a = [0, 0, 0]
b = [1, 1, 1]
print(longestSpanSum(a, b))

