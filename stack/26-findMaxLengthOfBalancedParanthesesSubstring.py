'''
Given a string of open bracket '(' and closed bracket ')'. The task is to find the length
of longest balanced prefix. 
Examples: 
 

Input : S = "((()())())((" 
Output : 10
From index 0 to index 9, they are forming 
a balanced parentheses prefix.

Input : S = "()(())((()"
Output : 6
'''

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

def findMax(exp):
    s = 0
    result = 0
    for i in range(len(exp)):
        if exp[i] == '(':
            s += 1
        else:
            s -= 1
            if s == 0:
                result = max(result, i + 1)
            if s < 0:
                break
    return result


print(findMax("()(())((()"))
