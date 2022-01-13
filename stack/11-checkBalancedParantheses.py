from stack import Stack

def checkBalanced(exp):
    s = Stack()
    for c in exp:
        if c == '{' or c =='[' or c == '(':
            s.push(c)
        else:
            v = s.pop()
            if c == '}' and v != '{':
                return False
            if c == ']' and v != '[':
                return False
            if c == ')' and v != '(':
                return False
    return s.isEmpty()

a = "[()]{[()(]()}"
print(checkBalanced(a))