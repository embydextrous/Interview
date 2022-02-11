from bst import Node, insert

# Also see, https://www.geeksforgeeks.org/count-pairs-from-two-bsts-whose-sum-is-equal-to-a-given-value-x/
# Also see, https://www.geeksforgeeks.org/find-pair-given-sum-bst/

def traverse(root, s):
    if root:
        s.add(root.data)
        traverse(root.left, s)
        traverse(root.right, s)

def printPairs(root, s, sum):
    if root:
        if sum - root.data in s:
            print((sum - root.data, root.data), end = " ")
        printPairs(root.left, s, sum)
        printPairs(root.right, s, sum)

def printPairsWithSum(a, b, sum):
    s = set()
    traverse(a, s)
    printPairs(b, s, sum)
    print()

root1 = Node(8)
root1 = insert(root1, 10)
root1 = insert(root1, 3)
root1 = insert(root1, 6)
root1 = insert(root1, 1)
root1 = insert(root1, 5)
root1 = insert(root1, 7)
root1 = insert(root1, 14)
root1 = insert(root1, 13)
 
    # second BST
root2 = Node(5)
root2 = insert(root2, 18)
root2 = insert(root2, 2)
root2 = insert(root2, 1)
root2 = insert(root2, 3)
root2 = insert(root2, 4)

printPairsWithSum(root1, root2, 10)