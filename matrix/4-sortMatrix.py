from matrix import printS

def sortMatrix(m):
    R, C = len(m), len(m[0])
    a = []
    for r in range(R):
        for c in range(C):
            a.append(m[r][c])
    a.sort()
    for i in range(len(a)):
        m[i // R][i % C] = a[i]



mat = [ [ 5, 4, 7 ],
        [ 1, 3, 8 ],
        [ 2, 9, 6 ] ]

sortMatrix(mat)
printS(mat)

