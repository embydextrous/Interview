from tree import Node, inorder

def sumUtil(root):
    if root is None:
        return
    pred = [0]
    fillPredecessor(root, pred, [0])
    print(pred)
    fillSum(root, pred, [1])

def fillPredecessor(root, pred, prev):
    if root:
        fillPredecessor(root.left, pred, prev)
        pred.append(root.data)
        fillPredecessor(root.right, pred, prev)

def fillSum(root, pred, idx):
    if root:
        fillSum(root.left, pred, idx)
        if idx[0] == len(pred) - 1:
            root.data = pred[idx[0] - 1]
        else:
            root.data = pred[idx[0] - 1] + pred[idx[0] + 1]
        idx[0] += 1
        fillSum(root.right, pred, idx)

'''
         3
      /    \  
     2      4
   /  \    /
  1    3  5  
'''

root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
sumUtil(root)
inorder(root)
print()
