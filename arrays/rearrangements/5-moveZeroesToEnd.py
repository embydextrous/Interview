# Maintain order - voila
def moveZeroesToEnd(a):
    n = len(a)
    for i in range(n):
        if a[i] != 0:
            l = i
            r = -1
            for j in range(i + 1, n):
                if a[j] == 0:
                    r = j
                    break
            if r == -1:
                break
            for i in range(r, l, -1):
                a[i] = a[i-1]
            a[l] = 0

a = [1, 2, 0, 0, 0, 3, 6]
# [1, 2, 0, 0, 0, 3, 6lr]
moveZeroesToEnd(a)
print(a)