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
    for c in exp:
        if c == '*' or c == '+':
            ops.append(c)
        else:
            nums.append(int(c))
    n = len(nums)
    dp = [[nums[i] if i == j else 0 for i in range(n)] for j in range(n)]
    for s in range(2, n + 1):
        i = 0
        j = i + s - 1
        while j < n:
            for k in range(i, j):
                print(i, j, k, dp[i][k], dp[k][j], ops[k])
                if ops[k] == '*':
                    dp[i][j] = max(dp[i][j], dp[i][k] * dp[k+1][j])
                else:
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j])
            i += 1
            j += 1
    for row in dp:
        print(row)
    return dp[0][n-1]

    
exp = "1+2*3+4*5"
print(maxValue(exp))