def moveZeroesToEnd(a):
    l, r = 0, len(a) - 1
    while l < r:
        if a[l] != 0:
            l += 1
            continue
        if a[r] == 0:
            r -= 1
            continue
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

a = [1, 2, 0, 0, 0, 3, 6]
moveZeroesToEnd(a)
print(a)