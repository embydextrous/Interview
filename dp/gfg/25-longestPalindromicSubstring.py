'''
Given a string, find the longest substring which is palindrome. 

For example, 

Input: Given string :"forgeeksskeegfor", 
Output: "geeksskeeg"

Input: Given string :"Geeks", 
Output: "ee"
'''

def lps(s):
    n = len(s)
    dp = [[True for j in range(n)] for i in range(n)]
    x, y = 0, 0
    size = 1
    for i in range(1, n):
        for j in range(n-i):
            dp[j][j+i] = s[j] == s[j+i] and dp[j+1][j+i-1]
            if dp[j][j+i] and i + 1 > size:
                size = i + 1
                x, y = j, j+i
    print(s[x:y+1])
    return size

s = "forgeeksskeegfor"
print(lps(s))