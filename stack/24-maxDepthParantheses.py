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

exp = "(b)((c)()"
print(maxDepth(exp))
    
