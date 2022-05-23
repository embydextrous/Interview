def maxProductCutting(n):
    if n % 3 == 0:
        return 3 ** (n//3)
    if n % 3 == 2:
        return 3 ** (n//3) * (n%3)
    return 3 ** (n//3 - 1) * 4

n = 17
print(maxProductCutting(10))