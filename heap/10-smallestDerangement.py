import heapq

'''
Given the sequence 

\ S = {1, 2, 3 \dots N}
find the lexicographically smallest (earliest in dictionary order) derangement of 
\ S
A derangement of S is as any permutation of S such that no two elements in S and its permutation occur at same position.

Examples:   

Input: 3
Output : 2 3 1
Explanation: The Sequence is 1 2 3.
Possible permutations are (1, 2, 3), (1, 3, 2),
          (2, 1, 3), (2, 3, 1), (3, 1, 2) (3, 2, 1).
Derangements are (2, 3, 1), (3, 1, 2).
Smallest Derangement: (2, 3, 1)

Input : 5
Output : 2 1 4 5 3.
Explanation: Out of all the permutations of 
(1, 2, 3, 4, 5), (2, 1, 4, 5, 3) is the first derangement.
'''

# for n = 3 sequence is 123, for n = 4 sequence is 1234
def smallestDerangement(n):
    result = [i for i in range(1, n+1)]
    j = 0
    while j < n - 1:
        result[j+1], result[j] = result[j], result[j+1]
        j += 2
    if j == n - 1:
        result[j], result[j-1] = result[j-1], result[j]
    return result

print(smallestDerangement(5))

