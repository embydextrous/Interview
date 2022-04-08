# Also see, https://www.geeksforgeeks.org/possible-form-triangle-array-values/
def countTriangles(a):
    n = len(a)
    a.sort()
    c = 0
    for i in range(n - 1, 1, -1):
        l = 0
        r = i - 1
        while l < r:
            if a[l] + a[r] > a[i]:
                c += (r - l)
                r -= 1
            else:
                l += 1
    return c

a = [1, 2, 3, 5, 6, 8, 10]
print(countTriangles(a))