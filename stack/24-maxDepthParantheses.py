def maxDepth(s):
    st = []
    maxDepth = 0
    for c in s:
        if c == '(':
            st.append(c)
            maxDepth = max(maxDepth, len(st))
        elif c == ')':
            if len(st) == 0 or st[-1] != '(':
                return -1
            else:
                st.pop()
    if len(st) != 0:
        return -1
    return maxDepth

exp = "(b)((c)())"
print(maxDepth(exp))
    
def maxDepth2(exp):
    s = 0
    result = 0
    for c in exp:
        if c == '(':
            s += 1
            result = max(result, s)
        elif c == ')':
            s -= 1
    return result if s == 0 else -1

print(maxDepth2(exp))
