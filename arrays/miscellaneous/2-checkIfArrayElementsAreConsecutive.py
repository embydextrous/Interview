def checkIfConsecutive(a):
    xorValue = 0
    for i in range(min(a), max(a) + 1):
        xorValue ^= i
    for i in a:
        xorValue ^= i
    return xorValue == 0

a = [5, 2, 1, 4, 6]
print(checkIfConsecutive(a))