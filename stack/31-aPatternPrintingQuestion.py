# https://www.geeksforgeeks.org/form-minimum-number-from-given-sequence/
def findMinimumNumber(a):
    result = ""
    current = 1
    i = 0
    while i < len(a):
        c = a[i]
        if c == 'I':
            result = result + str(current)
            current += 1
        else:
            dCount = 0
            j = i
            while j < len(a) and a[j] == 'D':
                dCount += 1
                j += 1
            k = current + dCount
            for y in range(k, current - 1, -1):
                result = result + str(y)
            current = k + 1
        i = current - 1
    if i == len(a):
        result += str(current)
    return result

s = "DDIDDIID"
print(findMinimumNumber("DIDID"))
print(findMinimumNumber("DIDIII"))
print(findMinimumNumber("DDDIIDI"))
print(findMinimumNumber("IDIDIID"))
print(findMinimumNumber("DIIDIDD"))
print(findMinimumNumber("IIDIDDD"))