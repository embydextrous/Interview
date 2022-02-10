from bst import Node, preorder

def sortedArrayToBalancedBST(a, l, r):
    if l > r:
        return None
    mid = (l + r) // 2
    root = Node(a[mid])
    root.left = sortedArrayToBalancedBST(a, l, mid - 1)
    root.right = sortedArrayToBalancedBST(a, mid + 1, r)
    return root

a = [1, 2, 3, 4, 5, 6, 7]
root = sortedArrayToBalancedBST(a, 0, len(a) - 1)
preorder(root)
print()