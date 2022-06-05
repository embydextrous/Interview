'''
Given an expression which contains numbers and two operators '+' and '*', we need to find maximum 
and minimum value which can be obtained by evaluating this expression by different parenthesization. 
Examples: 
 

Input  : expr = “1+2*3+4*5” 
Output : Minimum Value = 27, Maximum Value = 105 
Explanation:
Minimum evaluated value = 1 + (2*3) + (4*5) = 27
Maximum evaluated value = (1 + 2)*(3 + 4)*5 = 105
'''

def maxValue(exp):
    nums = []
    ops = []
    cNum = 0
    for c in exp:
        if c == '*' or c == '+':
            nums.append(cNum)
            ops.append(c)
            cNum = 0
        else:
            cNum = 10 * cNum + int(c)
    nums.append(cNum)
    n = len(nums)
    dp = [[nums[i] if i == j else 0 for i in range(n)] for j in range(n)]
    for s in range(2, n + 1):
        for i in range(n-s+1):
            j = i + s - 1
            for k in range(i, j):
                if ops[k] == '*':
                    dp[i][j] = max(dp[i][j], dp[i][k] * dp[k+1][j])
                else:
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j])
    return dp[0][n-1]

    
exp = "1+2*3+4*5"
print(maxValue(exp))