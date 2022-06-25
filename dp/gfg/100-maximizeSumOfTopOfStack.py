'''
Given S stacks of length M, the task is to maximize the sum of elements at the top of each stack by popping at most N elements.
Example: 
 

Input: S = 1, N = 3, stacks = { 5, 1, 2, 8, 9 } 
Output: 8 
Explanation: 
Maximum 3 elements can be removed. 
The current element at the top of the stack is 5. 
On removal of 5, the new element at the top is 1. 
On removal of 1, the new element at the top is 2. 
On removal of 2, the new element at the top is 8. 
No further pop operation is allowed. 
Hence, the maximum possible value at the top of the stack is 8.
Input: S = 2, N = 2, stacks = { { 2, 6, 4, 5}, {1, 6, 15, 10} } 
Output: 17 
Explanation: 
Current sum of the elements at the top = 2 + 1 = 3. 
Popping 1 from top of the second stack only makes the sum 8 (5 + 2 = 8) 
Popping 2 from the top of the second stack only makes the sum 7 (6 + 1). 
Popping both 1 and 2 from the top of each stack makes the sum 12 (6 + 6). 
Popping 2 and 6 from the first stack makes the sum 5 (4 + 1). 
Popping 1 and 6 from the second stack leaves 15 as the element at the top. 
Hence, the sum of elements at the top of the two stacks is maximized (15 + 2 = 17). 
'''
def maxSumUtil(stacks, k):
    S = len(stacks)
    dp = [[0 for i in range(k+1)] for j in range(S+1)]
    for i in range(1, S+1):
        for j in range(k+1):
            for m in range(j+1):
                dp[i][j] = max(dp[i][j], dp[i-1][m] + stacks[i-1][j-m])
    return dp[S][k]

stacks = [[2, 6, 4, 5], [1, 6, 15, 10]]
k = 2
print(maxSumUtil(stacks, k))