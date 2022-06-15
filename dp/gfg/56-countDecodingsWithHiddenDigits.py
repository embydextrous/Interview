'''
Given an encoded string str consisting of digits and * which can be filled by any digit 1 - 9, the task is to find the number of ways to decode that 
string into a sequence of alphabets A-Z.

Note: The input string contains number from 0-9 and character '*' only. 

Examples: 

    Input: str = “1*” 
    Output: 18 
    Explanation: 
    Since * can be replaced by any value from (1-9), 
    The given string can be decoded as A[A-I] + [J-R] = 9 + 9 ways

    Input: str = “12*3” 
    Output: 28 
'''
def countDecodings(s):
    n = len(s)
    if n == 0:
        return 1
    if s[0] == '0':
        return 0
    p = 1
    q = 9 if s[0] == '*' else 1
    for i in range(2, n + 1):
        newValue = 0
        a, b = s[i-2], s[i-1]
        if b == '*':
            newValue = 9 * q
        elif b != '0':
            newValue = q
        if a == '1' or a == '2':
            if b == '*':
                newValue += (9 if a == '1' else 6) * p
            else:
                if int(a) * 10 + int(b) <= 26:
                    newValue += p
        elif a == '*':
            if b == '*':
                newValue += 15 * p
            elif int(b) <= 6:
                newValue += 2 * p
            else:
                newValue += p
        p, q = q, newValue
    return q

s = "12*3"
print(countDecodings(s))