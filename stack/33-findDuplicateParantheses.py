def findDuplicateParanthesis(exp):
    s = []
    for c in exp:
        if c == ')':
            popCount = 0
            while s.pop() != '(':
                popCount += 1
            if popCount <= 1:
                return True
        else:
            s.append(c)
    return False

exp = "(a+(b)+(c+d))"
print(findDuplicateParanthesis(exp))