# https://www.geeksforgeeks.org/check-whether-arithmetic-progression-can-formed-given-array/

def check(a):
    n = len(a)
    if n <= 2:
        return True
    a.sort()
    d = a[1] - a[0]
    for i in range(2, n):
        if a[i] - a[i-1] != d:
            return False
    return True

a = [20, 15, 5, 1, 10]
print(check(a))
