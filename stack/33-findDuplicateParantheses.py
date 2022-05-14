'''
Given a balanced expression, find if it contains duplicate parenthesis or not. A set of parenthesis are duplicate if the same subexpression is surrounded by multiple parenthesis. 

Examples: 

Below expressions have duplicate parenthesis - 
((a+b)+((c+d)))
The subexpression "c+d" is surrounded by two
pairs of brackets.

(((a+(b)))+(c+d))
The subexpression "a+(b)" is surrounded by two 
pairs of brackets.

(((a+(b))+c+d))
The whole expression is surrounded by two 
pairs of brackets.

((a+(b))+(c+d))
(b) and ((a+(b)) is surrounded by two
pairs of brackets.

Below expressions don't have any duplicate parenthesis -
((a+b)+(c+d)) 
No subsexpression is surrounded by duplicate
brackets.
'''
def hasDuplicateParantheses(exp):
    s = []
    for c in exp:
        if c == ')':
            popCount = 0
            while s[-1] != '(':
                popCount += 1
                s.pop()
            if popCount <= 1:
                return True
            s.pop()
        else:
            s.append(c)
    return False

exp = "(a+b+(c+d))"
print(hasDuplicateParantheses(exp))