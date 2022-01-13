def findCelebrity(n):
    candidate = -1
    i, j = 0, n - 1
    while i < j:
        if knows(i, j):
            i += 1
        else:
            j -= 1
    candidate = i
    for k in range(n):
        if candidate != k:
            if knows(candidate, k) or not knows(k, candidate):
                return -1
    return candidate

N = 4
 
# Person with 2 is celebrity
MATRIX = [[0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 1, 0]]

def knows(i, j):
    return MATRIX[i][j] == 1

print(findCelebrity(4))
