'''
Traverse the array to find two odd elements.
First odd element will occur when a[i] < a[i-1]
Second element will occur when a[i] a[i] > a[j] for i < j
In case of adjacent swap there won't be second odd element
'''

def sort(a):
    n = len(a)
    f, s = None, None
    for i in range(1, n):
        if a[i] < a[i-1]:
            if f is None:
                f = i - 1
            else:
                s = i
    if s is None:
        a[f], a[f+1] = a[f+1], a[f]
    else:
        a[f], a[s] = a[s], a[f]

# 1 2 7 4 5 6 3 8
a = [1, 2, 3, 4, 5, 6, 8, 7]
sort(a)
print(a)