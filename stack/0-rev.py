from base64 import decode
from collections import deque

parantheses = set(['(', ')'])
operators = {'-':0, '+':0, '*':1, '/':1, '^':2}

def isOperator(c):
    return c in operators

def isParantheses(c):
    return c in parantheses

def isOperand(c):
    return not isOperator(c) and not isParantheses(c)

# 31 (power revision)
def infixToPostfix(exp):
    s = []
    result = []
    for c in exp:
        if isOperand(c):
            result.append(c)
        elif isParantheses(c):
            if c == '(':
                s.append(c)
            else:
                while len(s) > 0:
                    v = s.pop()
                    if v == '(':
                        break
                    result.append(v)
        else:
            if len(s) == 0 or s[-1] == '(' or operators[c] > operators[s[-1]]:
                s.append(c)
            else:
                while len(s) > 0 and s[-1] != '(' and operators[s[-1]] >= operators[c]:
                    result.append(s.pop())
                s.append(c)
    while len(s) > 0:
        result.append(s.pop())
    return "".join(result)

def prefixToInfix(exp):
    exp = exp[::-1]
    s = []
    for c in exp:
        if isOperand(c):
            s.append(c)
        else:
            a = s.pop()
            b = s.pop()
            s.append(f"({a}{c}{b})")
    return s[0]

def postfixToInfix(exp):
    s = []
    for c in exp:
        if isOperand(c):
            s.append(c)
        else:
            b = s.pop()
            a = s.pop()
            s.append(f"({a}{c}{b})")
    return s[0]

def prefixToPostfix(exp):
    exp = exp[::-1]
    s = []
    for c in exp:
        if isOperand(c):
            s.append(c)
        else:
            a = s.pop()
            b = s.pop()
            s.append(f"{a}{b}{c}")
    return s[0]

def postfixToPrefix(exp):
    s = []
    for c in exp:
        if isOperand(c):
            s.append(c)
        else:
            a = s.pop()
            b = s.pop()
            s.append(f"{c}{b}{a}")
    return s[0]

def infixToPrefix(exp):
    return postfixToPrefix(infixToPostfix(exp))

infixexp = "a+b*(c^d-e)^(f+g*h)-i"
prefixexp = "-+a*b^-^cde+f*ghi"
postfixexp = "abcd^e-fgh*+^*+i-"
print(infixToPostfix(infixexp))
print(prefixToInfix(prefixexp))
print(postfixToInfix(postfixexp))
print(prefixToPostfix(prefixexp))
print(postfixToPrefix(postfixexp))
print(infixToPrefix(infixexp))


def minReversals(exp):
    uoc = ucc = 0
    s = []
    for c in exp:
        if c == '{':
            s.append(c)
            uoc += 1
        elif c == '}':
            if len(s) > 0 and s[-1] == '{':
                s.pop()
                uoc -= 1
            else:
                s.append(c)
                ucc += 1
    if len(s) % 2 == 1:
        return -1
    return (1 + ucc) // 2 + (1 + uoc) // 2

exp = "{{}}"
print(minReversals(exp))

def identifyAndReplace(exp):
    a = list(exp)
    s = []
    for i in range(len(a)):
        c = a[i]
        if c == '(':
            s.append(i)
        elif c == ')':
            if len(s) > 0:
                a[s.pop()] = '0'
                a[i] = '1'
            else:
                a[i] = '-1'
    while len(s) > 0:
        a[s.pop()] = '-1'
    return "".join(a)

exp = "(((abc))((d)))))"
print(identifyAndReplace(exp))




exp = "(((abc))((d)))))"

def findIndex(exp, i):
    s = 0
    for k in range(i, len(exp)):
        c = exp[k]
        if c == '[':
            s += 1
        elif c == ']':
            s -= 1
            if s == 0:
                return k

exp = "[ABC[23]][89]"
print(findIndex(exp, 9))

def hasDuplicateParantheses(exp):
    s = []
    for c in exp:
        if c == ')':
            popCount = 0
            while len(s) > 0 and s[-1] != '(':
                popCount += 1
                s.pop()
            if popCount <= 1:
                return True
            s.pop()
        else:
            s.append(c)
    return False

exp = "(a+b+((c+d)))"
print(hasDuplicateParantheses(exp))

def isDigit(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')

# "3[b2[ca]]"
def decodeString(exp):
    s = []
    for c in exp:
        if isDigit(c):
            if len(s) == 0 or not isDigit(s[-1]):
                s.append(c)
            else:
                s.append(s.pop() + c)
        elif c == '[':
            continue
        elif c == ']':
            pat = s.pop()
            times = int(s.pop())
            if len(s) > 0:
                s.append(s.pop() + (pat * times))
            else:
                s.append(pat * times)
        else:
            if len(s) == 0 or isDigit(s[-1]):
                s.append(c)
            else:
                s.append(s.pop() + c)   
    return s[0]

exp = '3[b2[ca]]'
print(decodeString(exp))

def findNumbers(n):
    if n <= 9:
        for i in range(n):
            print(i + 1, end = " ")
        print()
        return
    q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    continueScan = True
    while continueScan:
        x = q.popleft()
        print(x, end = " ")
        r = x % 10
        for i in range(r, 10):
            num = 10 * x + i
            if num > n:
                continueScan = False
                break
            q.append(num)
    while len(q) > 0:
        print(q.popleft(), end = " ")
    print()

findNumbers(100)

