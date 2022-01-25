# https://www.geeksforgeeks.org/k-smallest-elements-order-using-o1-extra-space/
# You need to use constant space.

def kSmallestElements(a, k):
    n = len(a)
    for i in range(k, n):
        maxIndex = 0
        for j in range(1, k):
            if a[j] > a[maxIndex]:
                maxIndex = j
        if a[maxIndex] > a[i]:
            x = a[maxIndex]
            for j in range(maxIndex, k):
                a[j] = a[j+1]
            a[k], a[i] = a[i], x
    return a[:k]

a = [2, 4, 5, 8, 6]
k = 3
print(kSmallestElements(a, k))
