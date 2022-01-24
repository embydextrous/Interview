# https://www.geeksforgeeks.org/sum-diagonals-spiral-odd-order-square-matrix/

# n is odd
def findDiagonalSum(n):
    s = 1
    i = 1
    step = 0
    while i < n * n:
        step = step + 2
        for j in range(4):
            i += step
            s += i
    return s

n = 3
print(findDiagonalSum(3))
