# https://www.geeksforgeeks.org/sum-matrix-element-absolute-difference-row-column-numbers/
def sum(n):
    i = 1
    s = 0
    for j in range(n-1, 0, -1):
        s += i * j
        i += 1
    return 2 * s

n = 4
print(sum(n))