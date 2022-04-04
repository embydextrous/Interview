# https://www.geeksforgeeks.org/position-element-stable-sort/

def positionAfterStableSort(a, idx):
    c = 0
    for i in range(len(a)):
        if a[i] < a[idx] or (a[i] == a[idx] and i < idx):
            c += 1
    return c

a = [3, 4, 3, 5, 2, 3, 4, 3, 1, 5]
print(positionAfterStableSort(a, 5))
