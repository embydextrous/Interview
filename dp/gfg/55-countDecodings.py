'''
Let 1 represent A, 2 represents B, etc. Given a digit sequence, count the number of possible decodings of the given digit sequence. 

Examples: 

Input:  digits[] = "121"
Output: 3
// The possible decodings are "ABA", "AU", "LA"

Input: digits[] = "1234"
Output: 3
// The possible decodings are "ABCD", "LCD", "AWD"
'''
# Time Complexity - O(n)
# Space Complexity - O(1)
def countDecodings(s):
    n = len(s)
    if n == 0:
        return 1
    if int(s[0]) == 0:
        return 0
    p, q = 1, 1
    for i in range(2, n + 1):
        a, b = s[i-2], s[i-1]
        newValue = 0
        if a != '0':
            newValue += q
        if a == '1' or a == '2':
            if 10 * int(a) + int(b) <= 26:
                newValue += p
        p, q = q, newValue
    return q    

s = "1234"
print(countDecodings(s))
