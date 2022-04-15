# https://www.geeksforgeeks.org/print-matrix-snake-pattern/
'''
Given an n x n matrix .In the given matrix, you have to print the elements of the matrix in the snake pattern.

Examples : 

Input :mat[][] = { {10, 20, 30, 40},
                   {15, 25, 35, 45},
                   {27, 29, 37, 48},
                   {32, 33, 39, 50}};
              
Output : 10 20 30 40 45 35 25 15 27 29
         37 48 50 39 33 32 

Input :mat[][] = { {1, 2, 3},
                   {4, 5, 6},
                   {7, 8, 9}};
Output : 1 2 3 6 5 4 7 8 9
'''

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