'''
https://www.geeksforgeeks.org/return-previous-element-in-an-expanding-matrix/

The problem boils down to finding previous dictionary element.
Here dictionary order is a, b, c, d.

1. Scan from right and if current char is b or d, convert it to a or c and return the string.
2. If it is a or c, convert it to b or d, but now you need to take care of previous element so repeat steps 1 and 2.
'''
def findPattern(s):
    res = ""
    n = len(s)
    for i in range(n-1, -1, -1):
        if s[i] == 'd':
            res = 'c' + res
            return s[:i] + res
        elif s[i] == 'b':
            res = 'a' + res
            return s[:i] + res
        elif s[i] == 'c':
            res = 'd' + res
        else:
            res = 'b' + res
    return res

p = "cca"
print(findPattern(p))

