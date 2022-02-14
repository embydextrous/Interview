from bst import Node, insert

def checkUtil(root, seq, idx):
    if root:
        checkUtil(root.left, seq, idx)
        if root.data == seq[idx[0]]:
            idx[0] += 1
        if idx[0] == len(seq):
            return
        checkUtil(root.right, seq, idx)

def check(root, seq):
    if len(seq) == 0:
        return True
    idx = [0]
    checkUtil(root, seq, idx)
    return idx[0] == len(seq)

root = Node(8)
root = insert(root, 10)
root = insert(root, 3)
root = insert(root, 6)
root = insert(root, 1)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 14)
root = insert(root, 13)
 
seq = [4, 5, 8, 14]
print(check(root, seq))