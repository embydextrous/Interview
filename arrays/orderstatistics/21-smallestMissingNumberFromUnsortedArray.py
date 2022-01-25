def segregateNonNegativeAndPositive(a):
    l, r = 0, len(a) - 1
    while l < r:
        if a[l] <= 0 and a[r] > 0:
            a[l], a[r] = a[r], a[l]
            r -= 1
            l += 1
        elif a[l] > 0:
            l += 1
        else:
            r -= 1

def findMinPositiveNumber(a):
    n = len(a)
    segregateNonNegativeAndPositive(a)
    for i in a:
        if i - 1 >= 0 and i - 1 < len(a):
            a[i-1] = -1
    for i in range(n):
        if a[i] > 0:
            return i + 1
    return n + 1

a = [1, 2, 3, 4, 5]
print(findMinPositiveNumber(a))
        