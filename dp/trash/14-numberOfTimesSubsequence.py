'''
Given two strings, find the number of times the second string occurs in the first string, 
whether continuous or discontinuous.

Examples: 

Input:  
string a = "GeeksforGeeks"
string b = "Gks"

Output: 4

Explanation:  
The four strings are - (Check characters marked in bold)
GeeksforGeeks
GeeksforGeeks
GeeksforGeeks
GeeksforGeeks
'''
def countTimesUtil(a, b, idxA, idxB, dp):
    if (idxA == 0 and idxB == 0) or idxB == 0:
        return 1
    if idxA == 0:
        return 0
    if dp[idxA][idxB] != -1:
        return dp[idxA][idxB]
    result = 0
    if a[idxA-1] == b[idxB-1]:
        result += countTimesUtil(a, b, idxA - 1, idxB - 1, dp) + countTimesUtil(a, b, idxA - 1, idxB, dp)
    else:
        result += countTimesUtil(a, b, idxA - 1, idxB, dp)
    dp[idxA][idxB] = result
    return result

a = "geeksforgeeks"
b = "gks"
n, m = len(a), len(b)
dp = [[-1 for i in range(m+1)] for j in range(n+1)]
print(countTimesUtil(a, b, n, m, dp)) 