def findCommon(a, b, c):
    i = j = k = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] and b[j] == c[k]:
            print(a[i], end = " ")
            i += 1
            j += 1
            k += 1
        else:
            if a[i] == min(a[i], b[j], c[k]):
                i += 1
            elif b[j] == min(a[i], b[j], c[k]):
                j += 1
            else:
                k += 1
    print()

a = [1, 5, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80, 120]

findCommon(a, b, c)