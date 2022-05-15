'''
Given a binary string s and two integers x and y are given. Task is to arrange the given string in such
a way so that '0' comes X-time then '1' comes Y-time and so on until one of the '0' or '1' is finished. 
Then concatenate rest of the string and print the final string. 
Given : x or y can not be 0
Examples: 
 

Input : s = "0011"
        x = 1
        y = 1
Output : 0101
x is 1 and y is 1. So first we print
'0' one time the '1' one time and 
then we print '0', after printing '0',
all 0's are vanished from the given
string so we concatenate rest of the 
string which is '1'. 

Input : s = '1011011'
        x = 1
        y = 1
Output : 0101111
'''
from collections import Counter

def rearrange(s, x, y):
    a = list(s)
    c = Counter(s)
    result = []
    n = min(c['0'] // x, c['1'] // y)
    for i in range(n):
        result.extend(['1'] * x)
        result.extend(['0'] * y)
    if c['1'] - n * x > 0:
        result.extend(['1'] * (c['1'] - n * x))
    if c['0'] - n * y > 0:
        result.extend(['0'] * (c['0'] - n * y))
    return "".join(result)

s = "10101010101010010010110101001100101100101010010110"
print(Counter(s))
x = 5
y = 3
print(rearrange(s, x, y))