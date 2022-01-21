def findLargestPairSum(a):
    max1, max2 = max(a[0], a[1]), min(a[0], a[1])
    for i in range(2, len(a)):
        if a[i] >= max1:
            max1, max2 = a[i], max1
        elif a[i] < max1 and a[i] > max2:
            max2 = a[i]
    return max1 + max2

a = [12, 34, 10, 6, 40]
print(findLargestPairSum(a))