def minReversals(exp):
    unbalancedOpenCount = 0
    unbalancedClosedCount = 0
    s = []
    for c in exp:
        if c == '{':
            unbalancedOpenCount += 1
            s.append(c)
        else:
            if len(s) > 0:
                if s[-1] == '{':
                    s.pop()
                    unbalancedOpenCount -= 1
                else:
                    s.append(c)
                    unbalancedClosedCount += 1
            else:
                s.append(c)
                unbalancedClosedCount += 1
    if len(s) % 2 != 0:
        return -1
    return (1 + unbalancedOpenCount) // 2 + (1 + unbalancedClosedCount) // 2

s = "}}}"
print(minReversals(s))
