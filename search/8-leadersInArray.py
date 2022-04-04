# https://www.geeksforgeeks.org/leaders-in-an-array/

def printLeaders(a):
    n = len(a)
    s = [a[n-1]]
    for i in range(n - 2, -1, -1):
        if a[i] > s[-1]:
            s.append(a[i])
    while (len(s) > 0):
        print(s.pop(), end = " ")
    print()

a = [16, 17, 4, 3, 5, 2]
printLeaders(a)