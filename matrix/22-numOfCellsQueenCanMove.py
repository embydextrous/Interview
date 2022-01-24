def numCellsQueenCanMove(x, y, obs):
    SIZE = 8
    c = 0
    nearestLeft, nearestRight, nearestTop, nearestBottom = x, SIZE - x - 1, y, SIZE - y - 1
    nearestMainDiagonalTop, nearestMainDiagonalBottom = min(x, y), SIZE - (max(x, y) + 1)
    nearestSecondDiagonalTop = y if x + y < SIZE else SIZE - x - 1
    nearestSecondDiagonalBottom = x if x + y < SIZE else SIZE - y - 1
    for obstacle in obs:
        # On Same Horizontal Axis
        if obstacle[1] == y:
            if obstacle[0] < x and x - obstacle[0] - 1 < nearestLeft:
                nearestLeft = x - obstacle[0] - 1
            elif obstacle[0] > x and obstacle[0] - x - 1 < nearestRight:
                nearestRight = obstacle[0] - x - 1
        # On Same Vertical axis
        if obstacle[0] == x:
            if obstacle[1] < y and y - obstacle[1] - 1 < nearestTop:
                nearestTop = y - obstacle[1] - 1
            elif obstacle[1] > y and obstacle[1] - y - 1 < nearestBottom:
                nearestBottom = obstacle[1] - y - 1
        # On Main Diagonal
        if x - obstacle[0] == y - obstacle[1]:
            if x > obstacle[0] and x - obstacle[0] - 1 < nearestMainDiagonalTop:
                nearestMainDiagonalTop = x - obstacle[0] - 1
            elif x < obstacle[0] and obstacle[0] - x - 1 < nearestMainDiagonalBottom:
                nearestMainDiagonalBottom = obstacle[0] - x - 1
        # On Second Diagonal
        if x + y == obstacle[0] + obstacle[1]:
            if x > obstacle[0] and x - obstacle[0] - 1 < nearestSecondDiagonalBottom:
                nearestSecondDiagonalBottom = x - obstacle[0] - 1
            elif x < obstacle[0] and obstacle[0] - x - 1 < nearestSecondDiagonalTop:
                nearestSecondDiagonalTop = obstacle[0] - x - 1
    return nearestLeft + nearestRight + nearestBottom + nearestTop + nearestSecondDiagonalTop + nearestSecondDiagonalBottom + nearestMainDiagonalTop + nearestMainDiagonalBottom

print(numCellsQueenCanMove(4, 4, []))


