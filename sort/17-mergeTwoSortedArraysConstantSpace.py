'''
Input: ar1[] = {1, 5, 9, 10, 15, 20};
       ar2[] = {2, 3, 8, 13};
Output: ar1[] = {1, 2, 3, 5, 8, 9}
        ar2[] = {10, 13, 15, 20}
'''
def merge(a, b):
    i = 0
    j = 0
    k = len(a) - 1
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            b[j], a[k] = a[k], b[j]
            k -= 1
            j += 1
        else:
            i += 1
    a.sort()
    b.sort()

a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
merge(a, b)
print(a)
print(b)
        
