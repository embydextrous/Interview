# https://www.geeksforgeeks.org/find-index-closing-bracket-given-opening-bracket-expression/
# It is given that i is a valid opening bracket index

def findIndexOfClosingBracket(exp, k):
    s = []
    n = len(exp)
    for i in range(n):
        if exp[i] == "[":
            s.append(i)
        elif exp[i] == "]":
            if s[-1] == k:
                return i
            else:
                s.pop()

exp = "[ABC[23]][89]"
print(findIndexOfClosingBracket(exp, 9))


