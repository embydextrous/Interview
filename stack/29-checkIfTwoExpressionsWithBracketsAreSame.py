'''
Given two expressions in the form of strings. The task is to compare them and check if they are similar. 
Expressions consist of lowercase alphabets, '+', '-' and '( )'.
Examples: 
 
Input  : exp1 = "-(a+b+c)"
         exp2 = "-a-b-c"
Output : Yes

Input  : exp1 = "-(c+b+a)"
         exp2 = "-c-b-a"
Output : Yes

Input  : exp1 = "a-b-(c-d)"
         exp2 = "a-b-c-d"
Output : No
'''
MAX_OPERANDS = 26

def checkLocalSign(s, i):
    if i == 0:
        return True
    if s[i - 1] == "-":
        return False
    return True

def evaluateSignsOfAll(exp):
    allOperandsSign = [0] * MAX_OPERANDS
    s = [True]
    for i in range(len(exp)):
        if exp[i] == "(":
            s.append(checkLocalSign(exp, i))
        elif exp[i] == ")":
            s.pop()
        elif exp[i] != '-' and exp[i] != '+':
            if s[-1]:
                allOperandsSign[ord(exp[i]) - ord('a')] = 1 if checkLocalSign(exp, i) else -1
            else:
                allOperandsSign[ord(exp[i]) - ord('a')] = -1 if checkLocalSign(exp, i) else 1
    return allOperandsSign

def check(exp1, exp2):
    return evaluateSignsOfAll(exp1) == evaluateSignsOfAll(exp2)


exp1 = "-(a+b+c)"
exp2 = "-a-b-c"
print(check(exp1, exp2))
