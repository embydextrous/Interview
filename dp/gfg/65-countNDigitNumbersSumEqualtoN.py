'''
Given two integers 'n' and 'sum', find count of all n digit numbers with sum of digits as 'sum'. Leading 0's are not counted as digits. 
1 <= n <= 100 and 
1 <= sum <= 500

Example: 

Input:  n = 2, sum = 2
Output: 2
Explanation: Numbers are 11 and 20

Input:  n = 2, sum = 5
Output: 5
Explanation: Numbers are 14, 23, 32, 41 and 50

Input:  n = 3, sum = 6
Output: 21
'''
def C(n, r):
    r = min(r, n - r)
    result = 1
    for i in range(r):
        result *= n - i
        result //= i + 1
    return result

def countNumbers(n, x):
    if n == 1:
        return 1 if x < 10 else 0
    return C(x + n - 1, n - 1) - C(x + n - 2, n - 2)

print(countNumbers(1, 3))