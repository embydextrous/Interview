# https://www.geeksforgeeks.org/elements-to-be-added-so-that-all-elements-of-a-range-are-present-in-array/

def countMissing(a):
    a.sort()
    c = 0
    for i in range(1, len(a)):
        c += a[i] - a[i-1] - 1
    return c

a = [3, 5, 8, 6]
print(countMissing(a))