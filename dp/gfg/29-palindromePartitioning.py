'''
Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition
is a palindrome. For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”. 
Determine the fewest cuts needed for a palindrome partitioning of a given string. For example, minimum of 3
cuts are needed for “ababbbabbababa”. The three cuts are “a|babbbab|b|ababa”. If a string is a palindrome, 
then minimum 0 cuts are needed. If a string of length n containing all different characters, then minimum 
n-1 cuts are needed. 

Examples :  

Input : str = “geek” 
Output : 2 
We need to make minimum 2 cuts, i.e., “g ee k”
Input : str = “aaaa” 
Output : 0 
The string is already a palindrome.
Input : str = “abcde” 
Output : 4
Input : str = “abbac” 
Output : 1 

a bb
ab b
# 0, 0 -> 1, 1

0   1   1   0   1
x   0   0   1   2
x   x   0   1   2
x   x   x   0   1
x   x   x   x   0
'''
def palindromePartition(s):
    n = len(s)
    lps = [[True for i in range(n)] for j in range(n)]
    for i in range(1, n):
        for j in range(n-i):
            lps[j][j+i] = s[j] == s[j+i] and lps[j+1][j+i-1]
    for row in lps:
        print(row)
    dp = [10**9] * n
    dp[0] = 0
    for i in range(1, n):
        if lps[0][i]:
            dp[i] = 0
            continue
        for j in range(i, -1, -1):
            if lps[j][i]:
                dp[i] = min(dp[i], 1 + dp[j-1])
    print(dp)
    return max(dp)

s = "abbac"
print(palindromePartition(s))
