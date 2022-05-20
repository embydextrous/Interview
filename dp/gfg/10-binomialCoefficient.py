def binomialCoefficient(n, r):
    r = min(r, n - r)
    result = 1
    for i in range(r):
        result *= (n - i)
        result //= i+1
    return result

print(binomialCoefficient(10, 5))
