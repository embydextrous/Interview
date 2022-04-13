
# Also See
# https://www.geeksforgeeks.org/program-check-idempotent-matrix/ - M * M = M
# https://www.geeksforgeeks.org/program-check-involutory-matrix/ - M * M = I
# https://www.geeksforgeeks.org/program-check-diagonal-matrix-scalar-matrix/
# https://www.geeksforgeeks.org/markov-matrix/
# https://www.geeksforgeeks.org/diagonally-dominant-matrix/
# Diagonal Matrix - All non diagonal elements must be zero.
# Scalar Matrix - All main diagonal elements must be equal and non-diagonal elements must be zero.
# Markov Matrix - Sum of elements of each row is 1
# Diagonally Dominant Matrix - In each row magnitude of diagonal element is >= sum of other elements's magnitude

def multiply(a, b):
    r1, c1, r2, c2 = len(a), len(a[0]), len(b), len(b[0])
    # Not Possible
    if c1 != r2:
        print("Not Possible..")
    # Initialize Result Matrix
    result = [[0 for i in range(c2)] for j in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += a[i][k] * b[k][j]
    return result

M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
N = [[1],
    [2],
    [3]]
     
result = multiply(M, N)

for i in result:
    print(i)
 