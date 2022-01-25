def reverse(a):
    l, r = 0, len(a) - 1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

a = [1, 2, 3, 4, 5]
reverse(a)
print(a)