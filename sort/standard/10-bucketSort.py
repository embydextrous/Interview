import math
from random import randint

# Time Complexity - O(n + k), O(n^2) in worst case when everything goes to same bucket.
def bucketSort(a):
    maxi = max(a)
    mini = min(a)
    _range = maxi - mini + 1
    numBuckets = bucketSize = int(math.sqrt(_range)) + 1
    buckets = [None] * numBuckets
    for i in range(numBuckets):
        buckets[i] = []
    for i in a:
        bucketIndex = (i - mini) // bucketSize
        buckets[bucketIndex].append(i)
    k = 0
    for bucket in buckets:
        # use insertion sort here
        bucket.sort()
        for i in bucket:
            a[k] = i
            k += 1
        
a = [randint(21, 100) for i in range(200)]
bucketSort(a)
print(a)


    