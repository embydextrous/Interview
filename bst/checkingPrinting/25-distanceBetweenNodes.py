from bst import Node, insert

# Assuming a < b
# Assuming key exists
def distance(root, a, b):
    if root.data >= a and root.data <= b:
        return distanceDown(root, a) + distanceDown(root, b)
    if root.data < a:
        return distance(root.right, a, b)
    return distance(root.left, a, b)

def distanceDown(root, x):
    print(root.data, x)
    if root.data == x:
        return 0
    if root.data < x:
        return 1 + distanceDown(root.right, x)
    return 1 + distanceDown(root.left, x)


'''
            20
         /      \
       10       30
      /  \     /  \
     5    15  25   35

'''
root = Node(20)
insert(root, 10)
insert(root, 5)
insert(root, 15)
insert(root, 30)
insert(root, 25)
insert(root, 35)
a, b = 5, 20
print(distance(root, a, b))