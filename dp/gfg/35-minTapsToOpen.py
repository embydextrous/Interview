'''
There is a one-dimensional garden of length N. In each position of the N length garden, a fountain has been installed. Given an array a[]such that a[i] describes 
the coverage limit of ith fountain. A fountain can cover the range from the position max(i - a[i], 1) to min(i + a[i], N). In beginning, all the fountains are switched off. 
The task is to find the minimum number of fountains needed to be activated such that the whole N-length garden can be covered by water.

Examples:

Input: a[] = {1, 2, 1}
Output: 1
Explanation:
For position 1: a[1] = 1, range = 1 to 2
For position 2: a[2] = 2, range = 1 to 3
For position 3: a[3] = 1, range = 2 to 3
Therefore, the fountain at position a[2] covers the whole garden.
Therefore, the required output is 1.

Input: a[] = {2, 1, 1, 2, 1} 
Output: 2  (open first fountain and fourth fountain)

Input: a[] = {2, 1, 2, 1, 1} 
Output: 1 (open third fountain)

Input: a[] = {0, 0, 0, 0} 
Output: 4 (open all)

Input: a[] = {3, 4, 1, 1, 0, 0} 
Output: 1 (open second fountain)
'''
def minFountain(a):
    n = len(a)
    dp = [-1] * n
    for i in range(n):
        left = max(0, i - a[i])
        right = min(n - 1, i + a[i])
        dp[left] = max(dp[left], right)
    count = 0
    idxNext = 0
    idxRight = 0
    for i in range(n):
        idxNext = max(idxNext, dp[i])
        if i == idxRight:
            count += 1
            idxRight = idxNext + 1
    return count

a = [1, 2, 1, 1, 2, 1, 0, 1, 0, 2, 1, 2, 1, 0]
print(minFountain(a))

a = [3, 4, 1, 1, 0, 0, 0]
print(minFountain(a))

a = [0, 0, 0, 0]
print(minFountain(a))