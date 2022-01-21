# Also see Count Rotations Divisible By 4
def rotationDivisibleBy8(s):
    n = len(s)
    s += s
    c = 0
    for i in range(n):
        if (100 * int(s[i]) + 10 * int(s[i+1]) + int(s[i+2])) % 8 == 0:
            c += 1
    return c

a = "43292816"
print(rotationDivisibleBy8(a))
