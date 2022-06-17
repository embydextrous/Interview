'''
Given a string S, find the length of the longest balanced subsequence in it. A balanced string is defined as:- 

    A null string is a balanced string.
    If X and Y are balanced strings, then (X)Y and XY are balanced strings.

Examples: 

Input : S = "()())"
Output : 4

()() is the longest balanced subsequence 
of length 4.

Input : s = "()(((((()"
Output : 4
'''
def lvs(s):
    n = len(s)
    invalidOpen = invalidClosed = 0
    for c in s:
        if c == '(':
            invalidOpen += 1
        else:
            if invalidOpen == 0:
                invalidClosed += 1
            else:
                invalidOpen -= 1
    return n - invalidClosed - invalidOpen

s = "))(()"
print(lvs(s))