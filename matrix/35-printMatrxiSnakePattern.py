# https://www.geeksforgeeks.org/print-matrix-snake-pattern/

def printSnake(M):
    R, C = len(M), len(M[0])
    for i in range(R):
        for j in range(C):
            if i % 2 == 0:
                print(M[i][j], end = " ")
            else:
                print(M[i][C-j-1], end = " ")
    print()

M = [[ 10, 20, 30, 40 ],
       [ 15, 25, 35, 45 ],
       [ 27, 29, 37, 48 ],
       [ 32, 33, 39, 50 ]]

printSnake(M)