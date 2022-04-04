def minimizeSumOfProducts(a, b):
    a.sort()
    b.sort()
    p = 0
    n = len(a)
    for i in range(n):
        p += a[i] * b[n - i - 1]
    return p

a =[6, 1, 9, 5, 4]
b = [3, 4, 8, 2, 4]
print(minimizeSumOfProducts(a, b))