def sort(a):
    l, r = 0, len(a) - 1
    while l < r:
        if a[l] == 0:
            l += 1
        elif a[r] == 1:
            r -= 1
        else:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1

a = [0, 0, 0, 1, 0, 0, 1, 0]
sort(a)
print(a)