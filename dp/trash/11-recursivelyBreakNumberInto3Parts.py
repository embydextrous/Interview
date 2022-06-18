'''
Given a number n, we can divide it in only three parts n/2, n/3 and n/4 (we will consider only integer part). The task is to find the maximum sum we can make by dividing number in three parts recursively and summing up them together.
Examples: 
 

Input : n = 12
Output : 13
// We break n = 12 in three parts {12/2, 12/3, 12/4} 
// = {6, 4, 3},  now current sum is = (6 + 4 + 3) = 13 
// again we break 6 = {6/2, 6/3, 6/4} = {3, 2, 1} = 3 + 
// 2 + 1 = 6 and further breaking 3, 2 and 1 we get maximum
// summation as 1, so breaking 6 in three parts produces
// maximum sum 6 only similarly breaking 4 in three   
// parts we can get maximum sum 4 and same for 3 also.
// Thus maximum sum by breaking number in parts  is=13

Input : n = 24
Output : 27
// We break n = 24 in three parts {24/2, 24/3, 24/4} 
// = {12, 8, 6},  now current sum is = (12 + 8 + 6) = 26
// As seen in example, recursively breaking 12 would
// produce value 13. So our maximum sum is 13 + 8 + 6 = 27.
// Note that recursively breaking 8 and 6 doesn't produce
// more values, that is why they are not broken further.

Input : n = 23
Output : 23
// we break n = 23 in three parts {23/2, 23/3, 23/4} = 
// {10, 7, 5}, now current sum is = (10 + 7 + 5) = 22. 
// Since  after further breaking we can not get maximum
// sum hence number is itself maximum i.e; answer is 23
'''
def breakNumber(n, memo):
    if n < 2:
        return 0
    if n in memo:
        return memo[n]
    memo[n] = max(breakNumber(n//2, memo) + breakNumber(n // 3, memo) + breakNumber(n // 4, memo), n)
    return memo[n]

n = 24
memo = {}
print(breakNumber(n, memo))