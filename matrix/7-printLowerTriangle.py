# Also see, https://www.geeksforgeeks.org/program-check-matrix-upper-triangular/
# https://www.geeksforgeeks.org/program-check-matrix-lower-triangular/

def printLowerTriangle(m):
    R, C = len(m), len(m[0])
    for i in range(R):
        for j in range(C):
            toPrint = m[i][j] if i >= j else 0
            print(toPrint, end = " ")
        print()

def printUpperTriangle(m):
    R, C = len(m), len(m[0])
    for i in range(R):
        for j in range(C):
            toPrint = m[i][j] if i <= j else 0
            print(toPrint, end = " ")
        print()


M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

print("Lower Triangle:")
printLowerTriangle(M)
print("Upper Triangle:")
printUpperTriangle(M)

