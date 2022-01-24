# Next unimplemented questions
# Check if all rows of matrix are circular rotation - simple create an _ separated string for first row
# Concat other rows with itself and check if string formed by row 1 is present.
from matrix import printS

def rotateBy180(m):
    n = len(m)
    l, r = 0, n -1
    while l < r:
        m[l], m[r] = m[r], m[l]
        l, r = l + 1, r - 1
    for i in range(len(m)):
        m[i] = m[i][::-1]

matrix =[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ] 
        ]

rotateBy180(matrix)
printS(matrix)