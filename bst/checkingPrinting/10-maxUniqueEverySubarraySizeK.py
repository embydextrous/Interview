import sys
from typing import Counter

def solution(a, k):
    d = Counter(a[:k])
    n = len(a)
    maxi = -sys.maxsize-1
    for key in d.keys():
        if d[key] == 1:
            maxi = max(maxi, key)
    print(maxi, end = " ")
    for i in range(k, n):
        enter, exit = a[k], a[i-k]
        if enter in d:
            if enter == maxi:
                maxi = -sys.maxsize-1
            d[enter] += 1
        else:
            d[enter] = 1
            maxi = max(maxi, enter)
        if exit in d:
            d[exit] -= 1
            if d[exit] == 1:
                maxi = max(maxi, exit)
            if d[exit] == 0:
                d.pop(exit)
        print(maxi, end = " ")
    print()
            

a = [3, 3, 3, 4, 4, 2]
k = 4
solution(a, k)

