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
    openCount = closedCount = 0
    result = 0
    for c in s:
        if c == '(':
            openCount += 1
        else:
            closedCount += 1
            result = 2 * min(openCount, closedCount)
    return result

s = "()(((((()"
print(lvs(s))