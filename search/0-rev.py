# 1 3 5 6 7 9 10
# 11 12 13 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27 28 29 30
# 31 32 33 34 35 36 37 38 39 40
# 41 42 43 44 45 46 47 48 49 50
# 51 52
def findTwoRepeating(a):
    n = len(a) + 2
    xor = 0
    for i in a:
        xor ^= i
    for i in range(1, n + 1):
        xor ^= i
    x = y = 0
    fsb = xor & ~(xor-1)
    print(xor, fsb)
    for i in a:
        if (i & fsb == 0):
            x ^= i
        else:
            y ^= i
    for i in range(1, n + 1):
        if (i & fsb == 0):
            x ^= i
        else:
            y ^= i
    return (x, y)

a = [7, 9, 1, 6, 2, 8, 5]
print(findTwoRepeating(a))
