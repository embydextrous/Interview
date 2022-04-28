from random import randint

INT_MAX = 10 ** 9
INT_MIN = -10 ** 9

# Time Complexity is O(log(min(n, m)))
def median(a, b, n, m, l, r):
    cut1 = l + (r - l) // 2
    cut2 = (n + m + 1) // 2 - cut1 - 2
    l1 = INT_MIN if cut1 < 0 else a[cut1]
    r1 = INT_MAX if cut1 == n - 1 else a[cut1 + 1]
    l2 = b[cut2]
    r2 = b[cut2 + 1]
    if l1 <= r2 and l2 <= r1:
        if (n + m) % 2 == 1:
            return max(l1, l2)
        else:
            return (max(l1, l2) + min(r1, r2)) / 2
    elif l1 > r2:
        return median(a, b, n, m, l, cut1 - 1)
    else:
        return median(a, b, n, m, cut1 + 1, r)

a = [randint(1, 20) for i in range(randint(0, 10))]
b = [randint(1, 20) for i in range(randint(11, 20))]
a.sort()
b.sort()
print(a, len(a))
print(b, len(b))
print(median(a, b, len(a), len(b), 0, len(a) - 1))