# https://www.geeksforgeeks.org/find-index-closing-bracket-given-opening-bracket-expression/
# It is given that i is a valid opening bracket index

def findIndexOfClosingBracket(exp, k):
    s = 0
    n = len(exp)
    for i in range(k, n):
        if exp[i] == "[":
            s += 1
        elif exp[i] == "]":
            s -= 1
            if s == 0:
                return i

exp = "[ABC[23]][89]"
print(findIndexOfClosingBracket(exp, 9))


