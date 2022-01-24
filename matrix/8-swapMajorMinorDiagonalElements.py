from matrix import printS

# Also see:
# https://www.geeksforgeeks.org/squares-of-matrix-diagonal-elements/
# https://www.geeksforgeeks.org/center-element-of-matrix-equals-sums-of-half-diagonals/
# https://www.geeksforgeeks.org/program-swap-upper-diagonal-elements-lower-diagonal-elements-matrix/ - useful for symmetric and transpose of square matrices

def swapDiagonalElements(m):
    n = len(m)
    for i in range(n):
        m[i][i], m[i][n-i-1] = m[i][n-i-1], m[i][i]

matrix = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]]

swapDiagonalElements(matrix)
printS(matrix)
