operatorsOrder = {'+':0, '-':0, '*':1, '/': 1, '^': 2}
operators = set(['+', '-', '*', '/', '^'])
parantheses = set(['(', ')'])

def isOperand(c):
    return c not in operators and c not in parantheses

def isOperator(c):
    return c in operators

def isOpenParantheses(c):
    return c == '('

def isCloseParantheses(c):
    return c == '('

def isParantheses(c):
    return c in parantheses

def infixToPostFix(exp):
    s = []
    result = []
    for c in exp:
        # if operand just append to result
        if isOperand(c):
            result.append(c)
        # if parantheses
        elif isParantheses(c):
            # if open parantheses just append
            if isOpenParantheses(c):
                s.append(c)
            # if closed parantheses pop until there
            else:
                while len(s) > 0:
                    v = s.pop()
                    if isCloseParantheses(v):
                        break
                    result.append(v)
        else:
            if len(s) == 0 or isOpenParantheses(s[len(s) - 1]) or operatorsOrder[s[len(s) - 1]] < operatorsOrder[c]:
                s.append(c)
            else:
                while len(s) > 0:
                    if isParantheses(s[len(s) - 1]):
                        break
                    elif operatorsOrder[s[len(s) - 1]] >= operatorsOrder[c]:
                        result.append(s.pop())
                s.append(c)
    while len(s) > 0:
        result.append(s.pop())
    return "".join(result)

def prefixToInfix(exp):
    s = []
    exp = exp[::-1]
    for c in exp:
        if isOperator(c):
            a = s.pop()
            b = s.pop()
            res = "(" + a + c + b + ")"
            s.append(res)
        else:
            s.append(c)
    return s[0]

def prefixToPostfix(exp):
    s = []
    exp = exp[::-1]
    for c in exp:
        if isOperator(c):
            a = s.pop()
            b = s.pop()
            res = a + b + c
            s.append(res)
        else:
            s.append(c)
    return s[0]

def posfixToPrefix(exp):
    s = []
    for c in exp:
        if isOperator(c):
            a = s.pop()
            b = s.pop()
            res = c + b + a
            s.append(res)
        else:
            s.append(c)
    return s[0]

def posfixToInfix(exp):
    s = []
    for c in exp:
        if isOperator(c):
            a = s.pop()
            b = s.pop()
            res = "(" + b + c + a + ")"
            s.append(res)
        else:
            s.append(c)
    return s[0]

def infixToPrefix(exp):
    postFixExp = infixToPostFix(exp)
    return posfixToPrefix(postFixExp)

exp = "a+b*(c^d-e)^(f+g*h)-i"
print(infixToPrefix(exp))
print(infixToPostFix(exp))
#print(posfixToPrefix(prefixToPostfix(exp)))
#print(posfixToInfix(prefixToPostfix(exp)))

# -
# abcd^e-fgh*+^*+i-
