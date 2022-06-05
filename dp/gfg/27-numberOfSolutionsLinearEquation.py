'''
Given a linear equation of n variables, find number of non-negative integer solutions of it. For example, 
let the given equation be “x + 2y = 5”, solutions of this equation are “x = 1, y = 2”, “x = 5, y = 0” 
and “x = 3, y = 1”. It may be assumed that all coefficients in given equation are positive integers.
Example : 
 
Input:  coeff[] = {1, 2}, rhs = 5
Output: 3
The equation "x + 2y = 5" has 3 solutions.
(x=3,y=1), (x=1,y=2), (x=5,y=0)

Input:  coeff[] = {2, 2, 3}, rhs = 4
Output: 3
The equation "2x + 2y + 3z = 4"  has 3 solutions.
(x=0,y=2,z=0), (x=2,y=0,z=0), (x=1,y=1,z=0)
'''
def numSolutions(coeff, k):
    dp = [0] * (k + 1)
    dp[0] = 1
    for d in coeff:
        for i in range(d, k + 1):
            dp[i] += dp[i-d]
    print(dp)
    return dp[k]

coeff = [2, 2, 3]
k = 5
print(numSolutions(coeff, k))
