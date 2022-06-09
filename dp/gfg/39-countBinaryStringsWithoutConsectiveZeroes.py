def countBinaryStrings(n):
    if n == 1:
        return 2
    lastZero, lastOne = 1, 1
    for i in range(2, n + 1):
        lastZero, lastOne = lastOne, lastZero + lastOne
    return lastZero + lastOne

print(countBinaryStrings(4))

