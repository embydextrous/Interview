'''
A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty. 
Similarly, decreasing order sequence is considered Bitonic with the increasing part as empty. 
Examples:

Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)

Input arr[] = {12, 11, 40, 5, 3, 1}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 12, 11, 5, 3, 1)

Input arr[] = {80, 60, 30, 40, 20, 10}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 80, 60, 30, 20, 10)
'''
# Also see, https://www.geeksforgeeks.org/minimum-removals-required-to-make-a-given-array-bitonic/
# Also see, https://www.geeksforgeeks.org/minimum-removals-required-to-convert-given-array-to-a-mountain-array/
def lbs(a):
    n = len(a)
    lis = [1] * n
    reverselis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and lis[j] + 1 > lis[i]:
                lis[i] = 1 + lis[j]
    for i in range(n - 2, -1, -1):
        for j in range(n-1, i, -1):
            if a[i] > a[j] and reverselis[j] + 1 > reverselis[i]:
                reverselis[i] = 1 + reverselis[j]
    maxi = -1
    for i in range(n):
        maxi = max(maxi, lis[i] + reverselis[i])
    return maxi - 1

a = [12, 11, 40, 5, 3, 1]
print(lbs(a))