def check(a):
    if len(a) == 0:
        return True
    n = len(a)
    mini = maxi = a[n-1]
    for i in range(n-2, -1, -1):
        if a[i] < mini:
            mini = a[i]
        elif a[i] > maxi:
            maxi = a[i]
        else:
            return False
    return True

a = [5123, 3300, 783, 1111, 890]
print(check(a))