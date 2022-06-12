from typing import Counter


def isSubset(a, b):
    d = Counter(a)
    for i in b:
        if i not in d or d[i] == 0:
            return False
        d[i] -= 1
    return True

a = [1, 6, 3, 6, 2, 7, 5, 1, 6, 3, 6, 5, 4, 1, 4, 2, 3, 6, 7, 3, 2, 8, 7, 4, 7, 6, 2, 4, 2, 3]
b = [1, 1, 1, 6, 7, 8, 8]
print(isSubset(a, b))