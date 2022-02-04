def lca(parent, a, b):
    v = set()
    while True:
        v.add(a)
        a = parent[a]
        if a == -1:
            break
    while True:
        if b in v:
            return b
        b = parent[b]
        if b == -1:
            return None

'''
            2
          /   \
         3     8
        /     /
       9     7
     /   \    \
    1    6     5
       /   \
      0     4
'''
parent = [6, 9, -1, 2, 6, 7, 9, 8, 2, 3]
print(lca(parent, 0, 4))