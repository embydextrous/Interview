'''
Given a number n, print n-th Fibonacci Number. 

Examples: 

Input  : n = 2
Output : 1

Input  : n = 9
Output : 34
'''
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return b

print(fib(10))