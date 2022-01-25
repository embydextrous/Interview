# https://www.geeksforgeeks.org/rearrange-array-arri/

def rearrange(a):
    n = len(a)
    for i in range(n):
        while a[i] != -1 and a[i] != i:
            a[a[i]], a[i] = a[i], a[a[i]]
    
a = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
[0, 7, 2, 3, 4, 5, 12, 6, 1, 8, 11, 10, 9, 13, 14, 15, 16, 17, 18, 19]
rearrange(a)
print(a)
