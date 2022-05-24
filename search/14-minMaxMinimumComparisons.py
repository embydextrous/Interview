# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

def getMinMax(a, l, r):
    # Only one element
    if l == r:
        return (a[l], a[l])
    # Two elements
    if r == l + 1:
        return (min(a[l], a[r]), max(a[l], a[r]))
    m = l + (r - l) // 2
    (min1, max1) = getMinMax(a, l, m)
    (min2, max2) = getMinMax(a, m + 1, r)
    return (min(min1, min2), max(max1, max2))

a = [1000, 11, 445, 1, 330, 3000]
print(getMinMax(a, 0, len(a) - 1))