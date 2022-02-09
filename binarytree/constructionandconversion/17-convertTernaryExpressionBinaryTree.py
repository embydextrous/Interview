from tree import Node, inorder

def convert(exp):
    if len(exp) == 0:
        return None
    s = []
    result = Node(exp[0])
    s.append(result)
    for i in range(1, len(exp), 2):
        node = Node(exp[i+1])
        if exp[i] == '?':
            s[-1].left = node
        if exp[i] == ':':
            s.pop()
            while len(s) > 0 and s[-1].right != None:
                s.pop()
            s[-1].right = node
        s.append(node)
    return result

exp = "a?b?c:d:e"
inorder(convert(exp))
print()

'''
     a
   /  \
  b    e
 / \
c   d
'''