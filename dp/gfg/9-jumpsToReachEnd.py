'''
Given an array of integers where each element represents the max number of steps that can be made
forward from that element. Write a function to return the minimum number of jumps to reach the end
of the array (starting from the first element). If an element is 0, they cannot move through that element.
If the end isn't reachable, return -1.

Examples: 

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 9 -> 9)
Explanation: Jump from 1st element 
to 2nd element as there is only 1 step, 
now there are three options 5, 8 or 9. 
If 8 or 9 is chosen then the end node 9 
can be reached. So 3 jumps are made.

Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
Output: 10
Explanation: In every step a jump 
is needed so the count of jumps is 10.
'''
def minJumps(a):
    n = len(a)
    dp = [10 ** 9] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if a[j] >= i - j and dp[j] + 1 < dp[i]:
                dp[i] = dp[j] + 1
    return dp[n-1]

a = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(a))

a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(minJumps(a))
