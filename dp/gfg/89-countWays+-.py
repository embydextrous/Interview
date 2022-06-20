'''
Given an array A[] consisting of N non-negative integers, and an integer K, the task is to find the number of 
ways '+' and '-' operators can be placed in front of elements of the array A[] such that the sum of the array becomes K.

Examples:

    Input: A[] = {1, 1, 2, 3}, N = 4, K = 1
    Output: 3
    Explanation: Three possible ways are:

        + 1 + 1 + 2 - 3 = 1
        + 1 - 1 - 2 + 3 = 1
        - 1 + 1 - 1 + 3 = 1

    Input: A[] = {1, 1, 1, 1, 1}, N = 5, K = 3
    Output: 5
'''
def countUtil(a, idx, k, memo):
    if idx == len(a) and k == 0:
        return 1
    if idx == len(a) and k != 0:
        return 0
    if (k, idx) in memo:
        return memo[(k, idx)]
    memo[(k, idx)] = countUtil(a, idx + 1, k - a[idx-1], memo) + countUtil(a, idx + 1, k + a[idx-1], memo)
    return memo[(k, idx)]

memo = {}
a = [1, 1, 1, 1, 1]
k = 3
print(countUtil(a, 0, k, memo))