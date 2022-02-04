'''
Given a root of binary tree and two integers startValue and destValue denoting the starting and 
ending node respectively. The task is to find the shortest path from the start node to the end node 
and print the path in the form of directions given below. 

Going from one node to its left child node is indicated by the letter 'L'.
Going from one node to its right child node is indicated by the letter 'R'.
To navigate from a node to its parent node, use the letter 'U'.
Examples: 

Input: root = [5, 1, 2, 3, null, 6, 4], startValue = 3, destValue = 6

              5
          /      \
       1          2
    /          /     \
  3        6         4

Output: “UURL” 
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
'''

# idxA - 0
# idxSource - 5
# idxB - 0
# pathFromLCAToDest - []
# result - UURL

# Assuming source and destination exists
def path(root, source, destination):
    if source == destination:
        return
    idxA = idxSource = root.index(source)
    idxB = root.index(destination)
    pathFromLCAToDest = []
    while idxA != idxB:
        if idxA > idxB:
            idxA = (idxA - 1) // 2
        else:
            pathFromLCAToDest.append(idxB)
            idxB = (idxB - 1) // 2       
    result = ""
    while idxSource != idxA:
        result += "U"
        idxSource = (idxSource - 1) // 2
    if idxSource == pathFromLCAToDest[-1]:
        pathFromLCAToDest.pop()
    while len(pathFromLCAToDest) > 0:
        if pathFromLCAToDest[-1] == 2 * idxSource + 1:
            result += "L"
            idxSource = 2 * idxSource + 1
        else:
            result += "R"
            idxSource = 2 * idxSource + 2
        pathFromLCAToDest.pop()
    return result

root = [5, 1, 2, 3, None, 6, 4]
source = 3
destination = 6
print(path(root, source, destination))

    
    
