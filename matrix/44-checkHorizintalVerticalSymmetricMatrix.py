def checkHorizontalSymmetry(M):
    R, C = len(M), len(M[0])
    u, d = 0, R - 1
    while u < d:
        for j in range(C):
            if M[u][j] != M[d][j]:
                return False
        u += 1
        d -= 1
    return True

def checkVerticalSymmetry(M):
    R, C = len(M), len(M[0])
    l, r = 0, C - 1
    while l < r:
        for i in range(R):
            if M[i][l] != M[i][r]:
                return False
        l += 1
        r -= 1
    return True

def checkHorizontalVerticalSymmetry(M):
    isHorizontalSymmetric = checkHorizontalSymmetry(M)
    isVerticalSymmetric = checkVerticalSymmetry(M)
    if isHorizontalSymmetric and isVerticalSymmetric:
        print("Both")
    elif isHorizontalSymmetric:
        print("Horizontal")
    elif isVerticalSymmetric:
        print("Vertical")
    else:
        print("None")

M = [[1, 0, 1],
     [0, 1, 0],
     [0, 0, 0]]

checkHorizontalVerticalSymmetry(M)