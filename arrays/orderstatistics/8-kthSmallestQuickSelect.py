import sys
import random

def randomPartition(a, l, r):
    n = r - l + 1
    x = random.randint(1, 100) % n
    a[l+x], a[r] = a[r], a[l+x]
    return partition(a, l, r)

def partition(a, l, r):
    x = a[r]
    i = l
    for j in range(l, r):
        if a[j] <= x:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i
        
def kthSmallest(a, l, r, k):
    if l <= r and k - 1 >= l and k - 1 <= r :
        position = randomPartition(a, l, r)
        if position == k - 1:
            return a[position]
        if position > k - 1:
            return kthSmallest(a, l, position - 1, k)
        return kthSmallest(a, position + 1, r, k)

arr = [2, 1, 9, 6, 8, 4, 5, 7]
n = len(arr)
for i in range(n+1):
    print(kthSmallest(arr, 0, n-1, i))
