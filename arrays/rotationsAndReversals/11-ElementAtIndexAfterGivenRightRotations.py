'''
An array consisting of N integers is given. There are several Right Circular Rotations of range[L..R] 
that we perform. After performing these rotations, we need to find element at a given index.
Examples : 
 
Input : arr[] : {1, 2, 3, 4, 5}
        ranges[] = { {0, 2}, {0, 3} }
        index : 1
Output : 3
Explanation : After first given rotation {0, 2}
                arr[] = {3, 1, 2, 4, 5}
              After second rotation {0, 3} 
                arr[] = {4, 3, 1, 2, 5}
After all rotations we have element 3 at given
index 1. 
'''
def elementAtIndexAfterRotations(a, rotations, idx):
    for x in range(len(rotations) - 1, -1, -1):
        (i, j) = rotations[x]
        if idx >= i and idx <= j:
            if idx == i:
                idx = j
            else:
                idx -= 1
    return a[idx]


a = [1, 2, 3, 4, 5]
print(elementAtIndexAfterRotations(a, [[0, 2], [0, 3]], 1))
