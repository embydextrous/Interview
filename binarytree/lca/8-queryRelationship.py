from collections import defaultdict
from tree import Node

# Also see, https://www.geeksforgeeks.org/lowest-common-ancestor-for-a-set-of-nodes-in-a-rooted-tree/

class AncestorDescendentRelationship:
    def __init__(self, root):
        self.root = root
        self.inOutMap = defaultdict(list)
        self.fillInOutMap(root, [0])
        print(self.inOutMap)

    def fillInOutMap(self, root, time):
        if root is None:
            return
        time[0] += 1
        self.inOutMap[root.data].append(time[0])
        self.fillInOutMap(root.left, time)
        self.fillInOutMap(root.right, time)
        time[0] += 1
        self.inOutMap[root.data].append(time[0])
    
    def isAncestor(self, a, b):
        if not a in self.inOutMap or not b in self.inOutMap:
            return False
        (inA, outA) = self.inOutMap[a]
        (inB, outB) = self.inOutMap[b]
        return inB > inA and inB < outA and outB > inA and outB < outA


root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.right = Node(5)
root.left.right.left = Node(6)
root.right.right.left = Node(7)

a = AncestorDescendentRelationship(root)
print(root.left.data, root.right.data, a.isAncestor(root, root.right))
