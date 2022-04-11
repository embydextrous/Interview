# https://www.geeksforgeeks.org/construct-binary-palindrome-by-repeated-appending-and-trimming/
'''
Given n and k, Construct a palindrome of size n using a binary number of size k repeating itself to 
wrap into the palindrome. The palindrome must always begin with 1 and contains maximum number of zeros.
Examples : 
 
Input : n = 5,  k = 3
Output : 11011 
Explanation : the 3 sized substring is
110 combined twice and trimming the extra 
0 in the end to give 11011.

Input : n = 2,  k = 8
Output : 11 
Explanation : the 8 sized substring is 11...... 
wrapped to two places to give 11.
'''
from random import randint
def bp(n, k):
    if k > n or n % k == 0:
        return 10 ** (n - 1) + 1
    else:
        x = n % k - 1
        if x == 0:
            return 10 ** (k-1)
        else:
            return (10 ** x + 1) * (10 ** (k - x - 1))

def bp2(n, k):
    if k > n or n % k == 0:
        return 10 ** (n - 1) + 1
    s = [0 for i in range(k)]
    s[0] = 1
    a = [i % k for i in range(n)]
    l, r = 0, n - 1
    while l < r:
        i, j = a[l], a[r]
        if s[i] == 1 or s[j] == 1:
            s[i] = s[j] = 1
        l += 1
        r -= 1
    result = 0
    for i in s:
        result = result * 10 + i
    return result

print(bp2(17, 6))
for i in range(1000):
        n = randint(1, 20)
        k = randint(1, n)
        print(n, k, bp(n, k), bp2(n, k))