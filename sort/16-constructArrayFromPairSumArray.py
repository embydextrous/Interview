'''
Given a pair-sum array and size of the original array (n), construct the original array.
A pair-sum array for an array is the array that contains sum of all pairs in ordered form. 
For example pair-sum array for arr[] = {6, 8, 3, 4} is {14, 9, 10, 11, 12, 7}.
In general, pair-sum array for arr[0..n-1] is {arr[0]+arr[1], arr[0]+arr[2], ……., arr[1]+arr[2], 
arr[1]+arr[3], ……., arr[2]+arr[3], arr[2]+arr[4], …., arr[n-2]+arr[n-1}.
“Given a pair-sum array, construct the original array.”

We strongly recommend to minimize your browser and try this yourself.
Let the given array be “pair[]” and let there be n elements in original array. If we take a look at 
few examples, we can observe that arr[0] is half of pair[0] + pair[1] - pair[n-1]. 
Note that the value of 
pair[0] + pair[1] - pair[n-1] is (arr[0] + arr[1]) + (arr[0] + arr[2]) - (arr[1] + arr[2]). 
Once we have evaluated arr[0], we can evaluate other elements by subtracting arr[0]. 
For example arr[1] can be evaluated by subtracting arr[0] from pair[0], arr[2] can be evaluated 
by subtracting arr[0] from pair[1].
Following is the implementation of the above idea.

Input:
[15, 13, 11, 10, 12, 10, 9, 8, 7, 5]

Output:
8 7 5 3 2
'''
import math

def arrayFromPairSumArray(pairSumArray):
    n = int(math.sqrt(2 * len(pairSumArray)) + 1)
    result = [0] * n
    result[0] = (pairSumArray[0] + pairSumArray[1] - pairSumArray[n-1]) // 2
    for i in range(1, n):
        result[i] = pairSumArray[i-1] - result[0]
    return result

a = [15, 13, 11, 10, 12, 10, 9, 8, 7, 5]
print(arrayFromPairSumArray(a))