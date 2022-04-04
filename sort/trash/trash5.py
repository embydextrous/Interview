# https://www.geeksforgeeks.org/sum-minimum-absolute-difference-array-element/

def findMinSum(a):
    a.sort()
    n = len(a)
    s = 0
    for i in range(n):
        if i == 0:
            s += a[1] - a[0]
        elif i == n - 1:
            s += a[n - 1] - a[n - 2]
        else:
            s += min(a[i] - a[i - 1], a[i + 1] - a[i])
    return s

a = [12, 10, 15, 22, 21, 20, 1, 8, 9]
print(findMinSum(a))