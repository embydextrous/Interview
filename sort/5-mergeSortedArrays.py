# There are two sorted arrays. First one is of size m+n containing only m elements. 
# Another one is of size n and contains n elements. Merge these two arrays into the first array of size 
# m+n such that the output is sorted. 

# Assuming a is the larger array
def merge(a, b):
    m = len(b)
    n = len(a) - m
    for i in range(m + n - 1, m - 1, -1):
        if a[i] is None:
            j = i - 1
            while a[j] is None:
                j -= 1
            a[i], a[j] = a[j], a[i]
    i = m
    j = 0
    k = 0
    while i < n + m and j < m:
        if a[i] <= b[j]:
            a[k] = a[i]
            i += 1
        else:
            a[k] = b[j]
            j += 1
        k += 1
    while j < m:
        a[k] = b[j]
        j += 1
        k += 1

a = [2, 8, None, None, None, 13, None, 15, 20]
b = [5, 7, 9, 25]
merge(a, b)
print(a)