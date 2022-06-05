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
    M = [[True for i in range(n)] for j in range(n)]
    maxSize = 1
    x = 0
    for size in range(2, n + 1):
        for i in range(n - size + 1):
            j = i + size - 1
            M[i][j] = s[i] == s[j] and M[i+1][j-1]
            if M[i][j]:
                maxSize = size
                x = i
    print(s[x:x+maxSize])
    return maxSize

s = "forgeeksskeegfor"
print(lps(s))