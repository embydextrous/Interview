def firstNegativeIntegerInEachWindowOfSizeK(a, k):
    d = []
    n = len(a)
    for i in range(k):
        if a[i] < 0:
            d.append(a[i])
    for i in range(n-k+1):
        if len(d) > 0:
            print(d[0], end = " ")
        else:
            print(0, end = " ")
        if i == n - k:
            break
        exit, enter = a[i], a[k+i]
        if exit == d[0]:
            d.pop(0)
        if enter < 0:
            d.append(enter)
    print()

a = [12, -1, -7, 8, -15, 30, 16, 28]
firstNegativeIntegerInEachWindowOfSizeK(a, 3)



