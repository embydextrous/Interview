# Also see, https://www.geeksforgeeks.org/a-pancake-sorting-question/
def pancakeSort(a):
    n = len(a)
    for i in range(1, n):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            j -= 1
        if j + 1 != i:
            reverse(a, j + 1, i)
            reverse(a, j + 2, i)

def reverse(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

a = [1, 8, 3, 9, 10, 10, 2, 4 ]
pancakeSort(a)
print(a)
