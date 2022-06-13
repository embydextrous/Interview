'''
Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. 
See following examples for more details. 

Consider the following dictionary 
{ i, like, sam, sung, samsung, mobile, ice, 
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes 
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" 
or "i like sam sung".
ilikesamsungmobileicecreammango
'''
def wordBreak(s, words):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] > 0 and s[j:i] in words:
                dp[i] += dp[j]
    return dp[n]

words = set(["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"])
s = "ilikesamsungmobileicecreammango"
print(wordBreak(s, words))

    