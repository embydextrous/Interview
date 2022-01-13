def findMaxLength(exp):
    st = [-1]
    result = 0
    for i in range(len(exp)):
        if exp[i] == '(':
            st.append(i)
        else:
            if len(st) != 0:
                st.pop()
            if len(st) != 0:
                result = max(result, i - st[-1])
            else:
                st.append(i)
    return result

print(findMaxLength("()(()))))"))
