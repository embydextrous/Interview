# https://www.geeksforgeeks.org/identify-mark-unmatched-parenthesis-expression/
'''
Given an expression, find and mark matched and unmatched parenthesis in it. 
We need to replace all balanced opening parenthesis with 0, 
balanced closing parenthesis with 1, and all unbalanced with -1.
Examples:  

Input : ((a) 
Output : -10a1

Input : (a))
Output : 0a1-1

Input  : (((abc))((d)))))
Output : 000abc1100d111-1-1
'''
def identifyAndReplace(exp):
    n = len(exp)
    q = list(exp)
    s = []
    for i in range(n):
        c = exp[i]
        if c == '(':
            s.append(i)
        elif c == ')':
            if len(s) == 0:
                q[i] = "-1"
            else:
                q[i] = "1"
                q[s.pop()] = "0"
    while len(s) > 0:
        q[s.pop()] = "-1"
    return "".join(q)

exp = "(((abc))((d)))))"
print(identifyAndReplace(exp))
