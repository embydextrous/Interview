def russianPheasantMultiplication(a, b):
    res = 0
    while b > 0:
        if b & 1 == 1:
            res += a
        b >>= 1
        a <<= 1
    return res

print(russianPheasantMultiplication(18, 3))