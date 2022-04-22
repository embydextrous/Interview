# Check b is subset of a
from collections import Counter

def checkifSubset(a, b):
    d1 = Counter(a)
    d2 = Counter(b)
    for key in d2.keys():
        if key not in d1 or d1[key] < d2[key]:
            return False
    return True

arr1 = [ 2, 1, 3, 2, 4, 5, 3, 2]
arr2 = [ 1, 2, 2, 2, 3 ]
print(checkifSubset(arr1, arr2))