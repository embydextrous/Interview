def segregate(a):
    l, r = 0, len(a) - 1
    while l < r:
        if a[l] < 0:
            l += 1
            continue
        if a[r] >= 0:
            r -= 1
            continue
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

a = [12, 11, -13, -5, 6, -7, 5, -3, -6]
segregate(a)
print(a)