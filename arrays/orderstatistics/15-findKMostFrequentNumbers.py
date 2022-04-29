from heapq import heappop, heappush
from collections import Counter

def kMostFrequentElements(a, k):
    d = Counter(a)
    h = []
    for key in d.keys():
        heappush(h, [-d[key], key])
    for j in range(k):
        (freq, key) = heappop(h)
        print(f"{key} occurs {-1 * freq} times in array.")
    print()

a = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
k = 4
kMostFrequentElements(a, k)