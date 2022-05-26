def tripletSum(a, x):
    # To implement two pointer algorithm
    a.sort()
    n = len(a)
    for i in range(n - 2):
        # fixes ith element so we need to find if x - a[i] sum exists in remaining array
        l = 0
        r = n - 1
        while l < r:
            if a[l] + a[r] + a[i] == x:
                return True
            elif a[l] + a[r] + a[i] < x:
                l += 1
            else:
                r -= 1
    return False

a = [12, 3, 4, 1, 6, 9]
x = 26
print(tripletSum(a, x))