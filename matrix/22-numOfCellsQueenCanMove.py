'''
Number of cells a queen can move with obstacles on the chessboard

Consider a N X N chessboard with a Queen and K obstacles. The Queen cannot pass through obstacles. 
Given the position (x, y) of Queen, the task is to find the number of cells the queen can move.

Examples: 

Input : N = 8, x = 4, y = 4, 
        K = 0
Output : 27
'''
def numCellsQueenCanMove2(N, x, y, obstacles):
    nearestLeft, nearestTop = 0, 0
    nearestRight, nearestBottom = N - 1, N - 1
    nearestMainDiagonalTop = 0 if x <= y else x - y
    nearestMainDiagonalBottom = N - 1 if x >= y else x + N - y - 1
    nearestSecDiagonalTop = N - 1 if x + y >= N else x + y
    nearestSecDiagonalBottom = 0 if x + y < N else x - (N - y - 1)
    for obstacle in obstacles:
        (i, j) = obstacle
        # Check if anything on left and right
        if j == y:
            if i < x and i > nearestLeft:
                nearestLeft = i + 1
            if i > x and i < nearestRight:
                nearestRight = i - 1
        # Check if anything on top and bottom
        if i == x:
            if j < y and j > nearestTop:
                nearestTop = j + 1
            if j > y and j < nearestBottom:
                nearestBottom = j - 1
        # Check obstacle on main diagonal
        if (x-i) == (y-j):
            # Check if top
            if i < x and i > nearestMainDiagonalTop:
                nearestMainDiagonalTop = i + 1
            if i > x and i < nearestMainDiagonalBottom:
                nearestMainDiagonalBottom = i - 1
        # Check obstacle on second diagonal
        if (x-i) == -1 * (y-j):
            # Check if top
            if i < x and i > nearestSecDiagonalBottom:
                nearestSecDiagonalBottom = i + 1
            if i > x and i < nearestSecDiagonalTop:
                nearestSecDiagonalTop = i - 1
    print(x, y, nearestMainDiagonalTop, nearestMainDiagonalBottom, nearestSecDiagonalBottom, nearestSecDiagonalTop)
    return (x - nearestLeft) + (nearestRight - x) + (y - nearestTop) + (nearestBottom - y) \
            + (x - nearestMainDiagonalTop) + (nearestMainDiagonalBottom - y) \
            + (x - nearestSecDiagonalBottom) + (nearestSecDiagonalTop - y)


print(numCellsQueenCanMove2(8, 4, 4, [[5, 5]]))


