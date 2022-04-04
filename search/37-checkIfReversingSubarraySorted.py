# https://www.geeksforgeeks.org/check-reversing-sub-array-make-array-sorted/

'''
i     d      i 
0     n      0 - YES (Case Handled)
0     a      b - a + b == n, arr[0] <= arr[a]
n     0      0 - YES (Case Handled)
a     b      0 - a + b == n, arr[a-1] <= arr[n-1] (Case Handled)
a     b      c - a + b + c == n, arr[a-1] <= arr[a+b-1], arr[a] <= arr[b]
'''
def check(a):
    n = len(a)
    if n <= 2:
        return True
    i1 = d1 = i2 = 0
    i = 0
    if a[i] <= a[i+1]:
        i1 = 1
    else:
        d1 = 1
    while i < n - 1 and a[i] <= a[i+1]:
        i1 += 1
        i += 1
        if i == n - 1:
            return True
    while i < n - 1 and a[i] > a[i+1]:
        d1 += 1
        i += 1
        if i == n - 1:
            if d1 == n:
                return True
            if i1 + d1 == n:
                return a[n-1] >= a[i1 - 2]
    while i < n - 1 and a[i] <= a[i+1]:
        i2 += 1
        i += 1
        if i == n - 1:
            if i2 + d1 == n:
                return a[0] <= a[d1]
            if i1 + d1 + i2 == n:
                return a[i1+d1-1] >= a[i1 - 2] and a[i1+d1] >= a[i1]
    return False


a = [7, 5, 3, 7, 9, 11]
print(check(a))
