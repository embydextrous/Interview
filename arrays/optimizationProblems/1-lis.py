def lis(a):
    n = len(a)
    l = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and l[j] + 1 > l[i]:
                l[i] = l[j] + 1
    print(l)
    return max(l)

a = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
print(lis(a))
