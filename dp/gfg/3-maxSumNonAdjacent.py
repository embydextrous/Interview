'''
Given an array arr[] of positive numbers, the task is to find the maximum sum of a subsequence with 
the constraint that no 2 numbers in the sequence should be adjacent in the array.

Examples: 

    Input: arr[] = {5, 5, 10, 100, 10, 5}
    Output: 110
    Explanation: Pick the subsequence {5, 100, 5}.
    The sum is 110 and no two elements are adjacent. This is the highest possible sum.

    Input: arr[] = {3, 2, 7, 10}
    Output: 13
    Explanation: The subsequence is {3, 10}. This gives sum = 13.
    This is the highest possible sum of a subsequence following the given criteria

    Input: arr[] = {3, 2, 5, 10, 7}
    Output: 15
    Explanation: Pick the subsequence {3, 5, 7}. The sum is 15.
'''
def maxSum(a):
    incl = excl = 0
    for i in a:
        newIncl = max(excl + i, incl)
        excl = max(incl, excl)
        incl = newIncl
        print(max(incl, excl))
    return max(incl, excl)

a = [3, 2, 5, 10, 7]
print(maxSum(a))