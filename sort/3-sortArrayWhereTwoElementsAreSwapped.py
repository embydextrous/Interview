'''
Traverse the array to find two odd elements.
First odd element will occur when a[i] < a[i-1]
Second element will occur when a[i] a[i] > a[j] for i < j
In case of adjacent swap there won't be second odd element
'''

def sort(a):
    n = len(a)
    x , y = -1, -1
    for i in range(1, n):
        if a[i-1] > a[i]:
            if x == -1:
                x, y = i-1, i
            else:
                y = i
    a[x], a[y] = a[y], a[x]

# 1 2 7 4 5 6 3 8
a = [1, 2, 3, 4, 5, 6, 8, 7]
sort(a)
print(a)