'''
Given a text and a wildcard pattern, implement wildcard pattern matching algorithm that finds if wildcard pattern is matched with text. 
The matching should cover the entire text (not partial text). The wildcard pattern can include the characters '?' and '*' 

    '?' - matches any single character 
    '*' - Matches any sequence of characters (including the empty sequence)

For example:

Text = "baaabab",
Pattern = “*****ba*****ab", output : true
Pattern = "baaa?ab", output : true
Pattern = "ba*a?", output : true
Pattern = "a*ab", output : false 
'''
def wilcardPatternMatching(text, pattern):
    n, m = len(pattern), len(text)
    if n == 0 and m == 0:
        return True
    if n == 0:
        return False
    if m == 0:
        charsInPattern = set(pattern)
        return len(charsInPattern) == 1 and '*' in charsInPattern
    dp = [[False for i in range(m+1)] for j in range(n+1)]
    for i in range(n, -1, -1):
        trueObserved = False
        for j in range(m, -1, -1):
            if i != n and not trueObserved:
                trueObserved = dp[i+1][j]
            if i == n:
                dp[i][j] = j == m
            elif j == m:
                dp[i][j] = False if pattern[i-1] != '*' else dp[i+1][j]
            else:
                cPat = pattern[i-1]
                cText = text[j-1]
                if cPat == '?':
                    dp[i][j] = dp[i+1][j+1]
                elif cPat == '*':
                    dp[i][j] = trueObserved
                else:
                    dp[i][j] = cPat == cText and dp[i+1][j+1]
    return dp[0][0]

pattern = "a*ab"
text = "baaabab"

print(wilcardPatternMatching(text, pattern))
            


