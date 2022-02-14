from bst import Node, insert

def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)

def kthSmallestElement(root, k):
    while root:
        if root.left:
            rightMost = root.left
            while rightMost.right and rightMost.right != root:
                rightMost = rightMost.right
            if rightMost.right == root:
                k -= 1
                if k == 0:
                    return root.data
                rightMost.right = None
                root = root.right
            else:
                rightMost.right = root
                root = root.left
        else:
            k -= 1
            if k == 0:
                return root.data
            root = root.right

def findMedian(root):
    if root is None:
        return None
    s = size(root)
    if s % 2 == 1:
        return kthSmallestElement(root, s // 2 + 1)
    else:
        return (kthSmallestElement(root, s // 2) + kthSmallestElement(root, s // 2 + 1)) / 2

root = Node(50) 
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

print(findMedian(root))