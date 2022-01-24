# https://www.geeksforgeeks.org/given-1s-2s-3s-ks-print-zig-zag-way/

def printPattern(n, m, num):
    index = 0
    r = 0
    leftToRight = True
    while r < n:
        a = [0] * m
        i = 0
        while i < m:
            if num[index] == 0:
                index += 1
                continue
            else:
                if leftToRight:
                    a[i] = index + 1
                else:
                    a[m-i-1] = index + 1
                num[index] -= 1
                i += 1
        leftToRight = not leftToRight
        r += 1
        for i in a:
            print(i, end = " ")
        print()

n = 4
m = 5
num = [3, 4, 2, 2, 3, 1, 5]
printPattern(n, m, num)
