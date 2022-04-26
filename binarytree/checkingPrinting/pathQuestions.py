from tree import Node

#1 Print All Root to Leaf Paths
def printRootToLeafPaths(root, path):
    if root is None:
        return
    path.append(root.data)
    if root.left is None and root.right is None:
        print(path)
    printRootToLeafPaths(root.left, path)
    printRootToLeafPaths(root.right, path)
    path.pop()

#2 Print Longest Root to Leaf Path
def longestRootToLeafPathUtil(root, path, longestPath):
    if root is None:
        return
    path.append(root.data)
    if root.left is None and root.right is None and len(path) > len(longestPath[0]):
        longestPath[0] = path[:]
    longestRootToLeafPathUtil(root.left, path, longestPath)
    longestRootToLeafPathUtil(root.right, path, longestPath)
    path.pop()

def printLongestRootToLeafPath(root):
    path = []
    longestPath = [[]]
    longestRootToLeafPathUtil(root, path, longestPath)
    print(longestPath[0])

#3 Print Root to Leaf Path With Max Sum
def maxSumPathRootToLeafUtil(root, path, sum, maxSumPath, maxSum):
    if root is None:
        return
    path.append(root.data)
    sum += root.data
    if root.left is None and root.right is None and sum > maxSum[0]:
        maxSum[0] = sum
        maxSumPath[0] = path[:]
    maxSumPathRootToLeafUtil(root.left, path, sum, maxSumPath, maxSum)
    maxSumPathRootToLeafUtil(root.right, path, sum, maxSumPath, maxSum)
    path.pop()

def maxSumPathRootToLeaf(root):
    path = []
    sum = 0
    maxSum = [0]
    maxSumPath = [[]]
    maxSumPathRootToLeafUtil(root, path, sum, maxSumPath, maxSum)
    print(maxSum[0], maxSumPath[0])

#4 Check Root to Leaf Path Gives Sequence
def checkRootToLeafPathHasSequenceUtil(root, seq, index):
    if root is None or index == len(seq):
        return False
    if root.left is None and root.right is None:
        if index == len(seq) - 1 and root.data == seq[index]:
            return True
        return False
    return root.data == seq[index] and (checkRootToLeafPathHasSequenceUtil(root.left, seq, index + 1) or checkRootToLeafPathHasSequenceUtil(root.right, seq, index + 1))

def checkRootToLeafPathHasSequence(root, seq):
    return checkRootToLeafPathHasSequenceUtil(root, seq, 0)

#5 Check Root to Leaf Path With Given Sum
def printRootToLeafPathWithSum(root, path, sum, x):
    if root is None:
        return
    sum += root.data
    path.append(root.data)
    if root.left is None and root.right is None and sum == x:
        print(path)
    printRootToLeafPathWithSum(root.left, path, sum, x)
    printRootToLeafPathWithSum(root.right, path, sum, x)
    path.pop()

#6 Print root to any path with given sum
def printRootToAnyPathWithSum(root, path, sum, x):
    if root is None:
        return
    sum += root.data
    path.append(root.data)
    if sum == x:
        print(path)
    printRootToAnyPathWithSum(root.left, path, sum, x)
    printRootToAnyPathWithSum(root.right, path, sum, x)
    path.pop()

#7 Check Root to Leaf Path Gives Sequence
def checkRootToAnyPathHasSequenceUtil(root, seq, index):
    if root is None or index == len(seq):
        return False
    if index == len(seq) - 1:
        if root.data == seq[index]:
            return True
        else:
            return False
    return root.data == seq[index] and (checkRootToAnyPathHasSequenceUtil(root.left, seq, index + 1) or checkRootToAnyPathHasSequenceUtil(root.right, seq, index + 1))

def checkRootToAnyPathHasSequence(root, seq):
    return checkRootToAnyPathHasSequenceUtil(root, seq, 0)

#8 print any node to leaf path (no backward) with sum
def printAnyToLeafNoBackwardPathWithSumUtil(root, path, sum, x, prefixSums):
    if root is None:
        return
    sum += root.data
    path.append(root.data)
    if root.left is None and root.right is None:
        if sum == x:
            print(path)
        if sum - x in prefixSums:
            print(path[prefixSums[sum - x] + 1:])
    prefixSums[sum] = len(path) - 1
    printAnyToLeafNoBackwardPathWithSumUtil(root.left, path, sum, x, prefixSums)
    printAnyToLeafNoBackwardPathWithSumUtil(root.right, path, sum, x, prefixSums)
    path.pop()
    prefixSums.pop(sum)

#9 Check Any to Leaf (No Backward) has sequence
def checkAnyToLeafNotBackwardPathHasSequence(root, path, seq):
    if root is None:
        return False
    path.append(root.data)
    if root.left is None and root.right is None:
        if len(seq) <= len(path) and "".join(path[len(path) - len(seq):]) == seq:
            return True
    left = checkAnyToLeafNotBackwardPathHasSequence(root.left, path, seq) 
    right = checkAnyToLeafNotBackwardPathHasSequence(root.right, path, seq)
    path.pop()
    return left or right

#10 Any node to any node (no backward) with sum
def printAnyToAnyNoBackwardPathWithSumUtil(root, path, sum, x, prefixSums):
    if root is None:
        return
    sum += root.data
    path.append(root.data)
    if sum == x:
        print(path)
    if sum - x in prefixSums:
        print(path[prefixSums[sum - x] + 1:])
    prefixSums[sum] = len(path) - 1
    printAnyToAnyNoBackwardPathWithSumUtil(root.left, path, sum, x, prefixSums)
    printAnyToAnyNoBackwardPathWithSumUtil(root.right, path, sum, x, prefixSums)
    path.pop()
    prefixSums.pop(sum)

#11 Check Any to Any (No Backward) has sequence
def checkAnyToAnyNotBackwardPathHasSequence(root, path, seq):
    if root is None:
        return False
    path.append(root.data)
    if len(seq) <= len(path) and "".join(path[len(path) - len(seq):]) == seq:
        return True
    left = checkAnyToAnyNotBackwardPathHasSequence(root.left, path, seq) 
    right = checkAnyToAnyNotBackwardPathHasSequence(root.right, path, seq)
    path.pop()
    return left or right
'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)

printRootToLeafPaths(root, [])
print()
printLongestRootToLeafPath(root)
print()
maxSumPathRootToLeaf(root)
print()
printRootToLeafPathWithSum(root, [], 0, 34)
print()
printRootToAnyPathWithSum(root, [], 0, 11)
print()
printAnyToLeafNoBackwardPathWithSumUtil(root, [], 0, 4, {})
print()
printAnyToAnyNoBackwardPathWithSumUtil(root, [], 0, 19, {})
print()

'''
        a
      /   \
     b     c
   /   \     \
  d     e      f
       /  \   /  \
      g    h  i   j
'''
root = Node("a")
root.left = Node("b")
root.left.left = Node("d")
root.left.right = Node("e")
root.left.right.left = Node("g")
root.left.right.right = Node("h")
root.right = Node("c")
root.right.right = Node("f")
root.right.right.left = Node("i")
root.right.right.right = Node("j")

print(checkRootToLeafPathHasSequence(root, "acfj"))
print(checkRootToAnyPathHasSequence(root, "abc"))
print(checkAnyToLeafNotBackwardPathHasSequence(root, [], "cfj"))
print(checkAnyToAnyNotBackwardPathHasSequence(root, [], "be"))