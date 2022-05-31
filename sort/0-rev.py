
# 4, 5, 8, 9, 10
# 12, 13, 14, 15, 16, 17, 18, 19, 20
# 
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


a = [1, 2, 8, 4, 5, 6, 7, 3]
sort(a)
print(a)