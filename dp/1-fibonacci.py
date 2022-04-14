'''
fib(n) = n for n < 2
fib(n) = fib(n-1) + fib(n-2) for n >= 2
'''
def fib(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

print(fib(10))