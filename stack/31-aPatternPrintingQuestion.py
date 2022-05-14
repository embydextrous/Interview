# https://www.geeksforgeeks.org/form-minimum-number-from-given-sequence/
def findMinimumNumber(s):
    n = len(s)
    result = 0
    current = 1
    i = 0
    while i < n:
        if s[i] == 'I':
            result = result * 10 + current
            current += 1
            i += 1
        else:
            k = current
            while i < n and s[i] == 'D':
                current += 1
                i += 1
            for x in range(current, k - 1, -1):
                result = result * 10 + x
            current += 1
            i += 1
    if s[-1] == 'I':
        result = result * 10 + current
    return result

s = "DDIDDIID"
print(findMinimumNumber("DID"))
print(findMinimumNumber("DIDIII"))
print(findMinimumNumber("DDDIIDI"))
print(findMinimumNumber("IDIDIID"))
print(findMinimumNumber("DIIDIDD"))
print(findMinimumNumber("IIDIDDD"))
