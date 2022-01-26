# Check b is subset of a
def checkifSubset(a, b):
    d1 = {x : a.count(x) for x in a}
    d2 = {x : b.count(x) for x in b}
    for key in d2.keys():
        if key not in d1 or d1[key] < d2[key]:
            return False
    return True

arr1 = [ 2, 1, 3, 2, 4, 5, 3, 2]
arr2 = [ 1, 2, 2, 2, 3 ]
print(checkifSubset(arr1, arr2))