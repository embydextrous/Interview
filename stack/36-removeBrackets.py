# https://www.geeksforgeeks.org/remove-brackets-algebraic-string-containing-operators/
def removeBrackets(exp):
    s = []
    for c in exp:
        if c == ')':
            q = []
            while s[-1] != '(':
                q.append(s.pop())
            s.pop()
            shouldSwitchSign = not (len(s) == 0 or s[-1] == '+')
            while len(q) > 0:
                x = q.pop()
                if x == '+' or x == '-':
                    if shouldSwitchSign:
                        s.append('+' if x == '-' else '-')
                    else:
                        s.append(x)
                else:
                    s.append(x)
        else:
            s.append(c)
    return "".join(s)

'''
s = [a - b + c + d + e - f]
q = [e - d - c - b]
'''

exp = "(a-(b+c)+d)"
print(removeBrackets(exp))

def removeBrackets(exp):
    result = []
    s = [False]
    for i in range(len(exp)):
        c = exp[i]
        if c == '(':
            if i != 0 and exp[i-1] == '-':
                s.append(s[-1] ^ True)
            else:
                s.append(s[-1] ^ False)
        elif c == ')':
            s.pop()
        elif c == '+' or c == '-':
            if not s[-1]:
                result.append(c)
            else:
                result.append('+' if c == '-' else '-')
        else:
            result.append(c)
    return "".join(result)

exp = "((a + b))"
print(removeBrackets(exp))