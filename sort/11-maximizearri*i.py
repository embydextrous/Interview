def maximize(a):
    a.sort()
    s = 0
    for i in range(len(a)):
        s += i * a[i]
    return s

a = [3, 5, 6, 1]
print(maximize(a))