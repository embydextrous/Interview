'''
Given a string consisting of opening and closing parenthesis, find the length of the longest valid parenthesis substring.

Examples: 

Input : ((()
Output : 2
Explanation : ()

Input: )()())
Output : 4
Explanation: ()() 

Input:  ()(()))))
Output: 6
Explanation:  ()(())
'''
def lvs(s):
    maxi = 0
    left = right = 0
    for c in s:
        if c == '(':
            left += 1
        else:
            right += 1
            if left == right:
                maxi = max(maxi, 2 * right)
            elif right > left:
                left = right = 0
    n = len(s)
    left = right = 0
    for i in range(len(s)):
        c = s[n-i-1]
        if c == ')':
            right += 1
        else:
            left += 1
            if left == right:
                maxi = max(maxi, 2 * left)
            elif left > right:
                left = right = 0
    return maxi

s = "()(()))))"
print(lvs(s))
