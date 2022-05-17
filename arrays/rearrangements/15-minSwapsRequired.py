'''
Given an array of n positive integers and a number k. Find the minimum number of swaps required to 
bring all the numbers less than or equal to k together. 
 
Input:  arr[] = {2, 1, 5, 6, 3}, k = 3
Output: 1

Explanation: 
To bring elements 2, 1, 3 together, swap 
element '5' with '3' such that final array
will be-
arr[] = {2, 1, 3, 6, 5}

Input:  arr[] = {2, 7, 9, 5, 8, 7, 4}, k = 5
Output: 2
'''
def minSwaps(a, k):
    n = len(a)
    c = 0
    for i in a:
        if i <= k:
            c += 1
    if c == 0:
        return 0
    mini = 0
    for i in range(c):
        if a[i] > k:
            mini += 1
    badCount = mini
    for i in range(c, n):
        enter, exit = a[i], a[i-c]
        if enter > k:
            badCount += 1
        if exit > k:
            badCount -= 1
        mini = min(mini, badCount)
    return mini

a = [2, 7, 9, 5, 8, 7, 4]
k = 5
print(minSwaps(a, k))


