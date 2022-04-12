'''
Given an array of n distinct elements, find the minimum number of swaps required to sort the array.

Examples: 

Input: {4, 3, 2, 1}
Output: 2
Explanation: Swap index 0 with 3 and 1 with 2 to 
              form the sorted array {1, 2, 3, 4}.

Input: {1, 5, 4, 3, 2}
Output: 2
'''
# Also see, https://www.geeksforgeeks.org/minimum-swap-required-convert-binary-tree-binary-search-tree/

def minSwaps(a):
    n = len(a)
    arrPos = [[a[i], i] for i in range(n)]
    arrPos.sort(key = lambda x : x[0])
    # to add index
    visited = set()
    result = 0
    i = 0
    while i < n:
        cycleSize = 0
        while i not in visited:
            cycleSize += 1
            visited.add(i)
            i = arrPos[i][1]
        result += max(0, cycleSize - 1)
        i += 1 
    return result
            
a = [101, 758, 315, 730, 472, 619, 460, 479]
# 101 315 460 472 479 619 730 758
print(minSwaps(a))