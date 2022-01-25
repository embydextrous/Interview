def findMostFrequentElement(a, k):
    n = len(a)
    for i in range(n):
        a[a[i] % k] += k
    maxIndex = 0
    for i in range(1, n):
        if a[i] > a[maxIndex]:
            maxIndex = i
    return maxIndex

a = [2, 3, 3, 5, 3, 4, 1, 7]
print(findMostFrequentElement(a, 8))

