# https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/

def rotate(a, i, j):
    x = a[j]
    for k in range(j, i, -1):
        a[k] = a[k-1]
    a[i] = x

def rearrange(a):
    i = 0
    n = len(a)
    while i < n:
        if i % 2 == 0:
            if a[i] < 0:
                i += 1
                continue
            else:
                j = i + 1
                while j < n:
                    if a[j] < 0:
                        break
                    j += 1
                if j == n:
                    return
                rotate(a, i, j)
                i += 2
        else:
            if a[i] > 0:
                i += 1
                continue
            else:
                j = i + 1
                while j < n:
                    if a[j] > 0:
                        break
                    j += 1
                if j == n:
                    return
                rotate(a, i, j)
                i += 2

a = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
rearrange(a)
print(a)
