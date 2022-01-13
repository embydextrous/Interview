from ll import LinkedList, Node

# https://www.geeksforgeeks.org/construct-linked-list-2d-matrix/
def matrixToList(m, R, C, i, j):
    if i >= R or j >= C:
        return None
    node = Node(m[i][j])
    t[i][j] = node
    node.next = matrixToList(m, R, C, i, j + 1) 
    node.random = matrixToList(m, R, C, i + 1, j)   
    return node

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
t = [[None, None, None], [None, None, None], [None, None, None]]

a = LinkedList()
a.head = matrixToList(mat, len(mat), len(mat[0]), 0, 0)
for i in range(3):
    for j in range(3):
        a, b, c = t[i][j].data, t[i][j].next.data if t[i][j].next else None, t[i][j].random.data if t[i][j].random else None
        print(a, b, c)