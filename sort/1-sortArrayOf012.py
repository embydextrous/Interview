# In single pass. For two passes you can simply count frequency of 0, 1 and 2 an d update.

def sort(a):
    n = len(a)
    l = 0
    m = 0
    r = n - 1
    while m <= r:
        if a[m] == 0:
            a[l], a[m] = a[m], a[l]
            l += 1
            m += 1
        elif a[m] == 1:
            m += 1
        else:
            a[m], a[r] = a[r], a[m]
            r -= 1

a = [2, 2, 1, 0, 0, 1, 0, 2, 0, 1, 0, 2, 0]
sort(a)
print(a)
