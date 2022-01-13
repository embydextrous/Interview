# https://www.geeksforgeeks.org/decode-string-recursively-encoded-count-followed-substring/

'''
Input : str[] = "1[b]"
Output : b

Input : str[] = "2[ab]"
Output : abab

Input : str[] = "2[a2[b]]"
Output : abbabb

Input : str[] = "3[b2[ca]]"
Output : bcacabcacabcaca
'''
def isDigit(c):
    return ord(c) - ord('0') >= 0 and ord(c) - ord('0') < 10

def isPattern(s):
    if len(s) > 1:
        print("true")
        return True
    return s[0] != '[' and s[0] != ']' and not isDigit(s[0])

def decode(exp):
    s = []
    for c in exp:
        if c == '[' or isDigit(c):
            s.append(c)
        elif isPattern(c):
            if len(s) > 0 and isPattern(s[-1]):
                s.append(s.pop() + c)
            else:
                s.append(c)
        elif c == ']':
            pat = ""
            while s[-1] != '[':
                pat = s.pop() + pat
            s.pop()
            n = int(s.pop())
            s.append(pat * n)
    return s[-1]
        

exp = "3[b2[ca]]"
print(decode(exp))
